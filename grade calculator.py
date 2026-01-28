x = 0
v = 0
total_ch = 0
count = 0
classes = int(input("how many classes are you taking: "))
while count < classes:
    class_ = input("name of class: ")  
    class_grade = float(input("percent grade of class: "))
    class_ch = int(input("enter class credit hours: "))
    total_ch = class_ch + total_ch
    if class_grade >= 90:
        grade = "A"
        x = 4
    elif class_grade >= 80:
        grade = "B"
        x = 3
    elif class_grade >= 70:
        grade = "C"
        x = 2
    elif class_grade >= 60:
        grade = "D"
        x = 1
    else:
        grade = "F"
        x = 0
    v = v + (class_ch * x)
    total_ch = class_ch + total_ch
    print(f"your grade in {class_} is a {grade}")
    
    count += 1
print(v)
print(total_ch)
gpa = v/(total_ch/2)
print(f"your gpa is {gpa} ")








