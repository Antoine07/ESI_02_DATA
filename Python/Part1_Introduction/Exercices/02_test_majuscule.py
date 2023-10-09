
alphabetMajuscule = [ *"ABCDEFGHIJKLMOPQRSTUVWXYZ" ]

#02 Exercice lettre en majuscule<
def testUpper(l):
    # lève une exception si pas d'élément dans la liste
    assert len(l) > 0

    for el in l:
        if el not in alphabetMajuscule:
            return False

    return True 

print( testUpper(['A', 'B', 'C' , 'D']) )
print( testUpper(['A', 'b', 'C' , 'D']) )

