import argparse
import sys

from word_saver import WordSaver

parser = argparse.ArgumentParser(description="Add a word or see the total words number")
parser.add_argument('-a', '--add', type=str, nargs='+', help='provide new word for insertion')
parser.add_argument('-c', '--count', action='store_true', help='show number of words in the file')
parser.add_argument('-f', '--file', type=str, help='name of the file where the words will be stored', default='words.txt')
args = parser.parse_args()

if len(sys.argv) == 1:
	exit('no arguments provided')

words_arg = args.add
output_count_arg = args.count
filename = args.file

saver = WordSaver(filename)

output = saver.run_word_saver(words_arg, output_count_arg)
sys.stdout.write(output)

saver.close()