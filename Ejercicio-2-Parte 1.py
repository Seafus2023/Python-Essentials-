Datos_2021=[1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
lst1=tuple(Datos_2021)
n = 1
while (n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6 or n == 7 
       or n == 100 or n == 91 or n == 110 or n == 900 or n == 21 or n ==33
        or n == 32 or n == 2 or n == 4 or n == 8 or n == 10 or n == 13 
        or n == 13 or n == 16 or n == 15 or n == 1302) > 0:
    if n % 2 == 1:
        print("El numero",n,"es impar")
        n+= 1
    else:
        print("El numero",n,"es par")
        n+= 1
