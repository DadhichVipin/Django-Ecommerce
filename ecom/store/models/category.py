from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    # over rider str method for showing categroy name for admin
    def __str__(self) -> str:
        return self.name