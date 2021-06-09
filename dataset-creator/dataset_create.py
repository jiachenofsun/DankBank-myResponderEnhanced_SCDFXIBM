import csv
import json
import random

with open("database.json") as file:
    dict = json.load(file)

# print(dict)

conditions_list = []
for conditions in dict:
    conditions_list.append(conditions)
# print(conditions_list)

fields = ["id", "Condition", "Symptom 1", "Symptom 2",
"Symptom 3", "Symptom 4"]

# empty_list = []
# field_sample = random.sample(fields, 2)
# for item in field_sample:
#     empty_list.append(item)
# print(empty_list)

dataset = []
id = 0
def create_entry():
    start_list = []

    start_list.append(id)

    condition = random.choice(conditions_list)
    start_list.append(condition)

    num_of_symptoms = random.randint(1, len(dict[condition]["Symptoms"]))
    for item in random.sample(dict[condition]["Symptoms"], num_of_symptoms):
        start_list.append(item)
    
    num_of_blanks = 4 - num_of_symptoms
    for i in range(num_of_blanks):
        start_list.append("")

    dataset.append(start_list)

for i in range(1000):
    create_entry()
    id += 1

# print(dataset)

with open("dataset.csv", "w") as file:
    write = csv.writer(file)

    write.writerow(fields)
    write.writerows(dataset)



