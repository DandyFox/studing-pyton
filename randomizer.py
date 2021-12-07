from random import randint
from collections import Counter

n = int(input("Количество сгенерированных чисел: "))
max = int(input("Максимальное число: "))
min = int(input("Минимальное число: "))

i = 0
gen_numbers = []

while n > i:
    number = randint(min, max)
    gen_numbers.append(number)
    i += 1

count = Counter(gen_numbers)
result = count.most_common()[0]
print("Число",result[0],"было сгенерировано",result[0],"раз(а). Это является максимальным показателем")


exit = input("Чтобы выйти нажмите Enter:")

