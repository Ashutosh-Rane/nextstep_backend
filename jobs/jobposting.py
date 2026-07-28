
from google.oauth2.service_account import Credentials

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxwTm1COWzzNO4zJ-cgPbrHwzyyguhUTClRJI9V4Gzhw3oISB5suMLPsor87SilE2Xi/exec"  # paste your URL here

def process_job(data):

    '''response = data.post(WEB_APP_URL, json=data)
    response.raise_for_status()'''
    print("========= JOB RECEIVED =========")

    print("Job Name :", data.get("job_name"))
    print("Job ID   :", data.get("job_id"))
    print("Location :", data.get("location"))
    print("Exp      :", data.get("exp"))
    print("Education:", data.get("education"))
    print("Skills   :", data.get("skills"))
    print("Description:", data.get("description"))

    print("===============================")

    return {
        "message": "Job received successfully"
    }