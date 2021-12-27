cook_book = {}
def get_indigrients(file_name):
    with open(file_name) as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
            print(count)
            list_dish = []
            for indigrients in range(count):
                ingredient_name, quantity, measure = file.readline().split('|')
                sostav = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure[0:-1]}
                list_dish.append(sostav)
            cook_book[name] = list_dish
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shoplist = {}
    for dish in dishes:
        for ingredients in cook_book[dish]:
            shoplist.setdefault(ingredients['ingredient_name'], {'measure':ingredients['measure'], 'quantity':int(ingredients['quantity']) * person_count})
    return shoplist



def two_by_one(first_name, second_name):
    file1 = []
    file2 = []
    result = open('result.txt', 'w+')

    with open(first_name) as first_file:
        for line in first_file:
            file1.append(line)

    with open(second_name) as second_file:
        for line in second_file:
            file2.append(line)

    if len(file1) > len(file2):
        result.write(second_name + '\n' + str(len(file2)) + '\n')
        for i in range(len(file2)):
            result.write(file2[i])
        result.write('\n')

        result.write(first_name + '\n' + str(len(file1)) + '\n')
        for i in range(len(file1)):
            result.write(file1[i])
    result.close()

    return 'Done, checkout your file!'