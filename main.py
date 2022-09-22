import numpy as np


## Parâmetros para criar uma lista de numeros.
start = 5
step = 5
num = 2
##

L = np.arange(0,num)*step+start
W = 5
n = '\n'

## Gerador de Estruturas e dos arquivos pdb e data.
for i in range(len(L)):
    for j in range(len(L)):
        filemask = f'{W}x{L[j]}.tcl'
        pathname = '/Users/kyoun/IC/estruturas/'
        filename = pathname+filemask
        f = open(filename,'x')
        f.write(f'set fname {W}x{L[j]}.pdb {n}'
                f'set fdata {W}x{L[j]}.full {n}'
                f'set my_lx {W} {n}'
                f'set my_ly {L[j]} {n}'
                f'graphene -lx $my_lx -ly $my_ly -type armchair -nlayers 1 -b 1 -a 1 -d 1 -i 1 -cc 0.1148 -ma C-C {n}'
                f'set sel [atomselect top all] {n}'
                f'$sel move [transaxis x 90] {n}'
                f'$sel move [transaxis z 90] {n}'
                f'topo writelammpsdata /Users/kyoun/IC/estruturas/data/$fdata full {n}'
                f'$sel writepdb /Users/kyoun/IC/estruturas/pdb/$fname {n}')
    W += 5
##

## Gerador do arquivo texto de source vmd
W = 5
filemask = f'source.txt'
pathname = '/Users/kyoun/IC/estruturas/'
filename = pathname+filemask
f = open(filename,'x')
for i in range(len(L)):
    for j in range(len(L)):
        f.write(f'source {W}x{L[j]}.tcl {n}')
    W += 5
##

