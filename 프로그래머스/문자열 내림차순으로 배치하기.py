a = 'He11oWor1d'
b = 'lloWorl'
n = 2

aa = []
aa.append(a[:2])
aa.append(a[2:len(b)+2])
aa.append(a[len(b)+2:])

aa[1] = b
print(aa)
print(aa[0] + aa[1] + aa[2])