
def is_Palindrome_Recursive(word):
    
    #base case if word has 0 or 1 letters
    if len(word) <= 1:
        return True
    
    #check if first letter and last letter are the same
    if word[0] != word[-1]:
        return False
    
    #Recursively call the function and slicing of the first and last letters that where checked
    return is_Palindrome_Recursive(word[1:-1])

print(is_Palindrome_Recursive("appa"))

