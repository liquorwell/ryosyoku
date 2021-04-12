import requests

url = "https://notify-api.line.me/api/notify"
access_token = 'token'
headers = {'Authorization': 'Bearer ' + access_token}

f = open('ryosyoku.txt', 'r')

message_list = f.read().split('\n\n')
for message in message_list:
    message = '\n' + message    #最初に改行
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)

f.close()
