

record1 =["stdid","stdname" ,"standard","Student" ,"Age","Hindi","English" ,"Maths" ,"Science","computer","Total"]
record2 =['std101',"Ashish kumar",10 , 15, 67, 89, 87, 89, 90, 422]
record3= ["std102","Anhishek Kumar",10,14,85,45,48,90,45,330]
record4= ['std103',"Aman",10,15,23,56,78,78,67,304]
record5= ["std104","Rahul",10,  14,45,67,45,45,56,258]
record6= ["std105","Ruby", 10,  13,89,67,89,93,65,403]
record7= ["std106","Suman", 10,  13,90,46,67,67,67,337]
record8= ["std107","Saurabh",10 , 15,45,23,34,45,34,181]
record9= ["std108"," sumit",10, 14,23,35,45,67,78,90,303]
record10=["std109","kamlesh",10, 15,45,56,78,99,67,345]
record11 = ["std110","Rohan",10, 15,34,12,24,45,56,171]

llist = [record1,record2,record3,record4,record5,record6,record7,record8,record9,record10,record11]
#Task 1 : Printing the list in table like format
for row in llist:
    print(row)
print("-----------------------------------------------------------------------------------------------")
#-------------------------------------------------------------------------------------------------
 
#Task 2 : Printing the name of the students whose english marks are greater than 50
print("Name of students whose marks in english is greater than 50")
for rowindex in range(1,len(llist)):
    if (llist[rowindex][5]>50):
        print(llist[rowindex][1])

print("-------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------

#Task 3 :Printing the name of top 4 students there Age ,Score 
print("top four students in maths and there age")
students = []
for rowindex in range(1,len(llist)):
    student = {"name" : llist[rowindex][1],"maths":llist[rowindex][7],"age":llist[rowindex][3]}
    students.append(student)

#sorting the students
sorted_students =sorted(students,key =lambda x: x["maths"],reverse=True)

#printing the top four students
for student in sorted_students[:4]:
    print(f"Name :{student['name']},Age:{student['age']},Maths Score:{student['maths']}")

print("------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------

# Task 3 :Printing the Name ,Age ,Id of the students who are bottom three in computer

print("Bottom three students in Computer and their age and ID")

# Extracting names, Computer scores, ages, and IDs
students_computer = []
for rowindex in range(1, len(llist)):
    student = {
        "name": llist[rowindex][1],
        "computer": llist[rowindex][8],
        "age": llist[rowindex][3],
        "id": llist[rowindex][0]
    }
    students_computer.append(student)

# Sorting students by Computer scores in ascending order
sorted_students_computer = sorted(students_computer, key=lambda x: x["computer"])

# Printing the bottom three students in Computer and their ages and IDs
for student in sorted_students_computer[:3]:
    print(f"Name: {student['name']}, Age: {student['age']}, ID: {student['id']}, Computer Score: {student['computer']}")

