from utils.general_util import create_directory, change_directory, get_current_working_directory
import subprocess
from flask import make_response, jsonify

def clone(url, repo_dir):
    try:
        # Extracting repo name from repo url
        repo_name = url.split('.git')[0].split('/')[-1]
        create_directory(repo_name)
        repo_dir = repo_dir + '/' + repo_name
        subprocess.run(['bash','/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_clone.sh', url, repo_dir])
        return make_response(jsonify({'message': 'Repository cloned successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def push(branch, local_repo_path):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_push.sh', local_repo_path, branch], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': response}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def pull(branch, local_repo_path):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_pull.sh', local_repo_path, branch], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': response}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def add(files, local_repo_path):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_add.sh', local_repo_path, files], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': 'File(s) added successfully'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def commit(message, local_repo_path):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_commit.sh', local_repo_path, message], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': 'Git commit completed successfully.'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)

def branch(branch_name, local_repo_path):
    try:
        response = subprocess.run(['bash', 
            '/Users/viyadav/Vishwa\'s_Workspace/Practice_Projects/flask-api/scripts/darwin/git_branch.sh', local_repo_path, branch_name], 
            capture_output=True, text=True).stdout
        return make_response(jsonify({'message': branch_name + ' branch created successfully.'}), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'Something went wrong'}), 500)