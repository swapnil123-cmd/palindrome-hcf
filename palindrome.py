num=int(input("Enter a number: "))
temp=num
reversed=0

while temp>0:#151 , 15, 1
  digit=temp % 10 # 1, 5, 1
  reversed=reversed*10+digit #reversed=1, reversed=1*10+5=15, reversed=15*10+1
  temp//=10 # temp=15, 1, 0(loop is stopped)
  
if num==reversed:
  print("It is a palindrome")
else:
  print("It is not a palindrome")
  
  # to find the HCF between 2 numbers
numberLargest=int(input("Enter the largest number: ")) #8  #14
numberSmallest=int(input("Enter the smallest number: ")) #4 #6
while numberSmallest: # 4 # 6 & 2 & 0(loop terminated)
  numberStore=numberSmallest # numberStore=4 # numberStore=6 & 2
  numberSmallest=numberLargest %  numberSmallest # numberSmallest=0 # numberSmallest=2 & 0
  numberLargest=numberStore #numberLargest=4 # numberLargest= 6 # numberLargest=2(HCF)
  
print("HCF is ", numberLargest)