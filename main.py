import examples
import FSM

print('FSM demo')
while(True):
    try:
        op = int(input('kies demo: \n\t(1) oneven a even b'
                                '\n\t(2) ganzenbord w/o registers'
                                '\n\t(3) koffieautomaat'
                                '\n\t(4) boter, kaas & eieren 2x2'
                                '\n\t(4) boter, kaas & eieren 3x3 (duurt te lang)'
                                '\n\t(6) quit\n'))
        if (op == 6): break
        elif (op == 1): examples.odd_a_even_b(input('input string {a,b}: '))
        elif (op == 2): examples.ganzenbord()
        elif (op == 3): examples.koffieautomaat()
        elif (op == 4): examples.tictactoe(2)
        elif (op == 4): examples.tictactoe(3)
        else: print('invalid input')
        input("druk op Enter om door te gaan")

    except:
        print('invalid input')



