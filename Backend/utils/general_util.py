import os
import subprocess
from flask import make_response, jsonify

def create_directory(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def change_directory(path):
    try:
        subprocess.run(['bash', '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/cd.sh', path])
    except Exception as e:
        return 'Something went wrong'

def get_current_working_directory():
    try:
        response = subprocess.run(['pwd'], capture_output=True, text=True).stdout
        return make_response(jsonify({'message': response}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong'}), 500)