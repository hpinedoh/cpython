"""Primer Semestre
Segundo Semestre
Tercer Semestre
Cuarto Semestre
Quinto Semestre
Sexto Semestre
Recursos Socioemocionales
Recursos Socioemocionales"""
Asig=[['Ciencias Sociales I','Cultura Digital I','Humanidades I','Inglés I','La materia y sus interacciones CNEYT I','Lengua y Comunicación I','Pensamiento Matemático I'],['Ciencias Sociales II','Conservación de la energía y su interacción con la materia CNEYT II','Cultura Digital II','Humanidades II','Inglés II','Lengua y Comunicación II','Pensamiento Matemático II'],['Ecosistemas, interacciones, energia y dinamica CNEYT III','Humanidades III','Inglés III','Lengua y Comunicación III','Pensamiento Matemático III'],['Ciencias Sociales III','Conciencia Histórica I','Inglés IV','Reacciones químicas conservación de la materia en la formación de nuevas sustancias CNEYT IV'],['Conciencia Histórica II','La energía en los procesos de la vida diaria CNEYT V'],['Conciencia Histórica III','Cultura Digital III','Organismos, estructuras y procesos. Herencia y evolución biológica CNEYT VI']]
Porta='./Portafolio'
Sem=5
import os
ruta=os.getcwd()
# print('La ruta actual es', ruta)
if not os.path.exists(Porta):
    os.mkdir(Porta)
#    print('Directorio %s creado!' % Porta)
ruta2=(ruta+'/Portafolio')
# print('La ruta nueva es', ruta2)
os.chdir(ruta2)
i=0
while i <= Sem:
    i=1+i
    if not os.path.exists(str(i)+'ºSem'):
        os.mkdir(str(i)+'ºSem')
        print(asig(i-1))
#    print('Mi path es', rutaact)
#    os.mkdir(rutaact)
matrix_length=len(Asig)
# print(matrix_length)
"""j=0
k=0
for j in range(matrix_length):
    print(j)
    Length_a=len(Asig[0])
    print(Length_a)
    for k in range(Length_a):
#        print(Length_a)
        print(Asig[0][k])
        """
def asig(i):
    print('Si entré, mis valores son i', i, 'y k', k)
    Length_a=len(Asig[i])
    k=0
    for k in range(Length_a):
        print(Asig[i][k])
        return(Asig[i][k])
