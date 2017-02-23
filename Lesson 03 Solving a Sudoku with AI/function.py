# -*- coding: utf-8 -*-

from utils import *

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
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    values2 = values.copy()
    for k in sorted(values.keys()):
        row = k[0]
        col = k[1]
#        print("%s: %s" % (k, values[k]))
        if len(values[k]) == 1:
            continue
#        print("before: " + values[k])
        values2[k] = eliminate_one(values, cross(row, "123456789"), values2[k])
        values2[k] = eliminate_one(values, cross("ABCDEFGIH", col), values2[k])
        r,c = get_rows_cols(k)
#        print(cross(r, c))
        values2[k] = eliminate_one(values, cross(r, c), values2[k])
#        print("after: " + values2[k])
    return values2

def trace(s):
    if False:
        print (s)

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    values2 = values.copy()
#    display(values)
    peer_to_values = {}
    for box in sorted(values.keys()):
        trace("box: %s" % box)
        for unit in unitlist:
            # boxの属するunitを探す
            if box not in unit:
                continue
            trace("unit: %s" % unit)

            # unit内のpeerの状態を確認する
            value_to_peers = {}
            for peer in unit:
                trace("peer-values: %s => %s" % (peer, values[peer]))
                # peerがどの値を持ちうるかをdictにする（key:value、value:peer名のリスト）
                for value in values[peer]:
                    if value not in value_to_peers:
                        value_to_peers[value] = []
                    value_to_peers[value].append(peer)
            for value in value_to_peers:
                trace("value-peers: %s => %s" % (value, value_to_peers[value]))
                if len(value_to_peers[value]) == 1:
                    peer = value_to_peers[value][0]
                    trace("found: %s => %s" % (peer, value))
                    values2[peer] = value
#    display(values2)
    values = values2.copy()
    return values

if __name__ == '__main__':
    grid = "..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3.."
#    print(square_units)
    print("start:")
    values = grid_values(grid)
    display(values)

    print("eliminating:")
    values = eliminate(values)
    display(values)

    print("applying only choice:")
    values = only_choice(values)
    display(values)

    print("applying only choice:")
    values = only_choice(values)
    display(values)

    print("applying only choice:")
    values = only_choice(values)
    display(values)
