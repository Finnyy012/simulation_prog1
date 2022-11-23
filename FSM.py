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

# visualiseert de graaf
def graph(rules, accepting, layout='dot'):
    res = graphviz.Digraph('FSM')
    res.graph_attr['layout'] = layout   #'dot'      hierarchical/layered/directed graph
                                        #'neato'    spring model
                                        #'fdp'      force-directed placement
                                        #'circo'    circular graph
    nodes = {}
    n_node = 0

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
