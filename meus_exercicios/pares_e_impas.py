impares=open("ímpares.txt","w")
pares=open("pares.txt","w")
for n in range(0,1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
    else:
        impares.write("%d\n" % n)
impares.close()
pares.close()
print()