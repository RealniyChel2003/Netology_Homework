from Homework_Files import get_indigrients, get_shop_list_by_dishes, files_to_file


if __name__ == '__main__':
    print(get_indigrients('recipes.txt'), '\n')
    print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2), '\n')
    print(files_to_file('Files'))

