my_file = open("some.txt")
text = my_file.read()
my_file.close()
 
print("Было прочитано:")
print(text, '\n')
 
new_lst = []
letter = input('Введите букву: ').lower()
change = input('Введите символ: ')
print()
 
for word in text.split():
    if word.lower().startswith(letter):
      if not word[-1].isalpha():
        word = word[:-1]
      new_lst.append(word)
print(', '.join(new_lst))
 
for word in new_lst:
    word = change + word[1:]
    print(word, end=', ')
