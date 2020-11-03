from django.db import models
from courses.models import Course


class StudentMembership(models.Model):
    student_name = models.CharField(max_length=30)
    email_id = models.EmailField(max_length=254)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student_name
