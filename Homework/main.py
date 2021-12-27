from Homework_Files import get_indigrients, get_shop_list_by_dishes, two_by_one


if __name__ == '__main__':
    print(get_indigrients('recipes.txt'), '\n')
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), '\n')
    print(two_by_one('first.txt', 'second.txt'))
