import csv
import itertools
import time

app_set = set(())
app_list = []
app_dictionary = {}

print("\n-----------------------------------------------------")
print("\033[94mCoding Challenge:\033[0m"
      "\nCompare lookup times for set, list, and dictionary ")
print("-----------------------------------------------------")

start_time = time.time()
with open('AppleStore.csv') as csv_file:
    for row in itertools.islice(csv.DictReader(csv_file), 11000):
        app_set.add(row['track_name'])
        app_list.append(row['track_name'])
        app_dictionary[row['size_bytes']] = row['track_name']

print("\nElapsed time to initialize structures "
      "\nwith 11,000 rows of data:"
      "\n\033[92m{:.10f}s\033[0m".format(time.time() - start_time))

print("\nSet data: ", app_set)
print("List data: ", app_list)
print("Dictionary data: ", app_dictionary)

# ASK FOR USER INPUT
n = str(input("\nSearch for an app by name: "))

# -----------------------SET LOOKUP----------------------------------
app_set_start_time = time.time()
if n in app_set:
    print("\nSet:                    \033[92mMatch found\033[0m")
else:
    print("\nSet:                    \033[92mMatch not found\033[0m")
set_time = time.time() - app_set_start_time

# -----------------------LIST LOOKUP---------------------------------
app_list_start_time = time.time()
if n in app_list:
    print("List:                   \033[92mMatch found\033[0m")
else:
    print("List:                   \033[92mMatch not found\033[0m")
list_time = time.time() - app_list_start_time

# -----------------------DICTIONARY LOOKUP---------------------------
app_dictionary_start_time = time.time()
if n in app_dictionary.values():
    print("Dictionary:             \033[92mMatch found\033[0m")
else:
    print("Dictionary:             \033[92mMatch not found\033[0m")
dict_time = time.time() - app_dictionary_start_time

# PRINT RESULTS
print("\nSet Lookup Time:        \033[92m{:.10f}s\033[0m".format(set_time))
print("List Lookup Time:       \033[92m{:.10f}s\033[0m".format(list_time))
print("Dictionary Lookup Time: \033[92m{:.10f}s\033[0m".format(dict_time))

print("\nSlowest Time:           \033[92m{:.10f}s\033[0m".format(max(set_time, list_time, dict_time)))
print("Fastest Time:           \033[92m{:.10f}s\033[0m".format(min(set_time, list_time, dict_time)))