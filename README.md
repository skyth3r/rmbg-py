# rmbg py

**Note - This project is a work is progress**

A Python web app build using [Flask](https://flask.palletsprojects.com/en/3.0.x/) and [Docker](https://www.docker.com/) to remove backgrounds from images using the [Rembg package](https://github.com/danielgatis/rembg).

This project is based off the code from [Beyond Fireship's deploy serverless containers tutorial](https://www.youtube.com/watch?v=cw34KMPSt4k) with a number of changes made to the html templates and css and a login system.

## How to use

**Local installation**
1. Download repository
2. Navigate to the repository and create a virtual environment - `python3 -m venv rmbg-py`
3. Activate the virtual environment - `. rmgb-py/bin/activate`
4. Rename `example_config.py` to `config.py` and update the SECRET_KEY variable (hint - use `python3 -c 'import secrets; print(secrets.token_hex())'` to generate a value for this variable)
5. Install dependencies with `pip install -e .`
6. Run app with `python app.py` and view it at `http://127.0.0.1:5100/`