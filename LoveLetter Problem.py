#Gentle Ramirez April 16th, 2020
#HRank Love Letter 
def mystery(letter):
    n=len(letter)
    count=0
    for i in range (n//2):
        x= ord(letter[i])
        y= ord(letter[(n-1)-i])
        if x != y:
            if x > y:
                count+= x-y
            else:
                count += y-x
    return count

z= int(input())
for _ in range (z):
    letter=input()
    print(mystery(letter))

