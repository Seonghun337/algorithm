import requests, json
xauth = "x_auth_token: 29b1b291fdb69531d623138f8a384880"
base = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

# return 
def initialize(problem):
    req_header = {
        "X-Auth-Token": xauth,
        "Content-Type": "application/json"
    }
    req_body = {
        "problem": problem,
    }
    
    url_start = "/start"
    print(base + url_start)
    print(req_header)
    print(req_body)
    response = requests.post(base + url_start, headers = req_header, data = req_body)
    if response == "200":
        print(response.json())
    else:
        print(response)
    
initialize(1)