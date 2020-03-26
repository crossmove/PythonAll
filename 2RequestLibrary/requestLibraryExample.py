import requests ##pip install requests   #requests   2.23.0
import json

def  requestMethod1():
    url1="http://www.test.com"
    payload1={"username": "user1","password","password123"}
    header1={'Content-type':'application/json', 'Accept':'text/plain'}
    response =requests.post(url1,data=json.dumps(paypayload1load), headers=header1)
    auth_bearer = "Bearer "+response.json()['data']['token']
    sessionExpiry  =response.json()['data']['expiry']
    return auth_bearer, sessionExpiry