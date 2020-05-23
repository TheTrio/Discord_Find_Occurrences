import json
import matplotlib.pyplot as plt

find = input("Enter what to look for: ")
find = find.lower()
with open('Export.json') as f:
	data = json.load(f)

count = {}
for message in data['messages']:
	if find in message['content'].lower():
		if message['author']['name'] in count:
			count[message['author']['name']] = count[message['author']['name']] + 1
		else:
			count[message['author']['name']] = 1

with open('Data.txt','w',encoding="utf-8") as f:
	for k,v in count.items():
		f.write(k + "-" + str(v) + "\n")

name = []
count = []
with open('Data.txt') as f:
	for line in f:
		name.append(line.split("-")[0])
		count.append(int(line.split("-")[1]))

for i in range(len(name)):
	m = i
	for j in range(i+1,len(name)):
		if count[j] < count[m]:
			m = j
	count[i], count[m] = count[m], count[i]
	name[i], name[m] = name[m], name[i]

with open('Data.txt', 'w') as f:
	for i in range(len(name)):
		f.write(name[i] + "-" + str(count[i]) + "\n")
plt.style.use('fivethirtyeight')
plt.barh(name, count)
plt.xlabel('Count')
plt.ylabel('Username')
plt.title("Usage of the word " + find)
plt.tight_layout()
plt.show()
