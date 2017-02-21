def cross(a, b):
    return [s+t for s in a for t in b]

def grid_values(vals):
    keys = cross(rows,cols)
    assert len(keys) == len(vals)
    dic = {}
    for k,v in zip(keys, vals):
#        dic[k] = v
        dic[k] = v if v != '.' else '123456789'
    return dic

def eliminate_one(values, unit_keys, target):
    for k in unit_keys:
        if len(values[k]) == 1:
#            print("%s = %s" % (k, values[k]))
            target = target.replace(values[k], "")
    return target

def get_rows_cols(k):
    if k[0] in 'ABC':
        r = 'ABC'
    if k[0] in 'DEF':
        r = 'DEF'
    if k[0] in 'GHI':
        r = 'GHI'
    if k[1] in '123':
        c = '123'
    if k[1] in '456':
        c = '456'
    if k[1] in '789':
        c = '789'
    return (r,c)

def eliminate(values):
    values2 = values.copy()
    for k in sorted(values.keys()):
        row = k[0]
        col = k[1]
        print("%s: %s" % (k, values[k]))
        if len(values[k]) == 1:
            continue
        print("before: " + values[k])
        values2[k] = eliminate_one(values, cross(row, "123456789"), values2[k])
        values2[k] = eliminate_one(values, cross("ABCDEFGIH", col), values2[k])
        r,c = get_rows_cols(k)
        print(cross(r, c))
        values2[k] = eliminate_one(values, cross(r, c), values2[k])
        print("after: " + values2[k])

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

    eliminate(grid_values("..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."))
