n = '\n'

def gen_membrane(L, W, path, j):
    text = (
    f'package require pbctools {n}'
    f'package require topotools {n}'
    f'package require nanotube {n}'
    f'set fname {W}x{L[j]}.pdb {n}'
    f'set fdata {W}x{L[j]}.full {n}'
    f'set my_lx {W} {n}'
    f'set my_ly {L[j]} {n}'
    f'graphene -lx $my_lx -ly $my_ly -type armchair -nlayers 1 -b 1 -a 1 -d 1 -i 1 -cc 0.1148 -ma C-C {n}'
    f'set sel [atomselect top all] {n}'
    f'$sel move [transaxis x 90] {n}'
    f'$sel move [transaxis z 90] {n}'
    f'set box {{{2 * L[j]} {2 * L[j]} {2 * L[j]} 90 90 90}} {n}'
    f'pbc set $box {n}'
    f'source /home/woellner/IC/Douglas/estruturas/sculptor.tcl {n}'
    f'::Sculptor::sculpt \"{path}\" {n}'
    f'set center [measure center $sel weight none] {n}' 
    f'$sel moveby [vecscale -1.0 $center] {n}'
    f'topo writelammpsdata /home/woellner/IC/Douglas/estruturas/data/$fdata full {n}'
    f'$sel writepdb/home/woellner/IC/Douglas/estruturas/pdb/$fname {n}'
    )
    return text

def source(L, W, j):
    text = (
        f'source {W}x{L[j]}.tcl {n}'
    )
    return text
