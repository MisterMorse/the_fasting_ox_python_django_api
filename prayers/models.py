from django.db import models


class Prayer(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [ "category", "name" ]

    def __str__(self):
        return f"{ self.category } -> { self.name }"
