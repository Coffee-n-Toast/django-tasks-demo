from django.db import models


# Create your models here.
class Month(models.Model):
    name = models.CharField(max_length=50, blank=False)
    number = models.PositiveSmallIntegerField(unique=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Month'
        ordering = ['order']

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=(
        ('pending', 'Pending'), ('in-progress', 'In-progress'), ('complete', 'Complete')
    ), default='pending')
    month = models.ForeignKey(Month, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Task'

    def __str__(self):
        return f'{self.name}'
