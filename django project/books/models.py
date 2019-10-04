from django.db import models

class Book(models.Model):
    title = models.CharField(
        max_length = 100
    )
    author = models.CharField(
        max_length = 50
    )
    genre = models.CharField(
        max_length = 20
    )
    publishDate = models.DateField(

    )
    pages = models.IntegerField(

    )
    price = models.IntegerField(

    )

    def __str__(self):
        return "{}. {} | {} | {:,}".format(self.id, self.title, self.author, self.price)