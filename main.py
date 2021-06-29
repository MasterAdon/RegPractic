from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# Форматируем номера телефонов в соответствии с форматом из задания.
contacts_list1 = []
pattern = r"(8|\+7)\s*\(?(\d{3})[-\)\s]?\s*(\d{3})-?(\d{2})-?(\d+)\s?[\s\(]?\w*\.*\s*(\d*)\)*"
sub1 = r"+7(\2)\3-\4-\5"
sub2 = r"+7(\2)\3-\4-\5 доб.\6"
for contact_list in contacts_list:
    contact_list1 = []
    for contact in contact_list:
        result = re.match(pattern, contact)
        if result is not None:
            if result.group(6) != "":
                result1 = re.sub(pattern, sub2, contact)
                contact = contact.replace(contact, result1)
            else:
                result2 = re.sub(pattern, sub1, contact)
                contact = contact.replace(contact, result2)
        else:
            pass
        contact_list1.append(contact)
    contacts_list1.append(contact_list1)

# pprint(contacts_list1)
# Форматируем ФИО в соответствии с заданием
contacts_list2 = []
for contact_list in contacts_list1:
    second_part = contact_list[3:7]
    first_part = contact_list[0:3]
    first_part = [','.join(first_part)]
    for first_part_str in first_part:
        first_part_list = first_part_str.replace(',', ' ').split()
        if len(first_part_list) < 3:
            first_part_list.append('')
        contact_list1 = first_part_list + second_part
    contacts_list2.append(contact_list1)
# pprint(contacts_list2)

# Форматируем данные удаляя дублируещие записи по фамилии, имени, с сохранением данных.
contacts_list3 = []
contact_dict = {}  # Временная переменная
for contact_list in contacts_list2:  # Создаем временный словарь
    contact_dict_key = tuple(contact_list[0:2])
    dict_contact = {contact_dict_key: contact_list[2:7]}
    for contact_key, contact_value in dict_contact.items():  # Создаем временную переменную
        contact_dict.setdefault(contact_key, []).append(contact_value)

for contact_key1, contact_value1 in contact_dict.items():  # Обьединяем элементы словаря и создаем конечный список
    if len(contact_value1) > 1:
        if contact_value1[0][2] == '':
            contact_value1[0][2] = contact_value1[1][2]
            if contact_value1[0][4] == '':
                contact_value1[0][4] = contact_value1[1][4]
        del contact_value1[1]
# pprint(contact_dict)  # Проверка сортировки и обработки
    first_part = list(contact_key1)
    for second_part in contact_value1:
        contact_list = first_part + second_part
        contacts_list3.append(contact_list)
# pprint(contacts_list3)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list3)
