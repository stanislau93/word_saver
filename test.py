# -*- encoding: utf-8 -*-
import os

from unittest import TestCase, main
from word_saver import WordSaver

class WordSaverTest(TestCase):
    saver = None
    filename = 'test.txt'

    def setUp(self):
        self.saver = WordSaver(self.filename)

    def tearDown(self):
        self.saver.close()
        os.remove(self.filename)

    def test_insertion_with_output(self):
        expected_output = '3 words written\nTotal words number is 3\n'
        self.assertEqual(self.saver.run_word_saver(words=['yksi', 'kaksi', 'kolme'], make_output=True), expected_output)

if __name__ == '__main__':
    main()