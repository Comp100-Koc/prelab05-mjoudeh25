def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    has_duplicates = True
    
    
    while has_duplicates:
        has_duplicates = False
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i]+ s[i+2:]
                
                has_duplicates = True
                
                break
            
    return s
        
        
        