finalnumlist = []
total = 0

f = open("puzzleinput.txt", "r")

for line in f:
  first_num_found = False
  second_num_found = False
  while second_num_found == False:

    for char in line:
      if char.isdigit() and first_num_found == False:
        first_num = char
        first_num_found = True

      elif char.isdigit():
        second_num_found = True
        second_num = char
  num = first_num + second_num
  finalnumlist.append(int(num))

for i in finalnumlist:
  total += int(i)

print(total)
