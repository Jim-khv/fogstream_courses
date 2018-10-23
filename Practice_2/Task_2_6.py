#Вам задана строка words, состоящая из пробелов и латинских букв.
#Строка называется панграммой, если она содержит каждую из 26 латинских букв хотя бы раз.
#Определите является ли строка панграммой. В единственной строке входных данных записана строка.
#Строка может содержать только пробелы, заглавные и строчные буквы латинского алфавита.
#Заглавные и строчные буквы считаются одинаковыми. Ответ в переменную result True или False.

words = ("bkJBmn bn bnm gbmn g bmJHbgjsqwersadgfsdfm j nBh b b  hzfgasdgfgx bcbmluoou ipyu iyu og h fhdgsh  ewrt bhjb jGv h xgfx gf xgvh")
words = words.lower()
words_1 = []
for i in words:
    if i != " ": words_1.append(i)
    else: continue
words_2 = list(set(words))
words_2.sort()
if len(words_2) >= 26: result = True
else: False
print(result)