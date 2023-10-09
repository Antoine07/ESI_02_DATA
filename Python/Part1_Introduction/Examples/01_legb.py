"""
Définition des variables dans le script

LEGB 
"""

# G espace global
a = 101
b = 22

def foo():
    b = 1
    # E englobant puis il remonte
    def baz():
        # Python regarde localement la déf de b, il ne la trouve pas donc il regarde englobant, puis globalement, puis builtins
        print(b)
        print(a)

    baz()

    return "scope"

# Affiche 
# 1
# 101
print( foo() )