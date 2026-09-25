#1. add two numbers
a = int(input("enter number 1 : "))
b = int(input("Enter number 2 : "))

print("Sum is ", a + b)

#2. Find rmeainder a divided by b
print("remainder is ", a % b)


#3. compare the value
if a > b:
    print(a, " is greater than ", b)
elif b > a:
    print(b, " is greater than ", a)

#4. average of 2 number
print("Average of a and b : " , (a + b) // 2)

#5. Square of a number
print("square of a : ", a * a)