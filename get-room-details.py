# Fill in this file with the code to get room details from the Webex Teams exercise
import requests

access_token = 'NTcxYmQ3NTUtMWY1NC00MThiLWFiNmUtZjFkNTNmNWEwNjQxMzJhYTFhYzEtODU5_P0A1_9282fec5-949a-498f-b4a3-03239519286e'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzJhZGZhODAtNjA5OC0xMWVjLWFjOTItMjdiZDAxY2U1YzI1'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
