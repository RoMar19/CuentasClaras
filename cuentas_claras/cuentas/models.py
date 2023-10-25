from django.db import models

class Cuenta(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  amount = models.DecimalField(max_digits=4, decimal_places=2, null=True)
  date = models.DateField(null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"