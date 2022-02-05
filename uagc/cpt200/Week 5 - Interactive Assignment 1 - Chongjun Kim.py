'''
CPT200 - Week 5 - Interactive Assignment 1
Author: Chongjun Kim
Due Date: 09/16/2021
Title: Driver's License Exam
'''
from tkinter import Tk
from tkinter.filedialog import askopenfilename # module that opens file selector

Tk().withdraw() # opens file selector when program runs
filename = askopenfilename() # gets file directory and name

student_submission = open (filename) # gets file content
submission = student_submission.read() # stores content from file
submission_list = submission.split(",") # generates a list

# list of correct answers
answers = ['b', #1
           'd', #2
           'a', #3
           'a', #4
           'b', #5
           'a', #6
           'b', #7
           'a', #8
           'c', #9
           'd', #10
           'b', #11
           'c', #12
           'd', #13
           'a', #14
           'd', #15
           'c', #16
           'c', #17
           'b', #18
           'd', #19
           'a'  #20
           ]

# compares and finds all matching values from two lists
def findMatch(list1, list2):
    global score, questions
    index = 0
    score = 0
    questions =[]
    while len(answers) > index:
        if submission_list[index] == answers[index]:
            score += 1
        else:
            questions.append(index + 1) # adding 1 because index falls behind since it starts from 0
        index += 1
    return score

def result():
    correctAnswers = findMatch(submission_list, answers) # find matches
    score = correctAnswers
    wrong = len(answers) - score
    questions_converted = [str(element) for element in questions] # convert integer to string
    questions_string = ", ".join(questions_converted) # remove brackets
    
    print("You scored", score, "out of", len(answers), "questions.")
    print("You got", wrong, f"answer{'s'[:wrong^1]} wrong.")
    print("The incorrectly answered " +
          f"question{'s'[:wrong^1]} " +
          f"{'is' if wrong == 1 else 'are'}", # pluralize words when necessary
          questions_string + ".") # using '+' instead of ',' to avoid extra space

    # validate pass/fail and print message
    if correctAnswers < 15:
        print('Failed!')
    else:
        print('Passed!')

result()
