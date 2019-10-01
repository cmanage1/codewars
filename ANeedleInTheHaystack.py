#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle

def find_needle(haystack):
    
    for i in range (0, 50): #length of array didnt work so i put 50
        if haystack [i] == 'needle':
               return "found the needle at position " + str(i)
