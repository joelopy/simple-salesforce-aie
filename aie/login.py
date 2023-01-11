import json
from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'aie--acudev.sandbox.my'

print(security_token)

session_id, instance = SalesforceLogin(username=username, password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance_url=instance, session_id=session_id)
print(sf)