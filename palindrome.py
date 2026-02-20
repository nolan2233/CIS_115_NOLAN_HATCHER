
def isPalindrome(characters):
    reverseCharacters = characters[::-1]
    if characters == reverseCharacters:
        return True
    else: 
        return False 
    
myString = input("Enter a String of min 5 characters ")

if len(myString) < 5:
    print("String must be atleast 5 characters long.")
else: 
    if isPalindrome(myString):
        print(f"The string {myString} is a palindrome.")
    else:
        print(f"The string {myString} is NOT a palindrome.") 


