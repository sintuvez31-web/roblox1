import requests

TOKEN = "TOKENINI_BURAYA_YAZ"
CHANNEL_ID = "KANAL_IDINI_BURAYA_YAZ"

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
data = {"content": "roblox.com.ug"}

requests.post(url, headers=headers, json=data)
print("Link gönderildi!")
