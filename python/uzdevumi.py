def tests(parametrs):
    a = parametrs #darbības ar parametriem
    return a #funkcijas rezultāts

print(tests("kaķis"))

def pirmais(par1, par2):
    reizinajums = par1*par2
    summa = par1+par2
    if reizinajums<1000 :
        return reizinajums
    else:
        return summa

print("The result is", pirmais(20,30) )
