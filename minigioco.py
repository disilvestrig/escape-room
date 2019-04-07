import os
import random
from random import  choice
class minigame:

    # variabili globali
    CPU = 1
    USER = 0
    SYMBOLS = ['O', 'X']
    BOARD = [ [' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' '] ]

    def drawBoard():
        """ Disegna la tavola di gioco"""
        
        # Pulisce lo schermo
        SYMBOLS = minigame.SYMBOLS
        USER = minigame.USER
        CPU = minigame.CPU   
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        
        # disegna la lavagna
        print("    0   1   2");
        print("  -------------");
        print("0 | %c | %c | %c |" % (minigame.BOARD[0][0], minigame.BOARD[0][1], minigame.BOARD[0][2]));
        print("  -------------");
        print("1 | %c | %c | %c |" % (minigame.BOARD[1][0], minigame.BOARD[1][1], minigame.BOARD[1][2]));
        print("  -------------");
        print("2 | %c | %c | %c |" % (minigame.BOARD[2][0], minigame.BOARD[2][1], minigame.BOARD[2][2]));
        print("  -------------");
        print ("USER is: %c" % SYMBOLS[USER])
        print ("CPU is:  %c" % SYMBOLS[CPU])

    def setCellAt(coords, symbol):
        BOARD = minigame.BOARD
        """ mette nella cella identificata con le coordinate con il valore del simbolo """
        BOARD[coords['x']][coords['y']] = symbol

    def getMoveFrom(playerType):
        USER = minigame.USER
        coord = {}
        if playerType == USER :
            validCoord = False
            while not validCoord:
                # inserisci la riga
                print("Row[0-2]: ")
                row = input()
                if row == "":
                    continue;
                else:
                    row = int(row)
            
                # inserisci la colonna
                print("Col[0-2]: ")
                col = input()
                if col == "":
                    continue
                else:
                    col = int(col)
            
                #se le coordinate non sono giuste le richiede
                coord = [row, col]
                avalaibleCoords = minigame.getAllPossibleMove()
            
                if coord in avalaibleCoords:
                    validCoord = True
            
                else:
                    print ("Input sbagliato! Righe e colonne devono essere tra 0 e 2")

            
            coord = {'x': row, 'y': col}
        else :
            coord = minigame.IA()
        return coord
    

    def IA():
        BOARD = minigame.BOARD
        SYMBOLS = minigame.SYMBOLS
        moves = []
        avalaibleCoords = minigame.getAllPossibleMove()
        if BOARD[0][0] == BOARD[0][2] == SYMBOLS[0] and [0,1] in avalaibleCoords:
            moves.append([0,1])
        elif BOARD[0][0] == BOARD[2][0] == SYMBOLS[0] and [1,0] in avalaibleCoords:
            moves.append([1,0])
        elif BOARD[0][0] == BOARD[2][2] == SYMBOLS[0] and [1,1] in avalaibleCoords:
            moves.append([1,1])
        elif BOARD[0][1] == BOARD[2][1] == SYMBOLS[0] and [1,1] in avalaibleCoords:
           moves.append([1,1])
        elif BOARD[0][2] == BOARD[2][0] == SYMBOLS[0] and [1,1] in avalaibleCoords:
           moves.append([1,2])
        elif BOARD[0][2] == BOARD[2][2] == SYMBOLS[0] and [1,2] in avalaibleCoords:
           moves.append([1,2])
        elif BOARD[1][0] == BOARD[1][2] == SYMBOLS[0] and [1,1] in avalaibleCoords:
           moves.append([1,1])
        elif BOARD[2][2] == BOARD[2][0] == SYMBOLS[0] and [2,1] in avalaibleCoords:
            moves.append([1,0])    
        elif BOARD[0][0] == BOARD[0][1] == SYMBOLS[0] and [0,2] in avalaibleCoords:
            moves.append([0,2])
        elif BOARD[0][0] == BOARD[1][0] == SYMBOLS[0] and [2,0] in avalaibleCoords:
            moves.append([2,0])
        elif BOARD[0][0] == BOARD[1][1] == SYMBOLS[0] and [2,2] in avalaibleCoords:
            moves.append([2,2])
        elif BOARD[0][1] == BOARD[0][2] == SYMBOLS[0] and [0,0] in avalaibleCoords:
            moves.append([0,0])
        elif BOARD[0][1] == BOARD[1][1] == SYMBOLS[0] and [2,1] in avalaibleCoords:
            moves.append([2,1])
        elif BOARD[0][2] == BOARD[1][1] == SYMBOLS[0] and [2,0] in avalaibleCoords:
            moves.append([2,0])
        elif BOARD[0][2] == BOARD[1][2] == SYMBOLS[0] and [2,2] in avalaibleCoords:
            moves.append([2,2])
        elif BOARD[1][0] == BOARD[2][0] == SYMBOLS[0] and [0,0] in avalaibleCoords:
            moves.append([0,0])
        elif BOARD[1][0] == BOARD[1][1] == SYMBOLS[0] and [1,2] in avalaibleCoords:
            moves.append([1,2])
        elif BOARD[1][1] == BOARD[1][2] == SYMBOLS[0] and [1,0] in avalaibleCoords:
            moves.append([1,0])
        elif BOARD[1][1] == BOARD[2][0] == SYMBOLS[0] and [0,2] in avalaibleCoords:
            moves.append([0,2])
        elif BOARD[1][1] == BOARD[2][1] == SYMBOLS[0] and [0,1] in avalaibleCoords:
            moves.append([0,1])
        elif BOARD[1][1] == BOARD[2][2] == SYMBOLS[0] and [0,0] in avalaibleCoords:
            moves.append([0,0])
        elif BOARD[1][2] == BOARD[2][2] == SYMBOLS[0] and [0,2] in avalaibleCoords:
            moves.append([0,2])
        elif BOARD[2][0] == BOARD[2][1] == SYMBOLS[0] and [2,2] in avalaibleCoords:
            moves.append([2,2])
        elif BOARD[2][1] == BOARD[2][2] == SYMBOLS[0] and [2,0] in avalaibleCoords:
            moves.append([2,0])

        moves1 = []

        if BOARD[0][0] == BOARD[0][2] == SYMBOLS[1] and [0,1] in avalaibleCoords:
            moves1.append([0,1])
        elif BOARD[0][0] == BOARD[2][0] == SYMBOLS[1] and [1,0] in avalaibleCoords:
            moves1.append([1,0])
        elif BOARD[0][0] == BOARD[2][2] == SYMBOLS[1] and [1,1] in avalaibleCoords:
            moves1.append([1,1])
        elif BOARD[0][1] == BOARD[2][1] == SYMBOLS[1] and [1,1] in avalaibleCoords:
            moves1.append([1,1])
        elif BOARD[0][2] == BOARD[2][0] == SYMBOLS[1] and [1,1] in avalaibleCoords:
            moves1.append([1,2])
        elif BOARD[0][2] == BOARD[2][2] == SYMBOLS[1] and [1,2] in avalaibleCoords:
            moves1.append([1,2])
        elif BOARD[1][0] == BOARD[1][2] == SYMBOLS[1] and [1,1] in avalaibleCoords:
            moves1.append([1,1])
        elif BOARD[2][2] == BOARD[2][0] == SYMBOLS[1] and [2,1] in avalaibleCoords:
            moves1.append([1,0])    
        elif BOARD[0][0] == BOARD[0][1] == SYMBOLS[1] and [0,2] in avalaibleCoords:
            moves1.append([0,2])
        elif BOARD[0][0] == BOARD[1][0] == SYMBOLS[1] and [2,0] in avalaibleCoords:
            moves1.append([2,0])
        elif BOARD[0][0] == BOARD[1][1] == SYMBOLS[1] and [2,2] in avalaibleCoords:
            moves1.append([2,2])
        elif BOARD[0][1] == BOARD[0][2] == SYMBOLS[1] and [0,0] in avalaibleCoords:
            moves1.append([0,0])
        elif BOARD[0][1] == BOARD[1][1] == SYMBOLS[1] and [2,1] in avalaibleCoords:
            moves1.append([2,1])
        elif BOARD[0][2] == BOARD[1][1] == SYMBOLS[1] and [2,0] in avalaibleCoords:
            moves1.append([2,0])
        elif BOARD[0][2] == BOARD[1][2] == SYMBOLS[1] and [2,2] in avalaibleCoords:
            moves1.append([2,2])
        elif BOARD[1][0] == BOARD[2][0] == SYMBOLS[1] and [0,0] in avalaibleCoords:
            moves1.append([0,0])
        elif BOARD[1][0] == BOARD[1][1] == SYMBOLS[1] and [1,2] in avalaibleCoords:
            moves1.append([1,2])
        elif BOARD[1][1] == BOARD[1][2] == SYMBOLS[1] and [1,0] in avalaibleCoords:
            moves1.append([1,0])
        elif BOARD[1][1] == BOARD[2][0] == SYMBOLS[1] and [0,2] in avalaibleCoords:
            moves1.append([0,2])
        elif BOARD[1][1] == BOARD[2][1] == SYMBOLS[1] and [0,1] in avalaibleCoords:
            moves1.append([0,1])
        elif BOARD[1][1] == BOARD[2][2] == SYMBOLS[1] and [0,0] in avalaibleCoords:
            moves1.append([0,0])
        elif BOARD[1][2] == BOARD[2][2] == SYMBOLS[1] and [0,2] in avalaibleCoords:
            moves1.append([0,2])
        elif BOARD[2][0] == BOARD[2][1] == SYMBOLS[1] and [2,2] in avalaibleCoords:
            moves1.append([2,2])
        elif BOARD[2][1] == BOARD[2][2] == SYMBOLS[1] and [2,0] in avalaibleCoords:
            moves1.append([2,0])

        if len(moves) == 0 and len(moves1) == 0:
            a = random.randint(0,2)
            b = random.randint(0,2)
            while [a,b] not in avalaibleCoords:
                a = random.randint(0,2)
                b = random.randint(0,2)
            coord = {"x": a,"y":b}
        else:
            if len(moves1) == 0: 
                move = choice(moves)
                coord = {"x":move[0],"y":move[1]}
            else:
                move = choice(moves1)
                coord = {"x":move[0],"y":move[1]}

        return coord


        
    def getAllPossibleMove(board = BOARD):
        """Calcola tutte le mosse possibili e le restituisce """
        coords = []
    
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == ' ':
                    coords.append([i, j])
                
        return coords       
    
    def isFinished():
        BOARD = minigame.BOARD
        """ Restituisce True se la tavola è completa,altrimenti False """
        emptyCells = 0
    
        for i in range(0,3):
            for j in range(0,3):
                if BOARD[i][j] == ' ':
                    emptyCells += 1

        return (emptyCells == 0)
    
    def checkForWinner(board):
        """ Return the symbol of the winner """
        USER = minigame.USER
        CPU = minigame.CPU
        SYMBOLS = minigame.SYMBOLS
        if minigame.checkWin(board, USER):
            return SYMBOLS[USER]
        elif minigame.checkWin(board, CPU):
            return SYMBOLS[CPU]
        else:
            if minigame.isFinished():
                return '-'
        return ''
    
    def checkWin(board, player):
        SYMBOLS = minigame.SYMBOLS
        """ Return True if the player is the winner, false otherwise """
        sym = SYMBOLS[player]
        if (board[0][0] == sym and board[0][1] == sym and board[0][2] == sym) or \
           (board[1][0] == sym and board[1][1] == sym and board[1][2] == sym) or \
           (board[2][0] == sym and board[2][1] == sym and board[2][2] == sym):
            return True
        elif (board[0][0] == sym and board[1][0] == sym and board[2][0] == sym) or \
             (board[0][1] == sym and board[1][1] == sym and board[2][1] == sym) or \
             (board[0][2] == sym and board[1][2] == sym and board[2][2] == sym):
            return True
        elif (board[0][0] == sym and board[1][1] == sym and board[2][2] == sym) or \
             (board[0][2] == sym and board[1][1] == sym and board[2][0] == sym):
            return True
        else:
            return False
    
    def initGame():
        """ Inizia il gioco, chiede all' utente che simbolo vuole usare. """
        SYMBOLS = minigame.SYMBOLS

        print ("Ciao, vuoi essere 'O' o 'X' (default 'O')?")
        choice = input()
        choice = choice.upper()
        while choice != "X" and choice != "O":
            choice = input()
            choice = choice.upper()


        if choice == 'X':
            SYMBOLS[0] = 'X'
            SYMBOLS[1] = 'O'
        else:
            SYMBOLS[0] = 'O'
            SYMBOLS[1] = 'X'
    def gameLoop():
        """ Crea il loop finchè il gioco non finisce """
        SYMBOLS = minigame.SYMBOLS
        USER = minigame.USER
        CPU = minigame.CPU
        BOARD = minigame.BOARD
        minigame.initGame()

        finished = False
        curPlayer = USER
        while not finished:
            minigame.drawBoard()
            winner = minigame.checkForWinner(BOARD)
            if winner in SYMBOLS:
                if winner == SYMBOLS[USER]:
                    winner = "Il player"
                else:
                    winner = "Il giullare"
                    
                print ("%s ha vinto!" % winner) 
                finished = True
            elif winner == '-':
                print ("Pareggio!")
                finished = True
            else:
                minigame.setCellAt(minigame.getMoveFrom(curPlayer), SYMBOLS[curPlayer])
                if curPlayer == USER:
                    curPlayer = CPU
                else:
                    curPlayer = USER

    # Parte il gioco...