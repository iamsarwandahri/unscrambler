from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=264, unique=True, db_index=True)
    sorted_word = models.CharField(max_length=264, db_index=True, default='')

    def __str__(self):
        return self.word
