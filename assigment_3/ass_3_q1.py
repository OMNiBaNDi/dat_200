
"""
#Iterative approach
def is_Palindrome(word):
    front = 0
    back = len(word) - 1

    while front != back:
        
        if word[front] != word[back]:
            return print("False")
        
        else:
            front += 1
            back -=1
    print("True")
        
        
    
is_Palindrome("rutor")
is_Palindrome("rotor")

"""

def is_Palindrome_Recursive(word):
    
    #base case if word has 0 or 1 letters
    if len(word) <= 1:
        return True
    
    #check if first letter and last letter are the same
    elif word[0] != word[-1]:
        return False
    
    #Recursively call the function and slicing of the first and last letters that where checked
    else:
        return is_Palindrome_Recursive(word[1:-1])

print(is_Palindrome_Recursive("rotor"))
print(is_Palindrome_Recursive("motor"))
