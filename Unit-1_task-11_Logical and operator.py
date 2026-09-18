#logical and operator
a = 5
result = a > 2 and a < 10
print("result of",a,"> 2 and", a ,"< 10:",result )

a = 1
result = a > 2 and a < 10
print("result of",a,"> 2 and", a ,"< 10:",result )

#Logical or operator
a = 1
result = a > 2 or a < 10
print("result of",a,"> 2 or", a ,"< 10:",result )

a = 5
result = a > 2 or a < 10
print("result of",a,"> 2 or", a ,"< 10:",result )

#Logical operator Not
a = 1
result = not(a > 2 and a < 10)
print("result of",(not(a > 2 and a < 10)),result )

a = 5
result = not(a > 2 and a < 10)
print("result of",(not(a > 2 and a < 10)),result )