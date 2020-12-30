file = open("pi.txt")
str = ''
x =''
for i in range(0,150000):
    x= file.readline()
    if (x != '\n'):
        str+=x
print(str)
