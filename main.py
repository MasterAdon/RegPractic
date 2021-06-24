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
for cl in contacts_list:
    cl1 = []
    for c in cl:
        result = re.match(pattern, c)
        if result is not None:
            if result.group(6) != "":
                result1 = re.sub(pattern, sub2, c)
                c = c.replace(c, result1)
            else:
                result2 = re.sub(pattern, sub1, c)
                c = c.replace(c, result2)
        else:
            pass
        cl1.append(c)
    contacts_list1.append(cl1)

# pprint(contacts_list1)
# Форматируем ФИО в соответствии с заданием
contacts_list2 = []
for cl in contacts_list1:
    s = cl[3:7]
    f = cl[0:3]
    fr = [','.join(f)]
    cl1 = []
    for fra in fr:
        fra = fra.replace(',', ' ').split()
        if len(fra) < 3:
            fra.append('')
        #print(fra)
        cl1 = fra + s
    contacts_list2.append(cl1)
#pprint(contacts_list2)



with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list2)