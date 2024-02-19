import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unscrambler.settings")

import django
django.setup()

from unscramapp.models import Word


if __name__ == '__main__':
    Word.objects.all().delete()
    with open('static/sowpods.txt', 'r') as file:
        words_to_create = [Word(word=line.strip(), sorted_word=''.join(sorted(line.strip()))) for line in file]
        Word.objects.bulk_create(words_to_create)
