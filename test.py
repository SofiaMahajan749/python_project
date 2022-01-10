num1=int(input('Enter your number1: '))
num2=int(input('Enter your number2: '))
ops= input('Enter the operation you want to perform:
+ for addition
- for subtraction
* for multiplication
/ for division')
if ops=='+':
 print('{} + {} = '.format(num1,num2))
 print (num1+num2)
elif ops=='-':
  print('{} + {} = '.format(num1,num2))
  print (num1-num2)
elif ops=='*':
  print('{} * {} = '.format(num1,num2))
  print (num1*num2)
elif ops=='/':
  print('{} + {} = '.format(num1,num2))
  print (num1/num2)
else:
print('Ypou have not typed the vaild operator.')
