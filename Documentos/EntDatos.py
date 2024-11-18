Datos=[]
Rojo="\033[31m"
Azul="\033[7;34m"
Verde="\033[1;32m"
Normal="\033[0m"
# Datos=['Heraclio', 'Junior', 'Pinedo Hernández', 'Plaza Madero', '30', 'Centro', 'Villa González Ortega', '7', '8']
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

print(f"\n{Verde}\033[3;9HLos datos que capturaste son:\n")
print(f"\033[5;9H{Rojo}Nombre","\033[5;45HDomicilio","\033[5;98HCalif. M3S1","\033[5;115HCalif. M3S2")
print(f"\033[6;9H{Azul}\b",Datos[0],"\b",Datos[1],"\b",Datos[2],"\033[6;45H\b",Datos[3],"#",Datos[4],"\b,",Datos[5],"\b,",Datos[6],"\033[6;102H",Datos[7],"\033[6;119H",Datos[8])
print(f"{Verde}\nFin{Normal}")
