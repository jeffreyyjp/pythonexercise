# encoding: UTF-8
n = int(raw_input("Please input the number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print '{0}×{1}={2:2d}'.format(j, i, j * i), 
    print '\n'