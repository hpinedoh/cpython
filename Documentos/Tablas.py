i = 0
j = 0
while i < 12 :
    i += 1
    print("\t \t *****************")
    print("\t Esta es la tabla del \t", i)
    while j < 12:
        j += 1
        print(i,"\t X \t", j, "\t = \t ", i*j)
    j = 0
    
print("\t **** Terminé el ejercicio \t ****")