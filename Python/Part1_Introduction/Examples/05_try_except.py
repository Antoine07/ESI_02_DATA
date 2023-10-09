a, b = 1, 0

try:
    # Python lève une exception : ZeroDivisionError
    c =  a / b 

# si rien on capture toutes les erreurs, et sinon on précise l'erreur que l'on souhaite capturer
# except: # attrape toutes les exceptions 
except ZeroDivisionError:

    print("zero au diviseur")

print('----------------------------------')

try:

    if b == 0:
        raise ValueError("Division par zéro n'est pas autorisée.")

    c =  a / b 

except ValueError as e:
    print(e)
    print("zero au diviseur")

# On peut personnaliser ses exceptions

# On hérite de la classe Exception
class MyExceptionZero(Exception):
    def __init__(self, message="Error 00 (Bab division)"):
        self.message = message
        # Surcharger le constructeur de la classe Exception
        super().__init__(self.message)


try:

    if b == 0:
        raise MyExceptionZero()

    c =  a / b 

except MyExceptionZero as e:
    print(e)