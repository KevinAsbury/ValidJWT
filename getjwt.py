import http.client

'''
This will fetch the jwt access token from AUTH0
'''

AUTH0_DOMAIN = '[[YOUR PROFILE NAME]].auth0.com'
CLIENT_ID = '[[Under Applications Section]]'
CLIENT_SECRET = '[[Under Applications Section]]'
API_AUDIENCE = '[[Under APIs Section]]'

conn = http.client.HTTPSConnection(f"{AUTH0_DOMAIN}")
payload = f'{{"client_id":"{CLIENT_ID}","client_secret":"{CLIENT_SECRET}","audience":"{API_AUDIENCE}","grant_type":"client_credentials"}}'
headers = { 'content-type': "application/json" }
conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
