import time

a = list('hello world')
b = list(' abcdefghijkklmnopqrstuvwxyz')
c = ''
for i in a:
    for j in b:
        print(c + j)
        if i == j:
            c = c + j
            break
        time.sleep(0.2)
