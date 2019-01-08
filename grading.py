# grading challenge
# 73, 67, 38, 33
# 75, 67, 40, 33

my_array = [73, 67, 38, 33]
new_array = []

def grade_checker(grades_to_check):
    for grade in grades_to_check:
        if grade < 38:
            new_array.append(grade)
            continue
        new_grade = grade
        for i in range(3):
            if new_grade % 5 == 0:
                new_array.append(new_grade)
                break
            else:
                new_grade = new_grade + 1
                print (new_grade,' {}'.format('New grade'))
                if new_grade - grade == 3:
                    new_array.append(grade)
        
        

grade_checker(my_array)

print (new_array)



                
