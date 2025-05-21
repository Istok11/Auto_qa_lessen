data1 = []
data2 = []

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(str(data2).replace(' ', '').replace('doc', '').replace('.', '').lower())

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 = str(data1).replace(' ', '').lower()

assert data1 == data2