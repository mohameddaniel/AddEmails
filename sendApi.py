import requests
import json



def SendMail(data):
    url = "https://spamdetectionbackend-production.up.railway.app/sendEmail"
    payload = json.dumps(data) 
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)  
    print(response.text)