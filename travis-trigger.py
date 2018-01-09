import json, requests, sys

project=sys.argv[1]

body={
  "request": {
    "branch":"master"
  }
}

header={
  "Content-Type": "application/json",
  "Accept": "application/json",
  "Travis-API-Version": "3",
  "Authorization": "token 2h2q2pzTsgdiGoPJNqQP"
}

with open("dependees/%s" % project) as file:
    dependees = file.read().splitlines()

for dependee in dependees:
  url="https://api.travis-ci.org/repo/ringmesh%2F%s/requests" % dependee
  result=requests.post(url, data=json.dumps(body), headers=header)
  print(result.content)
