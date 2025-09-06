marks = []

for i in range(5):
    a = int(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(a)

#Calculate total and average marks
total = sum(marks)
print("Toatl Marks of 5 Subjects: ", total)

average = total/5
print("Average Marks: ", average)

#Grade
if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 50:
    print("Grade C")
else:
    print("Grade F")



    
    




