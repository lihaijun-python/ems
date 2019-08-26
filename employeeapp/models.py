from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    age=models.SmallIntegerField()
    birthday = models.DateField()
    headpic= models.ImageField(upload_to="pics")

    class Meta:
        db_table='my_employee'