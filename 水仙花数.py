# import sys 
# for line in sys.stdin:
#     a = line.split()
#     n=int(a[0])
#     m=int(a[1])
n=int(input())
m=int(input())
if not(n>=3 and n<=7):
    print(-1)
else:
    num=[]  #保存所有水仙花数
    exitnum=0
    for i in range(10**(n-1),10**n):
        sum=0   #数位的求和
        i2=i
        for j in range(n):
            sum=sum+(i2%10)**n
            i2=i2//10
        
        if (i==sum):
            num.append(i)
            if (len(num)==(m+1)):
                print(num[-1])
                exitnum=1
        
    if not exitnum:
        print(m*num[-1])
            
        
        