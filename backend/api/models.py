from django.db import models

class Opinion(models.Model):
        id = models.AutoField(primary_key = True)
        data = models.DateField();
        name = models.CharField(max_length= 32)
        email = models.CharField(max_length= 32)
        title = models.CharField(max_length= 32)
        content = models.CharField(max_length=2000)
