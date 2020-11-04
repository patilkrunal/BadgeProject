from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Branch_of_study(models.Model):
    branch_of_study = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.branch_of_study}'


class Course(models.Model):
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    branch_of_study = models.ForeignKey(Branch_of_study,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        # self.creator = request.user.username
        return super(Course, self).save(*args, **kwargs)
