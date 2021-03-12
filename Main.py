import json
import matplotlib.pyplot as plt
from collections import defaultdict
find = input("Enter what to look for: ")
find = find.lower()

with open('batch2024.json',encoding="utf-8") as f:
	data = json.load(f)

d = defaultdict(int)
for message in data['messages']:
	if find in message['content'].lower():
		d[message['author']['name']]+=1

with open('Data.txt','w',encoding="utf-8") as f:
	for k,v in d.items():
		f.write(k + "-" + str(v) + "\n")

name = []
count = []
with open('Data.txt',encoding="utf-8") as f:
	for line in f:
		name.append(line.split("-")[0])
		count.append(int(line.split("-")[1]))

count,name = (list(t) for t in zip(*sorted(zip(count, name))))

name,count = name[-10:], count[-10:]
plt.style.use('fivethirtyeight')
plt.barh(name, count)
plt.xlabel('Count')
plt.ylabel('Username')
plt.title(f'Word count - {find}')
plt.tight_layout()
plt.show()
