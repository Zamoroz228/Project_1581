file = open('file.csv')
mass = file.readlines()
t = 0
m = []
for i in mass:
    if t == 0:
        i = i[3:len(i) - 1]
        t = 1
    else:
        i = i[:len(i) - 1]
    m.append(list(map(int, i.split(';'))))
t = 0
for i in m:
    x = max(i) + min(i)
    if len(i) == len(set(i)) and (x * 3 <= (sum(i) - x) * 2):
        t += 1
print(t)