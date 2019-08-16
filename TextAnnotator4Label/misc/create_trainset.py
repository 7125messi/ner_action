import csv
import os

filename = "41city_30000garden.csv"
required_column = ['a.name', 'a.alias_name', 'a.city', 'a.district', 'a.zone', 'a.address', 'a.address_point',
                   'a.name_point']
with open(filename, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    pure_filename = os.path.splitext(filename)[0]
    output_count = 0
    split_size = 1000
    for index, row in enumerate(reader):
        if index % split_size == 0:
            target_filename = pure_filename + '_{}.txt'.format(index)
            target_f = open(target_filename, 'x', encoding='utf-8')
            output_count += 1

        line = ''.join([row[c] for c in required_column])
        target_f.write(line + '\n')

        if index % split_size == split_size - 1:
            target_f.close()
