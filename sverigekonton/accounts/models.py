from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # You should hash and store passwords securely in practice

    def __str__(self):
        return self.email