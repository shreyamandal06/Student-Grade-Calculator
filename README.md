# Student-Grade-Calculator
This is a Python program that takes input of 5 subjects from the user and calculates the Total, Average and Grade.

# Features
Takes input of 5 subjects.
Calculates the Total Marks.
Calculates the Average Marks.
Assigns a Grade based on Average:
A: 90 and above
B: 75 to 89
C: 50 to 74
F: Below 50

# Code
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

# How the code works
1. Start
2. The program uses a loop to ask the user to enter marks of 5 subjects and stores it in a list
3. Marks are added using built-in sum() function and prints the total
4. Average is calculated using the formula: Average = total/ number of subjects
5. using if-elif-else condition grade is assigned based on average.
6. Grade is printed.
7. End

# How to Run
1. Install Python on your system
2. save the code in a file grading.py
3. run the program

# Example Output
Enter Marks of Subject 1: 80
Enter Marks of Subject 2: 54
Enter Marks of Subject 3: 91
Enter Marks of Subject 4: 68
Enter Marks of Subject 5: 78
Toatl Marks of 5 Subjects:  371
Average Marks:  74.2
Grade C

