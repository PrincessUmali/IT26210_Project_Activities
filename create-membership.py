# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests

access_token = 'NTcxYmQ3NTUtMWY1NC00MThiLWFiNmUtZjFkNTNmNWEwNjQxMzJhYTFhYzEtODU5_P0A1_9282fec5-949a-498f-b4a3-03239519286e'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzJhZGZhODAtNjA5OC0xMWVjLWFjOTItMjdiZDAxY2U1YzI1'
person_email = 'charleschristian.tuazon.iics@ust.edu.ph'

url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
