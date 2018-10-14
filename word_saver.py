import os

class WordSaver(object):
	filename = ''
	file = None
	output = ''

	def __init__(self, filename):
		self.filename = filename
		self.file = self.get_file('a+', 'utf-8')

	def run_word_saver(self, words, make_output):
		self.output = ''

		if words is not None and len(words) > 0:
			self.add_word(words)

		if make_output == True:
			self.output_count()

		return self.output

	def add_word(self, words):
		feed = []

		for word in words:
			word = self.set_tremas_and_lower(word)
			if word != '' and not self.is_word_in_file(word):
				feed.append(word)

		if os.stat(self.filename).st_size > 0 and len(feed) > 0:
			self.file.write(',')

		self.file.write(','.join(feed))
		self.output += '%s words written\n' % (len(feed) if len(feed) > 0 else 'no')

	def output_count(self):
		words_number = len(self.get_file_content_delimited())
		self.output += 'Total words number is %d\n' % words_number

	def get_file(self, mode, encoding):
		try:
			return open(self.filename, mode, encoding=encoding)
		except:
			print("File %s does not exist or is corrupted" % self.filename)
			exit()

	def is_word_in_file(self, word):
		return word in self.get_file_content_delimited()

	def get_file_content_delimited(self, delimiter=','):
		self.file.seek(0)
		content = self.file.read()
		return [] if content == '' else list(filter(len, content.split(',')))

	def set_tremas_and_lower(self, word):
		return word.replace('a:','ä').replace('o:', 'ö').lower()

	def close(self):
		self.file.close()
