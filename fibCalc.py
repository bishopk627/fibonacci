print('Fibonacci Calculator')
print('--------------------')
iterations = int(input('How many iterations? '))
i = 1
a=0
b=1
c=0
while i < iterations:
    i+=1
    fileName = str(i)+'.txt'
    file = open(fileName,'w')
    c=a+b
    a=b
    b=c
    print("{:,}".format(c),file=file)
    print(c)
    file.close()
print('Done!')
input()
