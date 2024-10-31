Lista=[7,8,2,5,3,2,9,3,1,5,3,4,6]
n = len(Lista)
i=0
j=0
Temp = ""
print(Lista)
for i in range(n-1):
    for j in range(n-i-1):
        if Lista[j]>Lista[j+1]:
            Temp = Lista[j+1]
            Lista[j+1] = Lista[j]
            Lista[j] = Temp
            print(Lista)
