import random
import graphviz


def eval_FSM_tape(rules, tape, accepting):
    """
    Evalueert een FSM aan de hand van een tape.

    Er wordt door alle inputs in de lijst geloopt; bij elke input + state wordt de bijbehorende rule gevonden,
    waarna de state wordt overschreven door de volgende state in deze rule.
    Als er geen bijbehorende rule is, is impliciet een doom state berijkt.
    Alle states en of deze accepting zijn, en de conditie voor de overgang naar de volgende state worden geprint
    True wanneer de final state accepting is, False otherwise

    :param rules: een lijst van rules binnen de FSM; bijvoorbeeld de rule ['A','1','B'] representeerd de edge (A)-1->(B) ([[]])
    :param tape: inputs voor de FSM ([])
    :param accepting: accepting states ([])

    :return: True wanneer de laatste state accepting is, False otherwise (bool)
    """
    state = rules[0][0]
    print(str(state) + ' ' + str(str(state) in accepting))
    i = 0

    for condition in tape:
        doom = True
        print(condition)

        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(str(state) + ' ' + str(str(state) in accepting))
                doom = False
                break

        if(doom):
            print('doom state reached')
            break

        i+=1
        if (i == len(tape)):
            print('tape end reached')

    return state in accepting


def eval_FSM_IO(rules, accepting):
    """
    evalueert de FSM met input van de gebruiker

    Functioneren vergelijkbaar met vorige functie, gebruikt nu alleen input() ipv een tape

    :param rules: rules binnen de FSM ([[]])
    :param accepting: accepting states ([])

    :return: True wanneer de laatste state accepting is, False otherwise (bool)
    """
    state = rules[0][0]
    doom = False
    print(str(state) + ' ' + str(str(state) in accepting))

    while(not doom):
        doom = True
        condition = input('choice: ')
        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(str(state) + ' ' + str(str(state) in accepting))
                doom = False
                break
    print('doom state reached')

    return state in accepting


# evalueert de FSM met willekeurige input
def eval_FSM_rand(rules, accepting, randl, randh):
    """
    evalueert de FSM met input willekeurige input

    Functioneren vergelijkbaar met vorige functie maar dan random.
    Overgangscondities **moeten** integers zijn.

    :param rules: rules binnen de FSM ([[]])
    :param accepting: accepting states ([])
    :param randl: lower limit voor rng (inclusief) (int)
    :param randl: upper limit voor rng (inclusief) (int)

    :return: True wanneer de laatste state accepting is, False otherwise (bool)
    """
    state = rules[0][0]
    doom = False
    print(str(state) + ' ' + str(str(state) in accepting))

    while(not doom):
        doom = True
        condition = random.randint(randl, randh)
        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(condition)
                print(str(state) + '\t' + str(str(state) in accepting))
                doom = False
                break
    print('doom state reached')

    return state in accepting


def update_reg(reg, node):
    """
    hulpfunctie voor eval_FSM_vending

    updatet de registers aan de hand van de node label e.g. bij 'r0+=1' gaat de register op positie 0 in de lijst 1 omhoog

    :param reg: registers ([int])
    :param node: node label (str)
    :return: geüpdatete registers ([int])
    """
    if(len(node)==6):
        if(node[2:4] == '+='):
            reg[int(node[1])] += int(node[4:6])
            print('r' + node[1] + ':\t' + str(reg[int(node[1])]))
        elif(node[2:4] == '-='):
            reg[int(node[1])] -= int(node[4:6])
            print('r' + node[1] + ':\t' + str(reg[int(node[1])]))
        elif(node[2:4] == '= '):
            reg[int(node[1])] = int(node[4:6])
            print('r' + node[1] + ':\t' + str(reg[int(node[1])]))
    return reg


