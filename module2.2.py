number = int(input( 'Пропиши число 1: '))
number_1 = int(input('Пропиши число 2: '))
number_2 = int(input('Пропиши число 3: '))
if number_2 == number_1 and number == number_1 and number_2 == number:
    print(3)

elif number_2 == number_1 or number == number_1 or number_2 == number:
    print(2)

else:
    print(0)
