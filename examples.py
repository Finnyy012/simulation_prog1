import queue
import time
import numpy as np
import FSM


def odd_a_even_b(tape):
    """
    stelt rules op voor een FSM die accepting is wanneer de aangeleverde tape een even aantal b's en een oneven
    aantal a's bevat.

    :param tape: input tape ([])
    :return: True wanneer accepting False otherwise (bool)
    """
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

    print(FSM.eval_FSM_tape(rules, tape, accepting))


def tictactoe_old():
    """
    oude functie, wordt niet gebruikt
    """
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
    """
    genereert de regels voor een ganzenbord

    loopt door elke mogelijke positie, en per positie door elke mogelijke roll, om de volgende positie te bepalen

    :return: regels ([[int]])
    """
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
    """
    evalueert en visualiseert de ganzenbord FSM

    genereert eerst de regels met gen_ganzenbord(), en hiermee een graaf om deze af te beelden;
    simuleert vervolgens een spelverloop met willekeurige dobbelsteen worpen
    """
    rules = gen_ganzenbord()
    accepting = ['63']
    g = FSM.graph(rules, accepting, 'fdp')
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)
    FSM.eval_FSM_rand(rules, accepting, 1, 6)


def koffieautomaat():
    """
    evalueert en visualiseert de koffieautomaat FSM

    stelt regels en registers op, visualiseert hiermee de FSM en doorloopt vervolgens het process dmv user input
    """
    reg = [99]
    rules = [
        ['s1','strt','k'],
        ['k','k_f','s1'],
        ['k','k_s','op'],
        ['op','time30','s1'],
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
    FSM.eval_FSM_vending(rules, accepting, reg)


def game_over_check(board):
    """
    checkt of een tictactoe bord gewonnen is

    stelt een matrix op met False voor elke lege positie
    stelt een matrix op met identiteit van een positie aan de bovenste rij
    de AND van deze twee matrices maakt een matrix die True is op elke gevulde positie die gelijk is aan de bovenste rij
    vervolgens wordt van elke kolom de AND genomen. als in de resulterende lijst een True voorkomt,
    heeft die respectievelijke kolom een winnende state.
    hetzelfde wordt gedaan met de transpose van de matrix, om winnende rijen te vinden
    voor de diagonalen wordt elke positie in de diagonaal gelijkgesteld aan de eerste waarde binnen die diagonaal,
    en die waarde ongelijk aan 0 (een lege positie)
    de OR van de resulterende horizontalen, verticalen en diagonalen wordt gereturnd

    voorbeeld voor verticale check
    [[ 1  0  0]     [[1 0 0]      [[1 1 1]     [[1 0 0]
     [ 1 -1  0] ->   [1 1 0]  AND  [1 0 1]  ->  [1 0 0]  -> [1 0 0]
     [ 1 -1  0]]     [1 1 0]]      [1 0 1]]     [1 0 0]]

    :param board: tictactoe bord (np.array)
    :return: game status (bool)
    """
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
    """
    maakt een string van een bord matrix in HTML, zodat graphviz het kan weergeven in een node

    :param m: matrix van bord (np.array)
    :return: html representatie van het bord (str)
    """
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
    """
    genereert alle mogelijke overgangen in een nxn tictactoe spel

    er wordt een queue aangemaakt met een leeg matrix (dus nog voor iemand een zet gedaan heeft).
    vervolgens wordt er in een while loop telkens een board state uit deze queue gehaalt
    om hiermee elke mogelijke volgende zet aan de queue toe te voegen, tot er geen zetten meer zijn en de queue leeg is.

    :param n: dimensies van het bord (int)
    :return: FSM rules ([[str]]), accepting nodes ([str])
    """
    accepting = []
    edges = []
    q = queue.Queue()
    m = np.zeros((n,n))
    q.put(m)
    while(not q.empty()):
        temp = q.get().copy()
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
    """
    visualiseert de tictactoe FSM, en doorloopt een spel met user input

    :param n: dimensies van het bord (int)
    """
    t = time.time()
    rules, accepting = gen_tictactoe(n)
    g = FSM.graph(rules, accepting, 'dot')
    g.format = 'pdf'
    #print(time.time() - t)
    g.render(directory='graphviz_renders', view=True)
    #print(time.time() - t)
    FSM.eval_FSM_IO(rules, accepting)

