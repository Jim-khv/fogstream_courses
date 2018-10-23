#Дана строка words. Если в этой строке буква f встречается только один раз, то в переменную result её индекс.
#Если она встречается два и более раз, то сумму индексов её первого и последнего появления в переменную result.
#Если буква f в данной строке не встречается, вывести -1 в result.

words = ("a f c d f f f n o p")
list = []
count = 0
for i in words:
    if i == 'f':
        list.append(count)
    count += 1
if len(list) == 0: result = -1
elif len(list) == 1: result = list[0]
else: result = list[0] + list[-1]
print(result)