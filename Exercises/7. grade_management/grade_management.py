grades = []
new_grade = 0
avg = 0
while True:
    answer = input('\n\nDo you want do add new grade?  [yes] [no]\n')
    
    if answer.lower() == 'yes':
        new_grade = float(input('\nWhat grade would you like to add?'))
        grades.append(new_grade)
    elif answer.lower() == 'no':
        break

aryth_grades = input('All grades have been added, would you like to see arythmetic average of the grades?    [yes][no]\n')

if aryth_grades.lower() == 'yes':
    for x in grades:
        avg = avg+x
    avg = avg/len(grades)
    print(f'Average grade is: {round(avg, 1)}')

if avg >= 3.5:
    print('\nZaliczyles przedmiot!')
    print('You passed the class!')
else:
    print('\nNie zaliczyles przedmiotu.')
    print('You failed the class.')
    
full_grades = input('Would you like to see all the grades?  [yes][no]\n')

if full_grades.lower() == 'yes':
    print(grades)
