# Creación de la primera carpeta, sin nombre y luego renombrada a Portafolio en el directorio actual.
Asig=[['Ciencias Sociales I','Cultura Digital I','Humanidades I','Inglés I','La materia y sus interacciones CNEYT I','Lengua y Comunicación I','Pensamiento Matemático I'],['Ciencias Sociales II','Conservación de la energía y su interacción con la materia CNEYT II','Cultura Digital II','Humanidades II','Inglés II','Lengua y Comunicación II','Pensamiento Matemático II'],['Ecosistemas, interacciones, energia y dinamica CNEYT III','Humanidades III','Inglés III','Lengua y Comunicación III','Pensamiento Matemático III'],['Ciencias Sociales III','Conciencia Histórica I','Inglés IV','Reacciones químicas conservación de la materia en la formación de nuevas sustancias CNEYT IV'],['Conciencia Histórica II','La energía en los procesos de la vida diaria CNEYT V'],['Conciencia Histórica III','Cultura Digital III','Organismos, estructuras y procesos. Herencia y evolución biológica CNEYT VI']]
import os
def Carpeta(C_nom):
    if os.path.exists(C_nom):
        if os.path.exists(C_nom+'.old'):
            os.rmdir(C_nom+'.old')
        os.rename(C_nom,C_nom+'.old')
    os.mkdir(C_nom)
def Rename(C_nom):
    if not os.path.exists(C_nom):
        os.mkdir(C_nom)
nombre='Portafolio1'
Carpeta(nombre)
SemE = 1
os.chdir(nombre)
match SemE:
    case 1:
        AsigS=len(Asig[SemE])
        ContA = 0
        CarpS = str(SemE)+'ºSem'
        Carpeta(CarpS)
        os.chdir(CarpS)
        for ContA in range(AsigS):
            Carpeta(Asig[SemE-1][ContA])
    case 2:
        print('2')
