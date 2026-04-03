def is_palindrome(substring):
    
    if substring == substring[::-1]:
        return True
    return False 

def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    
    max_sub = ""
    for i in range(len(s)):
        for j in range(i+2,len(s)+1):
            if is_palindrome(s[i:j]):
                current_sub = s[i:j]
                
                if len(current_sub) > len(max_sub):
                    max_sub = current_sub

    return max_sub


