# Fill in this file with the messages code from the Webex Teams exercise
import requests

access_token = 'NTcxYmQ3NTUtMWY1NC00MThiLWFiNmUtZjFkNTNmNWEwNjQxMzJhYTFhYzEtODU5_P0A1_9282fec5-949a-498f-b4a3-03239519286e'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzJhZGZhODAtNjA5OC0xMWVjLWFjOTItMjdiZDAxY2U1YzI1'
message = 'Hello to all Support Engineers! We would like to notify all of you that there are 3 new features in the network. '
url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
