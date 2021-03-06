from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
class Writer(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=30)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    foundation_date = models.DateField('foundation date', default='1990-1-1')

    def __str__(self):
        return self.name


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('BK', 'Book'),
        ('PP', 'Paper'),
        ('WP', 'Web page'),
        ('LT', 'Letter'),
        ]
    DOCUMENT_GENRE_CHOICES = [
        ('SC', 'Scientific'),
        ('SF', 'Science fiction'),
        ('RM', 'Romance'),
        ('TR', 'Thriller'),
        ('DR', 'Drama'),
        ('TG', 'Tragic'),
        ]
    class RATING(models.IntegerChoices):
        ZERO = 0, _(' ')
        ONE = 1, _('*')
        TWO = 2, _('**')
        THREE = 3, _('***')
        FOUR = 4, _('****')
        FIVE = 5, _('*****')

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    document_type = models.CharField(
        max_length=2,
        choices=DOCUMENT_TYPE_CHOICES,
        default='BK'
        )
    document_genre = models.CharField(
        max_length=2,
        choices=DOCUMENT_GENRE_CHOICES,
        default='SC'
        )
    pub_date = models.DateField('publication date', default='1991-1-1')
    rating = models.IntegerField(default=0, choices=RATING.choices)

    def __str__(self):
        return self.name