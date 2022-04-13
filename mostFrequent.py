#Adnan Hoti
#CS-175L-50
#mostFrequent

def main():
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    frequent = 0
    
    user_string = input('Enter string value:')
    
    for ah in user_string:
        ah = ah.upper()
        index = letters.find(ah)
        if index >= 0:
            count[index] = count[index] + 1
    for i in range(len(count)):
        if count[i] > count[frequent]:
            frequent = i
    print('The character that appears most frequently in the string is ', letters[frequent], '.', sep='')

main()
