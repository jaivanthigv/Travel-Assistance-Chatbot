import requests

# Test the /get route of your Flask chatbot
res = requests.post("http://127.0.0.1:5000/get", data={"msg":"Hello"})
print(res.json())
