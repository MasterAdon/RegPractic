from typing import Any

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

#pprint(contacts_list1)
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
#pprint(contacts_list2)



with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list2)