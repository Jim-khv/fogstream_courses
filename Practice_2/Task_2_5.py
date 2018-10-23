#Дана строка words. Удалите каждый 3 символ из строки. Ответ в переменную result.

words = ("j3b6bk3jbvjk3kjvn6i i3oh4 ui1h1 1 h6j2j kh2j h46jh3jkjkd h5h 74jhk 2b1  1 1 15 16ljk h1lkh6j g12h5b2h 5121")
new_words = []
count = 0
for i in words:
    count += 1
    if count % 3 == 0: continue
    else: new_words.append(i)
result = ''.join(new_words)
print(result)