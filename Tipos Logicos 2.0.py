var1=True
while var1==True:
    print("Menu:\n\t1.Mostrar mensaje de saludo y salir. \n\t2. Volver a mostar el menu\n\t3.SALIR ")
    var2=int(input("Ingrese su opcion: "))
    if var2==1:
        print("SALUDOS")
        var1=False
    elif var2==2:
        var1=True
    elif var2==3:
        print("Programa Terminado")
        var1=False