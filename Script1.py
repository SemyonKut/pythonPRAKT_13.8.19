try:
    tickets = int(input('Введите сколько билетов вы хотите приобрести на мероприятие '
                        '(больше 3-х человек - скидка 10%):\n'))
except ValueError:
    print('Неверный формат количества билетов (необходимо вводить с помощью целых чисел)'); tickets = 0
if tickets > 3:
    skidka = 10
else:
    skidka = 0
summa = 0
print("Количество билетов:", tickets)
print('-' * 75)

try:
    for i in range(1, tickets + 1):
        print('Билет №', i)
        age = int(input(f'Введите возраст посетителя для билета {i}: '))
        if 18 <= age <= 25:
            print(f'Возраст посетителя {i} = {age}, стоимость билета = 990 руб.\n')
            summa = summa + 990
        if 25 < age < 115:
            print(f'Возраст посетителя {i} = {age}, стоимость билета (полная) = 1390 руб.\n')
            summa = summa + 1390
        if 0 < age < 18:
            print(f'Возраст посетителя {i} = {age}, стоимость билета (бесплатно) = 0 руб.\n')
            summa = summa + 0
        if age <= 0 or age >= 115:
            print(f'Невозможный возраст посетителя, начните ввод сначала {i} = {age}\n')
            exit()
except ValueError:
    print('Неверный формат возраста (необходимо вводить с помощью целых чисел)')

print('-' * 75)
print('-' * 75)
print(f"Ваша скидка: {summa * skidka / 100} руб.({skidka}%)")
print(f'Cумма к оплате:{summa - summa * skidka / 100} руб.')