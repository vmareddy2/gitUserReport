'''
Program will parse commits by user login in a given repo.
'''


import os, sys, argparse, requests, json

#Use Argument Parser
argParser = argparse.ArgumentParser(description='get User gitCommit History')
argParser.add_argument('--login',help='user login',required=True)
argParser.add_argument('--repo',help='repository to point to owner:/repo',required=True)

args = argParser.parse_args()


try:

    url = 'https://api.github.com/repos/'+args.repo+'/commits?author='+args.login
    req_header = { "Authorization": "token "+os.environ['USER_GIT_TOKEN'] }

    while True:
        #get list of commits and parse them
        response = requests.get(url,headers=req_header)

        if (response.status_code != 200):
            print("Error receiving commits")
            sys.exit()

        parsed_json = json.loads(response.content)

        #if length = 0 then no commits exist
        if(len(parsed_json) == 0):
            print("User: "+args.login+" has made no commits to repo: "+args.repo)
            sys.exit()

        #Go through each commit
        for commit in parsed_json:
            print("------")
            print('sha:'+ commit['sha'])
            print('author:'+ commit['author']['login'])
            print('authored date:'+commit['commit']['author']['date'])
            print('message:'+commit['commit']['message'])

        # if Response contain links to next page - follow them
        if 'next' in response.links.keys():
            url = response.links['next']['url']
        else:
            print("------")
            print("Done with commits for user")
            break

except Exception as e:
    print("An error occured"+str(e))
