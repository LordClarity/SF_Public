def sort_list(lst):
    lst.sort()

def index_num():
    ind = 0
    for i in range(len(list_of_nums) - 1):
        if list_of_nums[i] < num < list_of_nums[i + 1]:
            ind = i
    print(f'Индекс числа {list_of_nums[ind]} равен {ind}')


try:
    list_of_nums = list(map(int, input("Введите последовательность чисел через пробел").split()))
    num = int(input("Введите любое число"))

    sort_list(list_of_nums)
    if num <= list_of_nums[0] or num >= list_of_nums[-1]:
        print("Не соблюдены условия")
    else:
        index_num()

except:
    print("Ошибка: ввод должен содержать только числа")
