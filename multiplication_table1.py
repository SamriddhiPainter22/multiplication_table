import numbers


number=int(input("Enter a no. which user wants to print the multiplication table of :"))
print("The multiplication table of: ",number)
for count in range(1,11):
    print(number,'x',count,'=',number* count)
    