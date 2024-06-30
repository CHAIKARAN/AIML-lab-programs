import csv

with open("trainingexamples.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

specific = data[1][:-1]
general = [['?' for i in range(len(specific))] for j in range(len(specific))]

for i in data[1:]:  # Skip header row
    if i[-1] == "Yes":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                specific[j] = "?"
                general[j][j] = "?"

    elif i[-1] == "No":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = "?"

    print("\nStep " + str(data.index(i)) + " of Candidate Elimination Algorithm")
    print(specific)
    print(general)

gh = [i for i in general if any(j != '?' for j in i)]

print("\nFinal Specific hypothesis:\n", specific)
print("\nFinal General hypothesis:\n", gh)
