from scipy import constants as sp

def lam(U):
    return (sp.h * sp.c) / (sp.e * U)

print(lam(8))
