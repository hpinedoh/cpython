Datos=[]
Rojo="\033[31m"
Azul="\033[7;34m"
Normal="\033[0m"
#Datos=['Heraclio', 'Junior', 'Pinedo Hernández', 'Plaza Madero', '30', 'Centro', 'Villa González Ortega', '7', '8']
for i in range(9):
    if i==0:
        print("Escribe tu primer nombre")
    elif i==1:
        print("¿tienes más nombres? si/no")
        if input()!= "no":
            print("Escríbelos")
        else:
            Datos.append("")
    elif i==2:
       print("Escribe tus apellidos")
    elif i==3:
        print("Escrible el nombre de la calle donde está tu casa")
    elif i==4:
        print("Escrible el número de tu casa")
    elif i==5:
        print("Escrible el nombre de la colonia")
    elif i==6:
        print("Escrible el nombre de tu comunidad")
    elif i==7:
        print("Escrible tu calificación del M3S1")
    elif i==8:
        print("Escrible tu calificación del M3S2")
    Datos.append(input())
print(Datos)

print("Los datos que capturaste son:\n")
print(f"\t\t\t{Rojo}Nombre","\t\t\t\t\tDomicilio","\t\t\t\tCalif. M3S1","\t\tCalif. M3S2")
print(f"{Azul}\t",Datos[0],"\b",Datos[1],"\b",Datos[2],"\t",Datos[3],"#",Datos[4],"\b,",Datos[5],"\b,",Datos[6],"\t\t",Datos[7],"\t\t\t",Datos[8])
print(f"{Normal}\nFin")
