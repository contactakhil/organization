from django.db import models

# Create your models here.
class Employees(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    salary_perhour = models.IntegerField(default=0)
    working_hours = models.IntegerField(default=0)
    total_salry = models.IntegerField(default=0)

    def __self__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total_salry = self.salary_perhour * self.working_hours * 30
        super(Employees, self).save(*args, **kwargs)