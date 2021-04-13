import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
values.sort()
count=0
while True:
    for i in range(len(values)-1,-1,-1):
        if (values[i]%values[0]==0):
            values.pop(i)
    count+=1
    if len(values)==0:
        break
print(count)


