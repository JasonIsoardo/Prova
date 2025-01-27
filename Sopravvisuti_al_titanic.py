import csv
import matplotlib.pyplot as plt

# Inizializzare i contatori
male_survived = 0
male_died = 0
female_survived = 0
female_died = 0

# Leggere il file CSV
with open('titanic.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['Sex'] == 'male':
            if row['Survived'] == '1':
                male_survived += 1
            else:
                male_died += 1
        elif row['Sex'] == 'female':
            if row['Survived'] == '1':
                female_survived += 1
            else:
                female_died += 1

label = ['Maschi sopravvisuti', 'Maschi morti', 'Femmine morte', 'Femmine vive']
values = [male_survived, male_died, female_survived, female_died]

plt.bar(labels, values, color=['blue', 'blue', 'pink', 'pink'])
plt.title['Sopravvisuti e vittime del titan maschi e femmine']
plt.xlabel('Sesso')
plt.ylabel('Numero di Passeggeri')


plt.tight_layout()
plt.show()