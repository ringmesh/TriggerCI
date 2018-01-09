import json, requests, sys

project=sys.argv[1]
user_token="2h2q2pzTsgdiGoPJNqQP"


body={
  "request": {
    "branch":"master"
  }
}

header={
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Travis-API-Version": "3",
  "Authorization": "user_token"
}

with open("dependees/%s" % project) as file:
    dependees = file.read().splitlines()

for dependee in dependees:
  url="https://api.travis-ci.org/repo/ringmesh%2Fdependee/requests"
  result=requests.post(url, data=json.dumps(body), headers=header)
  print(result.content)
