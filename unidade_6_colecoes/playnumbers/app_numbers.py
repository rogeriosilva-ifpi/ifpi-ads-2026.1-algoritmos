import os

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

    0 - Exit >>> '''

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1: # New
            number = int(input('New number: '))
            numbers.append(number)
            print('Success!')
        elif opcao == 2: # List
            print(f'> {len(numbers)} numbers in system.')
            for item in numbers:
                print(f'{item}', end=' ')
            print('\n---------------')
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
            print('Numbers replaced sucessfully!')
        elif opcao == 5: # Count
            number = int(input('Number: '))
            count = count_item(numbers, number)
            print(f'There are {count} "{number}"s')
        elif opcao == 6: # remove
            number = int(input('Number: '))
            while not contain(numbers, number):
                print('Number not found!')
                number = int(input('number: '))
            count = count_item(numbers, number)
            numbers = remove_item(numbers, number)
            print(f'> {count} numbers "{number}" removed!')



        input('Enter to continue...')
        clear_screen()
        opcao = int(input(menu))

    # save values
    save_numbers(numbers)


def clear_screen():
    os.system('clear')



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



main()