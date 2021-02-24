import os


def words_only(text):
    alpha = ' abcdefghijklmnqoprstuvwxyz'
    text = text.lower()
    for char in text:
        if char == '\n':
            text = text.replace(char, ' ')
        if char not in alpha:
            text = text.replace(char, '')
    return text


poet = input('Input lastname of poet you want to analise (Shakespeare, Byron, Poe, Kipling or Wilde available):')
with open(os.path.join('Poets Database', poet + '.txt'), 'r', encoding='utf8') as poetFile:
    poetBio = poetFile.read()
print()

words_dict = {}
longest_word = ''
for word in words_only(poetBio).split():
    if len(word) > len(longest_word):       # Finding the longest word.
        longest_word = word
    if len(word) <= 3:                      # Don't look at too small words
        continue
    elif word in words_dict:                # Every other words count and write down in words dictionary
        words_dict[word] += 1
    else:
        words_dict[word] = 1

max_counted = []                # Here will be our most common words
for counted_word in words_dict:
    if len(max_counted) <= 1:               # We need only 2 of them
        max_counted.append(counted_word)
    else:
        if words_dict[counted_word] > words_dict[max_counted[0]]:
            max_counted.pop(0)
            max_counted.append(counted_word)
        elif words_dict[counted_word] > words_dict[max_counted[1]]:
            max_counted.pop(1)
            max_counted.append(counted_word)

print(f"The longest word - '{longest_word}'.\nTwo most common words are:\n"
      f"'{max_counted[0]}' - {words_dict[max_counted[0]]} times\n"
      f"'{max_counted[1]}' - {words_dict[max_counted[1]]} times.")