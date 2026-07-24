import requests

TOKEN = "MTUzMDIxMjM4OTEwNTE3NjYzOA.GJN5XJ.wEGEMLz_vGeImmJDQtJJeiKRvG8idp5mtbizN8"
CHANNEL_ID = "KANAL_ID"

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
data = {"content": "Test mesajı"}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())
