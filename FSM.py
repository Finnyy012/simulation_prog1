import math
import random
import numpy as np
import graphviz


# evalueert de FSM dmv tape input
def eval_FSM_tape(rules: [], tape: [], accepting):
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


# evalueert de FSM met input van de gebruiker
def eval_FSM_IO(rules: [], accepting):
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
def eval_FSM_rand(rules: [], accepting, randl, randh):
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
                break

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
            break

    return state in accepting


# visualiseert de graaf
def graph(rules, accepting, layout='dot', rankdir='TB', registers=None):
    res = graphviz.Digraph('FSM')
    res.graph_attr['layout'] = layout   #'dot'      hierarchical/layered/directed graph
                                        #'neato'    spring model
                                        #'fdp'      force-directed placement
                                        #'circo'    circular graph
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
    g = graphviz.Digraph('FSM')
    g.node('A', s, shape='circle', fontname='Consolas')
    g.node('B', '<bbbbb>', shape='circle')
    g.edge('A', 'B', 'a->b')
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)
