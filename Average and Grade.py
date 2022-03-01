#Adnan Hoti
#CS-175L

def determine_score(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


def calc_average(grade1, grade2, grade3, grade4, grade5):
    return (grade1 + grade2 + grade3 + grade4 + grade5) / 5.0


def main():
    grade1 = int(input("Enter a score: "))
    print("Letter grade is " + determine_score(grade1))
    grade2 = int(input("Enter a score: "))
    print("Letter grade is " + determine_score(grade2))
    grade3 = int(input("Enter a score: "))
    print("Letter grade is " + determine_score(grade3))
    grade4 = int(input("Enter a score: "))
    print("Letter grade is " + determine_score(grade4))
    grade5 = int(input("Enter a score: "))
    print("Letter grade is " + determine_score(grade5))

    avg = calc_average(grade1, grade2, grade3, grade4, grade5)

    print("Average score is " + str(avg))
    print("Average grade is " + determine_score(avg))

def repeat():
    user_says=input('Would you like to continue?')
    if user_says == 'y':
        running = True
    else:
        running = False
    return running 

working = True    
while working:
    main()
    working = repeat()
