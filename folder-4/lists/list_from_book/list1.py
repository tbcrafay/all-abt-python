'''
(Assign grades) Write a program that reads a list of scores and then assigns grades
based on the following scheme:
The grade is A if score is >= 10.
The grade is B if score is >= 20.
The grade is C if score is >= 30.
The grade is D if score is >= 40.
The grade is F otherwise.
'''

# score_list = []
# scores = map(int, input().split())

# score_list.extend(scores)
# print(scores)
# print(score_list)

def assign_grades(scores):

    score_list = []
    score_list.extend(scores)

    for i, score in enumerate(score_list):   # i = index , score = value in that index
        grade = None

        if score < 40:
            grade = 'Fail'
        elif score >= 40 and score < 50:
            grade = "D"
        elif score >= 50 and score < 60:
            grade = "C"
        elif score >= 60 and score < 70:
            grade = "B"
        elif score >= 70 and score < 80:
            grade = "A" 
        else:
            grade = "A+"

        print(f'Student {i} score is {score} and grade is {grade}') 

if __name__=='__main__':
    scores = map(eval, input("enter the scores::").split())
    assign_grades(scores)

                





