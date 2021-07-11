file_name = input('Enter file name: ')
fhand = open(file_name, 'r')


word_count = 0
sentence_count = 0
for line in fhand:
    sentence_count += line.count('.') + line.count('?') + line.count('!')

    words = line.split()
    word_count += len(words)

print('Sentence Count:', sentence_count)
print('Word Count:', word_count)
