import re

number_words = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }


def extract(line: str) -> int:
  pattern = r'(?=([1-9]|{0}'.format('|'.join(number_words)) + '))'
  p = re.compile(pattern)

  first_num = p.findall(line)[0]
  second_num = p.findall(line)[-1]

  words = list()
  for word in first_num, second_num:
    if word in number_words.keys():
      words.append(str(number_words[word]))
      continue
    words.append(word)
  return int(''.join(words))

with open('puzzleinput.txt', 'r') as f:
  total = sum([extract(line) for line in f.readlines()])

print(total)