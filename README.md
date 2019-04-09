# User Report of Git Commits in a Repo

<p>Program expects the following: <br>
     program arguments:<br>
        a. login = user-login in the git repo (eg: vmareddy2)<br>
        b. repo = repo name in format owner:/repo (eg: vmareddy2/awsTC)
     environment variable:<br>
        USER_GIT_TOKEN = personal access token to the git repository
Requirements: Python 2.7
</p>

<p>1. Program checks commits only in the default branch<br>
2. Program follows any pagination links
</p>

###### How to run
python userReport.py --login=gohabereg --repo=codex/editor.js 