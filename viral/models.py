from django.db import models

class BaseModel(models.Model):

    create_time = models.DateTimeField(auto_now_add=True, null=True)
    create_user = models.CharField(max_length=30, null=True, default='system')
    change_time = models.DateTimeField(auto_now=True, null=True)
    change_user = models.CharField(max_length=30, null=True, default='system')

    class Meta:
        abstract = True

class Stats(BaseModel):
    class Meta:
        db_table = 'type'

    date = models.DateField(null = True)
    state = models.CharField(max_length=2, null = True, blank = True)
    positive = models.IntegerField(null = True)
    positiveIncrease = models.IntegerField(null = True)
    totalTestResultsIncrease = models.IntegerField(null = True)
    total =  models.IntegerField(null = True)

# Create your models here.
