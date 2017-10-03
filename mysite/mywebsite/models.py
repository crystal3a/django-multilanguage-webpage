from django.db import models


class Order(models.Model):
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.model
