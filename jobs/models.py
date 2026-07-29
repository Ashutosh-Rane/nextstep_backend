from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=200)
    job_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    skills = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.job_name