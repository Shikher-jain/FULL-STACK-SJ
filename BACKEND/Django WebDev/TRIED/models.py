from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name
