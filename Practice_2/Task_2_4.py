#Дана строка words. Замените в этой строке все цифры 1 на слово one. Ответ в переменную result.

words = ("j3b6bk3jbvjk3kjvn6i i3oh4 ui1h1 1 h6j2j kh2j h46jh3jkjkd h5h 74jhk 2b1  1 1 15 16ljk h1lkh6j g12h5b2h 5121")
new_words = []
for i in words:
    if i == '1':
        new_words.append('one')
    else: new_words.append(i)
result = ''.join(myList)
print(result)