import codecs
import re

filesnames = codecs.open('filesnames.txt', 'r', 'utf_8')
all_text_file = codecs.open('all_text.txt', 'w', 'utf_8')
freq_file = codecs.open('freq_list.txt', 'w', 'utf_8')
all_files = filesnames.readlines()
all_texts = ''

for filename in all_files:
    f_name = filename.strip() + '.txt'
    file_contents = codecs.open(f_name, 'r', 'utf_8').read()
    just_ar_content = re.sub(r'[a-zA-Z0-9|,|.|:|\|/|"|،|\'|-|!|*|%|(|)|?|=|؟g]', '', file_contents)  # noqa
    all_texts += just_ar_content
    filesnames.close()

all_text_file.write(all_texts)
all_text_file.close()

all_words = re.findall(r'[\u0600-\u06FF]+', all_texts)
all_words_unique = set(all_words)
final_list = []

for word in all_words_unique:
    words_count = all_words.count(word)
    final_list.append([words_count, word])

final_list = sorted(final_list)

for element in final_list:
    freq_file.write(str(element[1]) + ' : ' + str(element[0]) + '\n')

freq_file.close()
print("Finished, data saved into the files !")
