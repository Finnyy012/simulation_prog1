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


def tictactoe_old():
    rules = [
        ['[ ][ ][ ][ ]', '0', '[X][ ][ ][ ]'],
        ['[ ][ ][ ][ ]', '1', '[ ][X][ ][ ]'],
        ['[ ][ ][ ][ ]', '2', '[ ][ ][X][ ]'],
        ['[ ][ ][ ][ ]', '3', '[ ][ ][ ][X]'],
        ['[X][ ][ ][ ]', '1', '[X][O][ ][ ]'],
        ['[X][ ][ ][ ]', '2', '[X][ ][O][ ]'],
        ['[X][ ][ ][ ]', '3', '[X][ ][ ][O]'],
        ['[ ][X][ ][ ]', '0', '[O][X][ ][ ]'],
        ['[ ][X][ ][ ]', '2', '[ ][X][O][ ]'],
        ['[ ][X][ ][ ]', '3', '[ ][X][ ][O]'],
        ['[ ][ ][X][ ]', '0', '[O][ ][X][ ]'],
        ['[ ][ ][X][ ]', '1', '[ ][O][X][ ]'],
        ['[ ][ ][X][ ]', '3', '[ ][ ][X][O]'],
        ['[ ][ ][ ][X]', '0', '[O][ ][ ][X]'],
        ['[ ][ ][ ][X]', '1', '[ ][O][ ][X]'],
        ['[ ][ ][ ][X]', '2', '[ ][ ][O][X]'],
        ['[X][O][ ][ ]', '2', '[X][O][X][ ]'],
        ['[X][O][ ][ ]', '3', '[X][O][ ][X]'],
        ['[X][ ][O][ ]', '1', '[X][X][O][ ]'],
        ['[X][ ][O][ ]', '3', '[X][ ][O][X]'],
        ['[X][ ][ ][O]', '1', '[X][X][ ][O]'],
        ['[X][ ][ ][O]', '2', '[X][ ][X][O]'],
        ['[O][X][ ][ ]', '2', '[O][X][X][ ]'],
        ['[O][X][ ][ ]', '3', '[O][X][ ][X]'],
        ['[ ][X][O][ ]', '0', '[X][X][O][ ]'],
        ['[ ][X][O][ ]', '3', '[ ][X][O][X]'],
        ['[ ][X][ ][O]', '0', '[X][X][ ][O]'],
        ['[ ][X][ ][O]', '2', '[ ][X][X][O]'],
        ['[O][ ][X][ ]', '1', '[O][X][X][ ]'],
        ['[O][ ][X][ ]', '3', '[O][ ][X][X]'],
        ['[ ][O][X][ ]', '0', '[X][O][X][ ]'],
        ['[ ][O][X][ ]', '3', '[ ][O][X][X]'],
        ['[ ][ ][X][O]', '0', '[X][ ][X][O]'],
        ['[ ][ ][X][O]', '1', '[ ][X][X][O]'],
        ['[O][ ][ ][X]', '1', '[O][X][ ][X]'],
        ['[O][ ][ ][X]', '2', '[O][ ][X][X]'],
        ['[ ][O][ ][X]', '0', '[X][O][ ][X]'],
        ['[ ][O][ ][X]', '2', '[ ][O][X][X]'],
        ['[ ][ ][O][X]', '0', '[X][ ][O][X]'],
        ['[ ][ ][O][X]', '1', '[ ][X][O][X]'],
        ['[X][O][ ][X]', '2', '[X][O][O][X]'],
        ['[X][ ][O][X]', '1', '[X][O][O][X]'],
        ['[O][X][X][ ]', '3', '[O][X][X][O]'],
        ['[ ][X][X][O]', '0', '[O][X][X][O]']
    ]

    accepting = [
        '[X][O][X][ ]',
        '[X][X][O][ ]',
        '[X][X][ ][O]',
        '[X][ ][X][O]',
        '[O][X][ ][X]',
        '[ ][X][O][X]',
        '[ ][O][X][X]',
        '[O][ ][X][X]'
    ]

    g = FSM.graph(rules, accepting)
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)

    FSM.eval_FSM_IO(rules, accepting)


def gen_ganzenbord():
    res = []
    for i in range(63):
        if not ((i/9 == 1) or ((i+4)/9 == 1) or (i == 6) or (i == 42) or (i == 58)):
            for roll in range(1,7):
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


def koffieautomaat():
    reg = [99]
    rules = [
        ['s1','strt','k'],
        ['k','k_f','s1'],
        ['k','k_s','op'],
        ['op','tim','s1'],
        ['op','op_t','t_pay'],
        ['op', 'op_c', 'c_pay'],
        ['c_pay', 'pay_f', 'no_pay'],
        ['c_pay', 'pay_s', 'c'],
        ['c','r0>=01','r0-=01'],
        ['c','r0==00', 'bc'],
        ['bc',' ','s1'],
        ['r0-=01', ' ', 's1'],
        ['t_pay','pay_s','dt'],
        ['t_pay','pay_f','no_pay'],
        ['dt',' ','s1'],
        ['no_pay',' ','s1'],
    ]
    accepting = ['r0-=01','dt']
    g = FSM.graph(rules, accepting, 'dot', 'LR', reg)
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)
    print('q om te stoppen')
    FSM.eval_FSM_vending(rules, accepting, reg)


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
    g.format = 'pdf'
    #print(time.time() - t)
    g.render(directory='graphviz_renders', view=True)
    #print(time.time() - t)
    FSM.eval_FSM_IO(rules, accepting)


#print('r0==00'[4:6])
#koffieautomaat()
