import examples
import FSM

print('FSM demo')
q = True
while(q):
    op = input('kies demo: \n\t(1) oneven a even b'
                            '\n\t(2) ganzenbord w/o registers'
                            '\n\t(3) ganzenbord w/ registers'
                            '\n\t(4) boter, kaas & eieren 2x2'
                            '\n\t(6) quit')
    if(op == 1): examples.odd_a_even_b(input('input string {a,b}: '))
    elif(op == 2): examples.ganzenbord()
    elif(op == 3): print('WIP')
    elif(op == 4): examples.tictactoe()
    elif(op == 6): q = False
    else: print('invalid input')

