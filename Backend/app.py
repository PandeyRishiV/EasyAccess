from flask import Flask
from flask_restful import Api
from service import Hello, CopyFiles, CloneGitRepo, PullGitRepo, PushGitRepo, GitAdd, GitCommit, GitBranch, GetCurrentWorkingDirectory, CopyDir
# from flask_cors import CORS

# ÷g.scripts_path = ["Testing..."]
app = Flask(__name__)
# app.app_context().push()
api = Api(app)

api.add_resource(Hello, '/')
api.add_resource(CloneGitRepo, '/clone-git-repo')
api.add_resource(PullGitRepo, '/pull-git-repo')
api.add_resource(PushGitRepo, '/push-git-repo')
api.add_resource(GitAdd, '/git-add')
api.add_resource(GitCommit, '/git-commit')
api.add_resource(GitBranch, '/git-branch')
api.add_resource(GetCurrentWorkingDirectory, '/get-current-working-directory')
api.add_resource(CopyFiles, '/copy-files')
api.add_resource(CopyDir, '/copy-dir')


if __name__ == '__main__':
    app.run(debug = True)