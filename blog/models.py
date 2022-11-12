from django.db import models

class ProjectBlog(models.Model):
    title = models.TextField(max_length=50)
    date = models.DateField(blank=True,max_length=20)
    desc = models.CharField(blank=True,max_length=1000)

    def __str__(self):
        return self.title
