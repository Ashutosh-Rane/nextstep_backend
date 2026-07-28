def process_job(data):

    print("========= JOB RECEIVED =========")

    print("Job Name :", data.get("job_name"))
    print("Job ID   :", data.get("job_id"))
    print("Location :", data.get("location"))
    print("Exp      :", data.get("experience"))
    print("Education:", data.get("education"))
    print("Skills   :", data.get("skills"))
    print("Description:", data.get("description"))

    print("===============================")

    return {
        "message": "Job received successfully"
    }