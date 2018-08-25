# import csv
# reader = csv.reader(open('AppleStore.csv', 'r'))
#
# d = {}
# for row in reader:
#     id, track_name = row[1], row[2]
#     d[id] = track_name
#     print(d)

# for i in d:
#     print(i, d[i])

import csv
import itertools

with open('AppleStore.csv') as csvfile:
    for row in itertools.islice(csv.DictReader(csvfile), 10):
        print(row['id'], row['track_name'])