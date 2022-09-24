import numpy as np
from spiral import spiral
from text import*


# Parâmetros para criar uma lista de numeros.
start = 5 # Numero Inicial
step = 5 # Quantos numeros pulam a cada passo
num = 2 # Total de numeros dentro da lista

L = np.arange(0,num)*step+start # Ly
W = 5 # Lx

## Gerador de Estruturas e dos arquivos pdb e data.
for i in range(len(L)):
    for j in range(len(L)):
        filemask = f'{W}x{L[j]}.tcl'
        pathname = '/Users/kyoun/IC/estruturas/'
        filename = pathname+filemask
        f = open(filename,'x')
        path = spiral(L[j])
        text = gen_membrane(L, W, path, j)
        f.write(text)
    W += 5


## Gerador do arquivo texto de source vmd
W = 5
filemask = f'source.txt'
pathname = '/Users/kyoun/IC/estruturas/'
filename = pathname+filemask
f = open(filename,'x')
for i in range(len(L)):
    for j in range(len(L)):
        text = source(L, W, j)
        f.write(text)
    W += 5
