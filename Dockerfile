FROM python:3.12-slim

# download https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx to repository root directory
# copy model from repository root to avoid unnecessary download
COPY u2net.onnx /home/.u2net/u2net.onnx

WORKDIR /rmbg

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5100

CMD ["python", "run.py"]