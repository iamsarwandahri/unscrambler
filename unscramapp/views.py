from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Word
from itertools import combinations, product
from django.db.models import Q
from django.test import TestCase

def index(request):
    return render(request, 'index.html')


def search(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            scrambled_word = data.get('input').lower()

            print('Text', scrambled_word)
            valid_words = unscramble_words(scrambled_word)

            lengths = [num for num in range(len(scrambled_word), 0, -1)]

            words_list = [[item for item in valid_words if len(item) == length] for length in lengths]

            mydict = {'list': words_list}
            return JsonResponse(mydict)

        except Exception as e:
            print(e)
            return JsonResponse("ERROR", safe=False)


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

    valid_words = list(Word.objects.filter(Q(sorted_word__in=possible_words)).values_list('word', flat=True))

    return valid_words

class UnscrambleWordsTestCase(TestCase):
    def setUp(self):
        # Create some Word objects in the database for testing
        Word.objects.create(word="cat", sorted_word="act")
        Word.objects.create(word="dog", sorted_word="dgo")
        Word.objects.create(word="tac", sorted_word="act")

    def test_unscramble_words_with_wildcards(self):
        # Test unscrambling words with wildcard characters
        result = unscramble_words("c?t")
        self.assertEqual(result, ["act", "cat"])

    def test_unscramble_words_without_wildcards(self):
        # Test unscrambling words without wildcard characters
        result = unscramble_words("god")
        self.assertEqual(result, ["dog"])

    def test_unscramble_words_with_duplicate_letters(self):
        # Test unscrambling words with duplicate letters
        result = unscramble_words("tac")
        self.assertEqual(result, ["act", "cat"])

    def test_unscramble_words_empty_input(self):
        # Test unscrambling empty input
        result = unscramble_words("")
        self.assertEqual(result, [])

    def test_unscramble_words_no_matching_words(self):
        # Test unscrambling with no matching words found
        result = unscramble_words("xyz")
        self.assertEqual(result, [])

    def tearDown(self):
        # Clean up Word objects created for testing
        Word.objects.all().delete()