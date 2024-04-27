def grading_system():
    marks = int(input("ENTER YOUR MARKS: "))
    if marks>90:
        print("YOUR GRADE IS A+")
    elif marks<90 and marks>80:
        print("YOUR GRADE IS A")
    elif marks<80 and marks>75:
        print("YOUR GRADE IS B+")
    elif marks<75 and marks>70:
        print("YOUR GRADE IS B")
    elif marks<70 and marks>60:
        print("YOUR GRADE IS C")
    elif marks<60 and marks>45:
        print("YOUR GRADE IS D")
    else:
        print("YOUR GRADE IS F")
grading_system()