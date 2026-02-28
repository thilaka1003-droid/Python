#1 to n
n=int(input("Enter number"))
print("Enter number",n)
for i in range(0,n):
    print(i)


# even numbers
for i in range(0,n):
    if(i%2==0):
        print(i)

#n to 1
for i in range(n,1,-1):
    print(i)

#sum upto n
sum=0
for i in range(0,n+1):
    sum+=i
print(sum)


 #sum of even numbers
sum=0
for i in range(1,n):
    if(i%2==0):
       sum=sum+i
print(sum)



#sum of digits of numbers
while(n!=0):
   dig=n%10
   sum+=dig
   n//=10
print(sum)


#count the numbers
count=0
while(n!=0):
    di=n%10
    count+=1
    n//=10
print(count)
        


