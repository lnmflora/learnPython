def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print("Choisis l'operation:")
print("1.Addition")
print("2.Soustraction")
print("3.Multiplication")
print("4.Division")

choix = input("Entre ton choix (1/2/3/4):")
num1 = int(input("Entre un premier nombre: "))
num2 = int(input("Entre un second nombre: "))

if choix == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choix == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choix == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choix == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Entree non valide")
