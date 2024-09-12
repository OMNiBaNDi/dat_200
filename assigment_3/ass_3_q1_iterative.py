#Iterative approach
def is_Palindrome(word):
    front = 0
    back = len(word) - 1

    while front < back:
        
        if word[front] != word[back]:
            return print("False")
        
        else:
            front += 1
            back -=1
    print("True")
        
        
    
is_Palindrome("rotor")
