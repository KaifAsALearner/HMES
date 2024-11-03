from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)
    # cost = models.DecimalField(max_digits=10, decimal_places=2)
    descript = models.TextField()
    def __str__(self):
        return self.name