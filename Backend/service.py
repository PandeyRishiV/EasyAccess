from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api
import subprocess
import shlex
from utils.git_util import clone, pull, push, add, commit, branch
from utils.general_util import get_current_working_directory
from utils.file_util import copy_dir, copy_files

class Hello(Resource):
    
    def get(self):
        # print(g.scripts_path)
        subprocess.run(['bash','./scripts/echo.sh', 'Testing...', 'Testing2'])
        # subprocess.call(shlex.split('./scripts/echo.sh param1'), shell = True)
        return jsonify({'message':'Hello World'})

    def post(self):
        data = request.get_json()
        return make_response(jsonify({'message': data}), 200)

class CopyFiles(Resource):

    def post(self):
        data = request.get_json()
        source = data['source']
        destination = data['destination']
        response = copy_files(source, destination)
        return response

class CopyDir(Resource):

    def post(self):
        data = request.get_json()
        source = data['source']
        destination = data['destination']
        response = copy_dir(source, destination)
        return response

class GetCurrentWorkingDirectory(Resource):

    def get(self):
        response = get_current_working_directory()
        return response


# # We need to ask for personal access token in order to do any of the git operations
class CloneGitRepo(Resource):

    def post(self):
        data = request.get_json()
        git_url = data['git_url']
        repo_dir = data['repo_dir']
        response = clone(git_url, repo_dir)
        return response

class PullGitRepo(Resource):

    def post(self):
        data = request.get_json()
        branch = data['branch']
        local_repo_path = data['local_repo_path']
        response = pull(branch, local_repo_path)
        return response

class PushGitRepo(Resource):

    def post(self):
        data = request.get_json()
        branch = data['branch']
        local_repo_path = data['local_repo_path']
        response = push(branch, local_repo_path)
        return response

class GitAdd(Resource):
    
    def post(self):
        data = request.get_json()
        files = data['files']
        local_repo_path = data['local_repo_path']
        response = add(files, local_repo_path)
        return response

class GitCommit(Resource):

    def post(self):
        data = request.get_json()
        message = data['message']
        local_repo_path = data['local_repo_path']
        response = commit(message, local_repo_path)
        return response

class GitBranch(Resource):

    def post(self):
        data = request.get_json()
        branch_name = data['branch_name']
        local_repo_path = data['local_repo_path']
        response = branch(branch_name, local_repo_path)
        return response