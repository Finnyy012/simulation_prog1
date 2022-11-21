import math
import numpy as np
import graphviz

#evalueert de FSM dmv tape input
def eval_FSM(rules: [], tape: [], accepting):
    state = rules[0][0]
    print(str(state) + ' ' + str(state in accepting))
    i = 0

    for condition in tape:
        doom = True
        print(condition)

        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(str(state) + ' ' + str(state in accepting))
                doom = False
                break

        if(doom):
            print('doom state reached')
            break

        i+=1
        if (i == len(tape)):
            print('tape end reached')

    return state in accepting

#evalueert de FSM dmv input van de gebruiker
def eval_FSM_IO(rules: [], accepting):
    state = rules[0][0]
    doom = False
    print(str(state) + ' ' + str(state in accepting))

    while(True):
        doom = True
        condition = input('choice: ')
        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(str(state) + ' ' + str(state in accepting))
                doom = False
                break
        if(doom):
            print('doom state reached')
            break

    return state in accepting

##visualiseert de graaf
def graph(rules, accepting, layout='dot'):

    res = graphviz.Digraph('FSM')
    res.graph_attr['layout'] = layout   #'dot'      hierarchical/layered/directed graph
                                        #'neato'    spring model
                                        #'fdp'      force-directed placement
                                        #'circo'    circular graph
    nodes = {}
    n_node = 65

    start = rules[0][0]
    for rule in rules:
        if(start in rule):
            if(start == rule[0]):
                rule[0] = '>' + str(rule[0])
            if(start == rule[2]):
                rule[2] = '>' + str(rule[2])

    for rule in rules:
        #print(rule)
        node1 = str(rule[0])
        node2 = str(rule[2])

        if(node1 not in nodes):
            nodes[node1] = chr(n_node)
            n_node+=1
            if(n_node==91): n_node=97
            if(node1 not in accepting):
                res.node(nodes[node1], node1, shape='circle')
            else:
                res.node(nodes[node1], node1, shape='doublecircle')

        if(node2 not in nodes):
            nodes[node2] = chr(n_node)
            n_node+=1
            if (n_node == 91): n_node = 97
            if(node2 not in accepting):
                res.node(nodes[node2], node2, shape='circle')
            else:
                res.node(nodes[node2], node2, shape='doublecircle')

        res.edge(nodes[node1], nodes[node2], label=str(rule[1]))
    return res
