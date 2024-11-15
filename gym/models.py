from django.db import models
from django.contrib.auth.models import User

class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_months = models.IntegerField()  # Duration in months
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    user = models.TextField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    plan = models.TextField(default='null')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.user.username

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.member.user.username} - {self.date}"

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    receipt_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.member.user.username} - {self.amount} - {self.date}"
