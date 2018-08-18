from django.db import models
from django.utils import timezone

class Expense(models.Model):
   # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    date = models.DateTimeField(
            default=timezone.now)
    sum = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    #published_date = models.DateTimeField(
    #blank=True, null=True)

    def create(self):
        self.save()

    def __str__(self):
        return self.title

class Note(models.Model):
    expense = models.ForeignKey('Expense', on_delete=models.CASCADE)
    note = models.TextField(max_length=200, blank=False)
    date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.note