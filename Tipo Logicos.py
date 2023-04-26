ed1=int(input("Ingrese su edad: "))
if ed1>=18:
    print("Usted es mayor de edad")
    tit1=input("Tiene titulo de bachiller: ").lower()
    if tit1=="si":
        print("Si puede sacar la Licencia")
    else:
        print("No tiene titulo de bachiller")
else:
    print("Usted NO es mayor de edad")
    if ed1>=16 and ed1<18:
        print("Existe la posibilidad de un permiso de aprendizaje")
    else:
        print("No es posible sacar una licencia")