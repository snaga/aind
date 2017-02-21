def cross(a, b):
    return [s+t for s in a for t in b]

def grid_values(vals):
    keys = cross(rows,cols)
    assert len(keys) == len(vals)
    dic = {}
    for k,v in zip(keys, vals):
        dic[k] = v
    return dic

from utils import *

if __name__ == '__main__':
    rows = 'ABCDEFGHI'
    cols = '123456789'
    
    boxes = cross(rows, cols)
    print(boxes)
    
    row_units = [cross(r, cols) for r in rows]
    print(row_units[0])
    
    column_units = [cross(rows, c) for c in cols]
    print(column_units[0])
    
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    print(square_units[0])
    
    unitlist = row_units + column_units + square_units

    print (grid_values("..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."))
    display(grid_values("..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."))
