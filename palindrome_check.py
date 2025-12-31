"""Check whether it is palidrome or not using Recursion"""

def check_palindrome(string,left,right):
    if left >= right:
        return True
    
    if string[left] != string[right]:
        return False
    
    return check_palindrome(string,left+1,right-1)


# a = check_palindrome("nitin",0,4)

# print(a)


