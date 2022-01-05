from django.db import models
class Srirama(models.Model):
    Name=models.CharField(max_length=20)
    Dept=models.CharField(max_length=15)
    Phonenumber=models.BigIntegerField()
    Age=models.IntegerField()

    def __str__(self):
        return self.Name
