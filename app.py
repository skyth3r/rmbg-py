from flask import Flask, request, render_template, send_file
from flask_login import login_required
from rembg import remove
from PIL import Image
from io import BytesIO
from db import db, User
from auth import auth_bp, login_manager
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ALLOW_REGISTRATION'] = config.ALLOW_REGISTRATION

db.init_app(app)
login_manager.init_app(app)
app.register_blueprint(auth_bp)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        
        if file:
            try:
                input_image = Image.open(file.stream)
                output_image = remove(input_image, post_process_mask=True)
                img_io = BytesIO()
                output_image.save(img_io, 'PNG')
                img_io.seek(0)
                return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='_rmbg.png')
            except Exception as e:
                return f"An error occurred: {str(e)}", 500

        return redirect(url_for('index'))
    
    return render_template('index.html')


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)