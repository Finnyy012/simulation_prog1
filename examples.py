import queue
import time

import numpy as np
import FSM

##string w/ oneven 'a' en even 'b'
def odd_a_even_b(str):
    rules = [
        ['XV','b','XX'],
        ['XX','b','XV'],
        ['XX','a','VX'],
        ['VX','a','XX'],
        ['VX','b','VV'],
        ['VV','b','VX'],
        ['VV','a','XV'],
        ['XV','a','VV']]

    accepting = ['VV']

    g = FSM.graph(rules, accepting, 'circo')
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)

    print(FSM.eval_FSM_tape(rules, str, accepting))

# [ ][ ]  [X][ ]  [ ][X]  [ ][ ]  [ ][ ]  [X][O]  [X][ ]  [X][ ]  [O][X]
# [ ][ ], [ ][ ], [ ][ ], [X][ ], [ ][X], [ ][ ], [O][ ], [ ][O], [ ][ ],
# r1      r2      r3      r4      r5      r6      r7      r8      r9
# [ ][X]  [ ][X]  [O][ ]  [ ][O]  [ ][ ]  [O][ ]  [ ][O]  [ ][ ]  [X][O]
# [O][ ], [ ][O], [X][ ], [X][ ], [X][O], [ ][X], [ ][X], [O][X], [X][ ],
# r10     r11     r12     r13     r14     r15     r16     r17     r18-A
# [X][O]  [X][X]  [X][ ]  [X][X]  [X][ ]  [O][X]  [O][X]  [ ][X]  [ ][X]
# [ ][X], [O][ ], [O][X], [ ][O], [X][O], [X][ ], [ ][X], [O][X], [X][O],
# r19     r20-A   r21     r22-A   r23-A   r24     r25-A   r26-A   r27
# [O][ ]  [ ][O]
# [X][X], [X][X]
# r28-A   r29-A

def tictactoe_old():
    rules = [
        ['[ ][ ][ ][ ]', '0', '[X][ ][ ][ ]'], #r1
        ['[ ][ ][ ][ ]', '1', '[ ][X][ ][ ]'],
        ['[ ][ ][ ][ ]', '2', '[ ][ ][X][ ]'],
        ['[ ][ ][ ][ ]', '3', '[ ][ ][ ][X]'],
        ['[X][ ][ ][ ]', '1', '[X][O][ ][ ]'], #r2
        ['[X][ ][ ][ ]', '2', '[X][ ][O][ ]'],
        ['[X][ ][ ][ ]', '3', '[X][ ][ ][O]'],
        ['[ ][X][ ][ ]', '0', '[O][X][ ][ ]'], #r3
        ['[ ][X][ ][ ]', '2', '[ ][X][O][ ]'],
        ['[ ][X][ ][ ]', '3', '[ ][X][ ][O]'],
        ['[ ][ ][X][ ]', '0', '[O][ ][X][ ]'], #r4
        ['[ ][ ][X][ ]', '1', '[ ][O][X][ ]'],
        ['[ ][ ][X][ ]', '3', '[ ][ ][X][O]'],
        ['[ ][ ][ ][X]', '0', '[O][ ][ ][X]'], #r5
        ['[ ][ ][ ][X]', '1', '[ ][O][ ][X]'],
        ['[ ][ ][ ][X]', '2', '[ ][ ][O][X]'],
        ['[X][O][ ][ ]', '2', '[X][O][X][ ]'], #r6
        ['[X][O][ ][ ]', '3', '[X][O][ ][X]'],
        ['[X][ ][O][ ]', '1', '[X][X][O][ ]'], #r7
        ['[X][ ][O][ ]', '3', '[X][ ][O][X]'],
        ['[X][ ][ ][O]', '1', '[X][X][ ][O]'], #r8
        ['[X][ ][ ][O]', '2', '[X][ ][X][O]'],
        ['[O][X][ ][ ]', '2', '[O][X][X][ ]'], #r9
        ['[O][X][ ][ ]', '3', '[O][X][ ][X]'],
        ['[ ][X][O][ ]', '0', '[X][X][O][ ]'], #r10
        ['[ ][X][O][ ]', '3', '[ ][X][O][X]'],
        ['[ ][X][ ][O]', '0', '[X][X][ ][O]'], #r11
        ['[ ][X][ ][O]', '2', '[ ][X][X][O]'],
        ['[O][ ][X][ ]', '1', '[O][X][X][ ]'], #r12
        ['[O][ ][X][ ]', '3', '[O][ ][X][X]'],
        ['[ ][O][X][ ]', '0', '[X][O][X][ ]'], #r13
        ['[ ][O][X][ ]', '3', '[ ][O][X][X]'],
        ['[ ][ ][X][O]', '0', '[X][ ][X][O]'], #r14
        ['[ ][ ][X][O]', '1', '[ ][X][X][O]'],
        ['[O][ ][ ][X]', '1', '[O][X][ ][X]'], #r15
        ['[O][ ][ ][X]', '2', '[O][ ][X][X]'],
        ['[ ][O][ ][X]', '0', '[X][O][ ][X]'], #r16
        ['[ ][O][ ][X]', '2', '[ ][O][X][X]'],
        ['[ ][ ][O][X]', '0', '[X][ ][O][X]'], #r17
        ['[ ][ ][O][X]', '1', '[ ][X][O][X]'],
        ['[X][O][ ][X]', '2', '[X][O][O][X]'], #r19
        ['[X][ ][O][X]', '1', '[X][O][O][X]'], #r21
        ['[O][X][X][ ]', '3', '[O][X][X][O]'], #r24
        ['[ ][X][X][O]', '0', '[O][X][X][O]'] #r27
    ]

    accepting = [
        '[X][O][X][ ]', #r18
        '[X][X][O][ ]', #r20
        '[X][X][ ][O]', #r22
        '[X][ ][X][O]', #r23
        '[O][X][ ][X]', #r25
        '[ ][X][O][X]', #r26
        '[ ][O][X][X]', #r29
        '[O][ ][X][X]'  #r28
    ]

    g = FSM.graph(rules, accepting)
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)

    FSM.eval_FSM_IO(rules, accepting)

