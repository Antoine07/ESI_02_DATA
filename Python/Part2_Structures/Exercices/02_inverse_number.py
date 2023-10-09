
num = -6523

# signe de num
sign = -1 if num < 0 else 1
# si négatif le signe saute, si positif rien ne change
num = sign * num 
mumStr = str(num)

# mumStr = mumStr[1::] if sign < 0 else mumStr[0::] 

num = sign * int( mumStr[::-1] )

def invNum(num):
    # signe 
    sign = -1 if num < 0 else 1
   
    # on retire le signe astuce matheuse
    sign = -1 if num < 0 else 1
    num = sign * num 

     # on transforme en chaine de caractères pour l'inverser
    mumStr = str(num)

    return  sign * int( mumStr[::-1] )

print( invNum(-9181716) )
print( invNum(9181716) )
