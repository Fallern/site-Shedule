from django.db import models


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "groups"
        verbose_name_plural = "groups"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=40)
    teacher = models.CharField(max_length=60, blank=True)
    code_conference = models.CharField(max_length=20, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "lessons"
        db_table = 'lessons'

    def __str__(self):
        return f"{self.name} {self.date}"