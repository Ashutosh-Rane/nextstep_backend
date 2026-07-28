import requests
from google.oauth2.service_account import Credentials


WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxwTm1COWzzNO4zJ-cgPbrHwzyyguhUTClRJI9V4Gzhw3oISB5suMLPsor87SilE2Xi/exec"


def process_job(data):
    try:
        # Send data to Google Sheet
        response = requests.post(WEB_APP_URL, json=data, timeout=10)
        response.raise_for_status()

        print("========= JOB SAVED TO GOOGLE SHEET =========")
        print("Job Name    :", data.get("job_name"))
        print("Job ID      :", data.get("job_id"))
        print("Location    :", data.get("location"))
        print("Experience  :", data.get("exp"))
        print("Education   :", data.get("education"))
        print("Skills      :", data.get("skills"))
        print("Description :", data.get("description"))
        print("Sheet Response:", response.text)
        print("============================================")

        return {
            "message": "Job received and saved to Google Sheet successfully",
            "sheet_response": response.json()
        }

    except Exception as e:
        print("Error while saving to sheet:", str(e))
        return {
            "message": "Failed to save job to Google Sheet",
            "error": str(e)
        }


