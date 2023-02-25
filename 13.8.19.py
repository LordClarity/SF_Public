summary = 0
tickets = int(input("Сколько билетов вы хотите приобрести?"))
for i in range(1,tickets+1):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
        s = 0
    elif 18 <= age < 25:
        s = 990
    elif age >= 25:
        s = 1390
    summary = summary + s
if tickets > 3:
    summary = int(summary * 0.9)
print ("Сумма к оплате:",summary)
