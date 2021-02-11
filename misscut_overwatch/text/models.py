from django.db import models

from django.utils.timezone import now


class TextFile(models.Model):
    create_time = models.DateTimeField(default=now)
    file = models.FileField(upload_to="text_files", blank=True, null=True)
    ret_file = models.FileField(upload_to="results", blank=True, null=True)
    finish_flag = models.IntegerField(default=0)
    operate_time = models.DateTimeField(default=now)
    username = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.file.name + " " + str(self.create_time)

# Create your models here.

