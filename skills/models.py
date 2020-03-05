from django.db import models

class Skills(models.Model):
    skill_name = models.CharField(max_length=250)
    skill_logo = models.CharField(max_length=250)
    skill_tag_line = models.CharField(max_length=500)

    def __self__(self):
        return self.skill_name + " - "+ self.skill_tag_line + " - "+ self.skill_logo

class Projects(models.Model):
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_details = models.CharField(max_length=500)
    project_link = models.CharField(max_length=500)
    project_pic = models.CharField(max_length=250)

