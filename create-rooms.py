# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests

access_token = 'NTcxYmQ3NTUtMWY1NC00MThiLWFiNmUtZjFkNTNmNWEwNjQxMzJhYTFhYzEtODU5_P0A1_9282fec5-949a-498f-b4a3-03239519286e'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'Binary101 SE group!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
