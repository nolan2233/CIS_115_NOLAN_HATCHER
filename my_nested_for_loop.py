#this program created a nested for loop from prompt 2 

def printWordList():
    list = ["Apples", "Bananas", "Pears", "Carrots"]

    for item in list:
         print(item)

         for letter in item:
           
           print(letter) 
       
       
printWordList()