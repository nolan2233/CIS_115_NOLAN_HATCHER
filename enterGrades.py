#this program will allow a user to enter up to 10 grades

numOfGrades = int(input("How many grades would you like to enter?   "))
count = 0

while count < numOfGrades: 
   count = count + 1 
   grade = input("Enter Your Grades:  ")

   if(count > numOfGrades):
      print(f"The user entered {numOfGrades} and is now done.")
      

