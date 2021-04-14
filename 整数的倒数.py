num=input()
if num[0]=='-':
    print(num[0]+num[:0:-1])
else:
    print(num[::-1])