#Complete the solution so that it splits the string into pairs of two characters. 
#If the string contains an odd number of characters then it should replace the 
#missing second character of the final pair with an underscore ('_').

#solution('abc') # should return ['ab', 'c_']
#solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    output=[]
    if len(s) == 0:
        return [] 
    for i in range (len(s)):
        if i % 2 == 0: 
            output.append(s[i])  
        else:
            output[(i-1)//2] += s[i]
    if len(output[-1]) == 1:
        output[-1] += '_'
    return output
