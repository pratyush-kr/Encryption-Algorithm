num = '123'
n = 0
def take_input():
    global num,n
    while(len(num) != 4):
        try:
            num = input('Enter a four(0,9999) digit number: ')
            n = int(num)
        except(ValueError):
            print('Enter only integers')
            num = '123'
            take_input()
take_input()
