from django.db import models

class Family_members(models.Model):
    name = models.CharField(max_Length=40)
    age = models.IntegerField()
    job = models.Charfield(max_Length=40)
    last_active_whapp = models.DateField()
    
