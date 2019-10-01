#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):

    temp= []
    output=''
    counter=1

    for i in range (len(s)):
        temp=s[i]
        temp *= counter #multiplies letter by position number
        output+= temp[:1].upper() + temp[1:].lower()  #capitalizes and adds to output
        if counter <= (len(s) -1):
            output+= '-'
        counter+=1
    return output
