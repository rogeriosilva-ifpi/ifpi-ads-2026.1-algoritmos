import os
import math

def main():
    clear_screen()
    # colecao de dados
    numbers = load_numbers()

    menu = '''
    **** Play Numbers ****
    1 - New Number
    2 - List Numbers
    3 - Number existence
    4 - Replace number
    5 - Count number
    6 - Remove number
    7 - Even numbers (filter)
    8 - Prime numbers (filter)
    9 - Negative numbers (filter)
    10 - Odd numbers (filter)
    11 - Powered by 2 (map)
    12 - Halfred (map)
    13 - Half of Even numbers (filter/map)
    14 - Sum of All (reduce)
    15 - Sum of Odd numbers (filter/reduce)
    16 - Sum of Double of Even numbers (map/filter/reduce)
    17 - The largest odd number (filter/reduce)
    18 - The largest number of all (reduce)

    0 - Exit >>> '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1: # New
            number = int(input('New number: '))
            numbers.append(number)
            success()
        elif opcao == 2: # List
            list_numbers(numbers)
        elif opcao == 3: # existence
            number = int(input('Number: '))
            exist = contain(numbers, number)
            result = 'Yes' if exist else 'No'
            print(f'Exist: {result}')
        elif opcao == 4: # update -> replace
            old_number = int(input('Actual number: '))
            while not contain(numbers, old_number):
                print('Number not found!')
                old_number = int(input('Actual number: '))
            
            new_number = int(input('New number: '))
            replace(numbers, old_number, new_number)
            success()
        elif opcao == 5: # Count
            number = int(input('Number: '))
            count = count_item(numbers, number)
            print(f'There are {count} "{number}"s')
            success()
        elif opcao == 6: # remove
            number = int(input('Number: '))
            while not contain(numbers, number):
                print('Number not found!')
                number = int(input('number: '))
            count = count_item(numbers, number)
            numbers = remove_item(numbers, number)
            print(f'> {count} numbers "{number}" removed!')
            success()
        elif opcao == 7:
            even_numbers = filter(numbers, is_even)
            list_numbers(even_numbers)
            success()
        elif opcao == 8:
            prime_numbers = filter(numbers, is_prime)
            list_numbers(prime_numbers)
            success()
        elif opcao == 9:
            # negative_numbers = filter(numbers, is_negative)
            negative_numbers = filter(numbers, lambda n:n < 0)
            list_numbers(negative_numbers)
            success()
        elif opcao == 10:
            list_numbers(filter(numbers, is_odd))
            success()
        elif opcao == 11:
            # powered = powered_by_2(numbers)
            # list_numbers(map(numbers, pow_by_2))
            list_numbers(map(numbers, lambda r:r**2))
            success()
        elif opcao == 12:
            # halfereds = halfered(numbers)
            list_numbers(map(numbers, half_value))
            success()
        elif opcao == 13:
            list_numbers(map(filter(numbers, is_even), half_value))
            success()
        elif opcao == 14:
            sum_of_all = reduce_sum(numbers)
            print(f'Sum of all numbers --> {sum_of_all}')
        elif opcao == 15:
            result = reduce_sum(filter(numbers, is_odd))
            print(f'Sum of all odd numbers --> {result}')
        elif opcao == 16:
            # result = reduce_sum(map(filter(numbers, is_even), double_value))

            result = reduce(map(filter(numbers, is_even), lambda x:x*2), lambda acc, actual: acc + actual, 0)

            print(f'Sum of double of even numbers --> {result}')
        elif opcao == 17:
            result = reduce_largest(filter(numbers, is_odd))
            print(f'The largest odd number is {result}')
        elif opcao == 18:
            # result = reduce(numbers, largest, numbers[0])
            result = reduce(numbers, lambda acc, actual: actual if actual >= acc else acc, numbers[0])

            print(f'The largest number is {result}')


        input('Enter to continue...')
        clear_screen()
        opcao = int(input(menu))

    # save values
    save_numbers(numbers)


def largest(value1, value2):
    if value1 >= value2:
        return value1
    else:
        return value2

def clear_screen():
    os.system('clear')


def success():
    print('Success!')


def contain(collection, element):
    for item in collection:
        if item == element:
            return True
    return False


def replace(collection, old_value, new_value):
    for i in range(len(collection)):
        item = collection[i]
        if item == old_value:
            collection[i] = new_value


def count_item(collection, element):
    count = 0
    for item in collection:
        if item == element:
            count += 1
    return count


def remove_item(collection, element):
    new_collection = []

    for item in collection:
        if item != element:
            new_collection.append(item)
    
    return new_collection


def list_numbers(numbers):
    print(f'> {len(numbers)} numbers:')
    for item in numbers:
        print(f'{item}', end=' ')
    print('\n---------------')


def load_numbers():
    collection = []
    file = open('numbers.txt')
    
    for line in file:
        number = line.strip()
        collection.append(int(number))

    file.close()

    return collection


def save_numbers(numbers):
    lines = []
    for number in numbers:
        lines.append(str(number)+'\n')
    
    file = open('numbers.txt', 'w')
    file.writelines(lines)
    file.close()
    print('Chiao!')


# Criterion Functions
def is_even(number):
    return number % 2 == 0

def pow_by_2(number):
    return number**2


def is_odd(number):
    return not is_even(number)


def is_negative(number):
    return number < 0


def is_prime(number):
    if number <= 1:
        return False
    
    for n in range(2, int(math.sqrt(number))+1):
        if number % n == 0:
            return False
    
    return True


# Filters
def filter(collection, fn_criterion):
    filtereds = []
    for item in collection:
        if fn_criterion(item):
            filtereds.append(item)
    
    return filtereds

# Tranform function
def half_value(value):
    return value/2


def double_value(value):
    return value*2

# Maps
def map(collection, fn_transformation):
    new_collection = []
    for item in collection:
        new_item = fn_transformation(item)
        new_collection.append(new_item)

    return new_collection


def powered_by_2(numbers):
    new_list = []
    for number in numbers:
        new_number = number**2
        new_list.append(new_number)

    return new_list


def halfered(numbers):
    new_list = []
    for number in numbers:
        new_number = number/2
        new_list.append(new_number)

    return new_list


# Reduce
def reduce(collection, operation, initial_value):
    acc = initial_value

    for actual in collection:
        acc = operation(acc, actual)

    return acc


def reduce_sum(numbers):
    sum_all = 0
    for number in numbers:
        sum_all = sum_all + number
    
    return sum_all


def reduce_largest(numbers):
    largest = numbers[0]

    for item in numbers:
        if item > largest:
            largest = item
    
    return largest












main()