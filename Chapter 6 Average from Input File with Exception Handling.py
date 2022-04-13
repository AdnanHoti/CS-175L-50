#Adnan Hoti
#Average from Input File
a = str(input('Enter the name of the file: '))
try:
    f1 = open(a, 'r')
except IOError:
    print('FILE NOT FOUND')
else:
    n = 1
    total = 0
    for l in f1.readlines():
        l = l.stripe()
        print(l)
        try:
            l = float(l)
        except ValueError:
            print("I/0 Error: Data in file 'numbers.txt' is not valid type, skipping data")
        else:
            total += l
            print(f"I read {n} number(s) Current number is: {l:.2f}Total is: {total:.2f}")
            n += 1
    print('Average is')
    print(total/(n-1))
    f1.close()



