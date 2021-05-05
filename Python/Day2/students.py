numberOfStudents = input('How many students do you have?')

def is_int(input_string):
    intCheck = True
    while intCheck == True:
        if input_string.isnumeric():
            intCheck = False
            return int(input_string)
        else: 
            input_string = input('Please enter a valid number.')

numberOfStudents = is_int(numberOfStudents)

subjects = {'1' : 'Math', '2': 'science', '3': 'History'}

studentNames = [{}]

for x in range(numberOfStudents):
    
    if len(studentNames) < x + 1:
        studentNames.append({})
    
    studentNames[x]['name'] = (input('What is your student\'s name?'))
    alphaCheck = True
    while alphaCheck == True:
        if studentNames[x]['name'].isalpha():
            alphaCheck = False
            break
        else: 
            studentNames[x]['name'] = (input('Please enter a valid name'))
    
    studentNames[x]['grade'] = input('Student\'s Grade')
    studentNames[x]['grade'] = is_int(studentNames[x]['grade'])

    studentNames[x]['Course'] = input('Select a course: 1 - Math, 2 - Science, 3 - History')
    choiceCheck = True
    while choiceCheck == True:
        for subject in subjects:
            if studentNames[x]['Course'] == subject:
                studentNames[x]['Course'] = subjects[subject]
                choiceCheck = False
                break
        else:
            studentNames[x]['Course'] = input('Invalid choice: Please select a course: 1 - Math, 2 - Science, 3 - History')
    

def printInfo(some_dict):
    for entry in some_dict:
        student_info = ""
        for stuff in entry:
            student_info += f"{stuff}: {entry[stuff]}, "
        print(student_info)


printInfo(studentNames)



