from django.db import models

# Create your models here.
class Writer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=30)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    founded = models.DateTimeField('foundation date')

    def __str__(self):
        return self.name


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('BK', 'Book'),
        ('PP', 'Paper'),
        ('WP', 'Web page'),
        ('LT', 'Letter'),
        ]

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    document_type = models.CharField(
        max_length=2,
        choices=DOCUMENT_TYPE_CHOICES,
        default='BK'
        )
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name