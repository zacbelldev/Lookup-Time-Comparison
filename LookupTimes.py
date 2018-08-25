import csv
import itertools
import time

start_time = time.time()

app_set = set(())
app_list = []
app_dictionary = {}

with open('AppleStore.csv') as csv_file:
    for row in itertools.islice(csv.DictReader(csv_file), 10000):
        app_set.add(row['track_name'])
        app_list.append(row['track_name'])
        app_dictionary[row['size_bytes']] = row['track_name']

# print("Set data: ", app_set)
# print("List data: ", app_list)
# print("Dictionary data: ", app_dictionary)
print("\nTime to initialize 10,000 rows into a set,list, and dictionary: {:.10f}s".format(time.time() - start_time))


# ASK FOR USER INPUT
n = str(input("\nEnter an App Name to search from the set, list, and dictionary: "))


# -----------------------SET LOOKUP----------------------------------
app_set_start_time = time.time()
if n in app_set:
    print("\nMatch found in set")
else:
    print("\nMatch not found in set")
set_time = time.time() - app_set_start_time


# -----------------------LIST LOOKUP---------------------------------
app_list_start_time = time.time()
if n in app_list:
    print("Match found in list")
else:
    print("Match not found in list")
list_time = time.time() - app_list_start_time


# -----------------------DICTIONARY LOOKUP---------------------------
app_dictionary_start_time = time.time()
if n in app_dictionary.values():
    print("Match found in dictionary")
else:
    print("Match not found in dictionary")
dict_time = time.time() - app_dictionary_start_time

print("\nSet lookup time: {:.10f}s".format(set_time))
print("List lookup time: {:.10f}s".format(list_time))
print("Dictionary lookup time: {:.10f}s".format(dict_time))

print("\nSLOWEST: {:.10f}s".format(max(set_time, list_time, dict_time)))
print("FASTEST: {:.10f}s".format(min(set_time, list_time, dict_time)))