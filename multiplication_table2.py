from itertools import count


number=int(input("Enter the no. which user wants multiplication table of: "))
count=1
print("The multiplication table : ",number)
while count<=10:
    number=number*1
    print(number,'x',count,'=',number* count)
    count+=1