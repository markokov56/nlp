import json, requests, base64

client_key = 'Q0XtFh6u2uCTRglDpvHzKGhoY'
client_secret = 'QW0FuM9xWp5e19T7WfwPhGXUN4A48lHnSlrrAhCEKWwYUbeVTA'

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

print(auth_resp.status_code)
print(auth_resp.json().keys())

access_token = auth_resp.json()['access_token']
print(access_token)

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
}

search_params = {
    #'q': 'to:@EmmanuelMacron',
    'q': 'to:@EmmanuelMacron since:2019-01-01',
    'result_type': 'mixed',
    'count': 10,
    'tweet_mode': 'extended'
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers, params=search_params)

print(search_resp.status_code)

print("end py run")



