from django.test import TestCase
from .models import Word
from .views import unscramble_words


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
