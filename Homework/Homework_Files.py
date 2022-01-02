import glob, os
cook_book = {}
def get_indigrients(file_name):
    with open(file_name) as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
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
            if ingredients['ingredient_name'] in list(shoplist.keys()):
                shoplist[ingredients['ingredient_name']].update(quantity = int(shoplist[ingredients['ingredient_name']]['quantity']) + int(ingredients['quantity']) * person_count)
            else:
                shoplist.setdefault(ingredients['ingredient_name'], {'measure': ingredients['measure'],'quantity': int(ingredients['quantity']) * person_count})
    return shoplist



def files_to_file(directory):

    file_dict = {}
    sort_dict = {}
    # создаем неотсортированный словарь
    file_list = os.chdir(directory)
    if 'result.txt' in os.listdir():
        os.remove('result.txt')
    for file in glob.glob("*.txt"):
        mass_of_lines = []
        with open(file) as file2read:
            for line in file2read:
                mass_of_lines.append(line)
        file_dict.setdefault(file, [mass_of_lines, len(mass_of_lines)])
    # сортируем
    counter = 0
    while True:
        counter += 1
        for value in file_dict:
            if file_dict[value][1] == counter:
                sort_dict.setdefault(value, file_dict[value])
        if len(sort_dict) == len(file_dict):
            break
    #  записываем в итоговый файл
    result = open('result.txt', 'w+')
    for key in sort_dict:
        result.write(key + '\n' + str(sort_dict[key][1]) + '\n')
        for i in range(len(sort_dict[key][0])):
            result.write(sort_dict[key][0][i])
        result.write('\n')
    return 'Done, checkout your file!'

