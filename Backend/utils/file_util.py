import shutil
import os
from flask import make_response, jsonify
import subprocess
 
def copy_files(source, destination):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/cp.sh', source, destination], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': 'File(s) copied successfully'}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def copy_dir(src_dir, dest_dir):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/cp_dir.sh', src_dir, dest_dir], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': 'Directory copied successfully'}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'Something went wrong'}), 500)