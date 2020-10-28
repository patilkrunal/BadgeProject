from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
#from memberships.models import Membership


class Branch_of_study(models.Model):
    branch_of_study = models.CharField(max_length=150)

    def __str__(self):
        return '{}'.format(self.branch_of_study)


class Course(models.Model):
    creator = models.ForeignKey(User,on_delete = models.CASCADE)
    slug = models.SlugField()
    title = models.CharField(max_length=30)
    branch_of_study = models.ForeignKey(Branch_of_study,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_time = models.DateTimeField(auto_now=True)
    starting_date = models.DateField(null=True)
    ending_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()