def eval_FSM_vending(rules: [], accepting, registers):
    state = rules[0][0]
    print('machine state: ' + str(state))

    while(True):
        check = True
        while(check):
            check = False
            for rule in rules:
                #print(str(rule[0]) + ' ' + str(len(rule[1]) == 6) + ' ' + str(rule[1][2]))
                if((state == rule[0]) and (len(rule[1])==6) and
                        ((rule[1][2] == '>') or (rule[1][2] == '<') or (rule[1][2] == '='))):
                    r = int(rule[1][1])
                    c = int(rule[1][4:6])
                    #print(str(r) + ' ' + str(c) + ' ' + str(registers[r]))
                    #print(str(rule[1][2:4]))
                    if((rule[1][2:4] == '>=') and (registers[r] >= c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break
                    if((rule[1][2:4] == '<=') and (registers[r] <= c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break
                    if((rule[1][2:4] == '==') and (registers[r] == c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break
                    if((rule[1][2:4] == '!=') and (registers[r] != c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break
                    if((rule[1][2:4] == '> ') and (registers[r] > c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break
                    if((rule[1][2:4] == '> ') and (registers[r] > c)):
                            state = rule[2]
                            check = True
                            print('condition:\t' + str(rule[1]) + '\nstate:\t' + str(state))
                            registers = update_reg(registers, state)
                            break

        c = False
        for rule in rules:
            if ((state == rule[0]) and (rule[1]) == ' '):
                print('druk op Enter om door te gaan')
                c = True
                c_state = rule[2]

        condition = input('choice: ')
        if(condition == 'q'): break

        if(not c):
            for rule in rules:
                if((state == rule[0]) and (condition == rule[1])):
                    state = rule[2]
                    print('state:\t' + str(state))
                    break
        else:
            state = c_state
            print('state:\t' + str(state))

    return state in accepting


def graph(rules, accepting, layout='dot', rankdir='TB', registers=None):
    """
    maakt een Digraph object van een FSM

    loopt door alle rules heen en voegt een edge toe per loop;
    houdt een lijst van nodes bij en voegt een node toe wanneer deze nog niet in de lijst zit;
    wanneer een node in accepting zit krijgt deze een dubbele ring

    :param rules: rules binnen de FSM ([[]])
    :param accepting: accepting states ([])
    :param layout: layout engine, default='dot' (str)
        - 'dot'      hierarchical/layered graph
        - 'neato'    spring model
        - 'fdp'      force-directed placement
        - 'circo'    circular graph
    :param rankdir: layout direction, alleen voor 'dot', default='TB' (str)
    :param registers: registers voor als de FSM informatie moet bijhouden, default=None ([int])
    :return: directed graph object van FSM (graphviz.Digraph)
    """

    res = graphviz.Digraph('FSM')
    res.graph_attr['layout'] = layout
    if(layout=='dot'):
        res.graph_attr['rankdir'] = rankdir

    nodes = {}
    n_node = 0

    if(registers is not None):
        regl = '<<table border="0">'
        for i in range(len(registers)):
            regl += '<tr><td align="text">r' + str(i) + '=' + str(registers[i]) + '</td></tr>'
        regl += '</table>>'
        res.node('R', regl, shape='box', fontname='Consolas')

    # start = rules[0][0]
    # for rule in rules:
    #     if(start in rule):
    #         if(start == rule[0]):
    #             rule[0] = '>' + str(rule[0])
    #         if(start == rule[2]):
    #             rule[2] = '>' + str(rule[2])

    for rule in rules:
        node_pair = (str(rule[0]), str(rule[2]))

        for node in node_pair:
            if node not in nodes:
                nodes[node] = str(n_node)
                n_node+=1
                if node not in accepting:
                    res.node(nodes[node], node, shape='circle', fontname='Consolas')
                else:
                    res.node(nodes[node], node, shape='doublecircle', fontname='Consolas')

        res.edge(nodes[node_pair[0]], nodes[node_pair[1]], label=str(rule[1]), fontname='Consolas')
    return res


def test_layout(s):
    """
    test functie
    """

    g = graphviz.Digraph('FSM')
    g.node('A', s, shape='circle', fontname='Consolas')
    g.node('B', '<bbbbb>', shape='circle')
    g.edge('A', 'B', 'a->b')
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)
