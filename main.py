import math
import numpy as np
import graphviz

#evalueert de FSM
def eval_FSM(rules: [], tape: [], accepting):
    state = rules[0][0]
    for condition in tape:
        print(condition)
        for rule in rules:
            if((state == rule[0]) and (condition == rule[1])):
                state = rule[2]
                print(str(state) + ' ' + str(state in accepting))
                break
    return state in accepting

##visualiseert de graaf
def graph(rules, accepting):
    dot = graphviz.Digraph('FSM')
    dot.graph_attr['rankdir'] = 'LR'
    nodes = {}
    n_node = 65

    start = rules[0][0]
    for rule in rules:
        if(start in rule):
            if(start == rule[0]):
                rule[0] = '>' + str(rule[0])
            if(start == rule[2]):
                rule[2] = '>' + str(rule[2])
    print(rules)

    for rule in rules:
        node1 = str(rule[0])
        node2 = str(rule[2])

        if(node1 not in nodes):
            nodes[node1] = chr(n_node)
            n_node+=1
            if(node1 not in accepting):
                dot.node(nodes[node1], node1)
            else:
                dot.node(nodes[node1], node1, shape='doublecircle')

        if(node2 not in nodes):
            nodes[node2] = chr(n_node)
            n_node += 1
            if(node2 not in accepting):
                dot.node(nodes[node2], node2)
            else:
                dot.node(nodes[node2], node2, shape='doublecircle')

        dot.edge(nodes[node1], nodes[node2], label=str(rule[1]))
    return dot

##string w/ oneven 'a' en even 'b'
def test1():
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
    tape = ['a','b','b']

    g = graph(rules, accepting)
    print(g.source)
    g.format = 'pdf'
    g.render(directory='graphviz_renders', view=True)

    print(eval_FSM(rules, tape, accepting))

