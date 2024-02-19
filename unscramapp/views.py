from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Word
from itertools import combinations, product
import re


def has_valid_characters(input_string):
    regex = re.compile(r'^[a-zA-Z0-9?]+$')

    return bool(regex.match(input_string))


def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            scrambled_word = data.get('input').lower()
            wild_count = scrambled_word.count('?')

            if has_digit(scrambled_word):
                mydict = {'list': 'Please enter a unscrambled word'}

            elif wild_count > 3:
                mydict = {'list': 'Please enter a unscrambled word with less than 4 wiled characters'}

            elif not has_valid_characters(scrambled_word):
                mydict = {'list': 'Please enter a valid word'}

            else:
                valid_words = unscramble_words(scrambled_word)

                lengths = [num for num in range(len(scrambled_word), 0, -1)]

                words_list = [[item for item in valid_words if len(item) == length] for length in lengths]

                mydict = {'list': words_list}
            return JsonResponse(mydict)

        except Exception as e:
            print(e)
            return JsonResponse("ERROR", safe=False)


def has_digit(word):
    return any(char.isdigit() for char in word)


def unscramble_words(scrambled_word):
    wild_count = scrambled_word.count('?')

    possible_words = []
    if('?' in list(scrambled_word)):
        wild_count = min(3, wild_count)

        for wild_chars in product('abcdefghijklmnopqrstuvwxyz', repeat=wild_count):

            temp_word = list(scrambled_word)

            for char in wild_chars:
                temp_word[temp_word.index('?')] = char

            possible_word = ''.join(temp_word)

            possible_words.append(possible_word)

    else:
        for length in range(1, len(scrambled_word)+1):
            possible_words.extend([(''.join(sorted(t))) for t in combinations(scrambled_word, length)])

    valid_words = list(Word.objects.filter(sorted_word__in=possible_words).values_list('word', flat=True))

    return valid_words
