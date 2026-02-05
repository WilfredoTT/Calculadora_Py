import math
def menu ():
    
    opcion = input("SI DESEA SUMAR UTILICE EL SIGNO(+) /n SI DESEA RESTAR EL SIGNO(-) /n SI DESEA LA RAIZ CUADRADA EL SIGNO(*) /n OPCION:")
    
    if opcion == "+":
        print(f"LA SUMA DE LOS NUMEROS {numero_1} + {numero_2} es igual a: {numero_1 + numero_2}")
        
    elif opcion == "-":
        print(f"LA RESTA DE LOS NUMEROS {numero_1} - {numero_2} es igual a: {numero_1 - numero_2}")
        
    elif opcion == "*":
        opcion=input(f"ELIJA DE QUE NUMERO DESEA OBTENER LA RAIZ CUADRADA /n 1.)1:{numero_1} o 2:{numero_2} OPCION:")

        if opcion == "1":
            resultado = round(math.sqrt(numero_1))
            print(f"LA RAIZ CUADRADA DEL NUMERO:{numero_1} ES RESULTADO:{resultado}")
            
        elif opcion == "2":
            resultado = round(math.sqrt(numero_2))
            print(f"LA RAIZ CUADRADA DEL NUMERO:{numero_2} ES RESULTADO:{resultado}")
            
    else:
        print("VERIFIQUE LA OPCION QUE ESTA ESCOGIENDO")
        menu()
        
numero_1 = float(input("INGRESE EL PRIMER NUMERO:"))
numero_2 = float(input("INGRESE EL SEGUNDO NUMERO:"))
menu()