def gen_ganzenbord():
    res = []
    for i in range(63):
        #print('i: ' + str(i))
        if not ((i/9 == 1) or ((i+4)/9 == 1) or (i == 6) or (i == 42) or (i == 58)):
            for roll in range(1,7):
                #print('r: ' + str(roll))
                n = roll
                n_old = 0
                while(n != n_old):
                    n_old = n
                    if((i+n)/9 == 1) or ((i+n+4)/9 == 1):
                        n = n+roll
                    if((i+n) == 6):
                        n = n+6
                    if((i+n) == 42):
                        n = n-5
                    if((i+n) == 58):
                        n = n-58
                    if((i+n) > 63):
                        n = n - 2*((i+n)-63)
                rule = [i, roll, i+n]
                res.append(rule)
    return res

def ganzenbord():
    rules = gen_ganzenbord()
    accepting = ['63']
    g = FSM.graph(rules, accepting, 'fdp')
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)
    FSM.eval_FSM_rand(rules, accepting, 1, 6)


def game_over_check(board):
    m = board.copy()
    m[m==0] = False
    m[m!=0] = True
    v = np.all(np.logical_and(m, (board == board[0,:])), axis=0)
    h = np.all(np.logical_and(m.T, (board.T == board.T[0,:])), axis=0)
    diag = board.diagonal()
    diag2 = np.fliplr(board).diagonal()
    d = (np.all(diag == diag[0]) and (diag[0]!=0)) or (np.all(diag2 == diag2[0]) and (diag2[0]!=0))
    return np.any(v) or np.any(h) or d


def board_to_string(m):
    res = '<<table border="0">'
    for i in m:
        str = '<tr><td align="text">'
        for j in i:
            if(j == 0): x = ' '
            elif(j == 1): x = 'X'
            else: x = 'O'
            str += '[' + x + ']'
        str += '</td></tr>'
        res += str
    res += '</table>>'
    return res


def gen_tictactoe(n):
    accepting = []
    edges = []
    q = queue.Queue()
    m = np.zeros((n,n))
    q.put(m)
    count = 0
    while(not q.empty()):
        temp = q.get().copy()
        count += 1
        for i in range(n):
            for j in range(n):
                m = temp.copy()
                if(m[i][j] == 0):
                    edge = [board_to_string(m)]
                    c = np.unique(m, return_counts=True)
                    if len(c[1])!=2 and ((len(c[1]) == 1) or (c[1][0] == c[1][2])):
                        m[i][j] = 1
                    else:
                        m[i][j] = -1
                    edge.append(('(' + str(i) + ',' + str(j) + ')'))
                    edge.append(board_to_string(m))
                    edges.append(edge)
                    if(not game_over_check(m)):
                        q.put(m)
                    else:
                        accepting.append(edge[2])
    return edges, accepting


def tictactoe(n):
    t = time.time()
    rules, accepting = gen_tictactoe(n)
    #print(accepting)
    g = FSM.graph(rules, accepting, 'dot')
    g.format = 'bmp'
    print(time.time() - t)
    g.render(directory='graphviz_renders', view=True)
    print(time.time() - t)

#board = np.array([[1,0,0],
#                  [1,-1,1],
#                  [-1,0,0]])

# board = np.array([[1,0],
#                   [-1,0]])

#print(game_over_check(board))
#board_to_string(board)
#odd_a_even_b('abb')
#ganzenbord()
#tictactoe(2)