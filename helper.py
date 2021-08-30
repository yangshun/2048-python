import numpy as np
import math

import logic
import constants as c



#The depth that the algorithm will be search to find the best move(default 2, if you want more accurate prediction will be take more time)
MAX_DEPTH = 2


#Help function that call the necessary function
def get_help(board):
    best_move = determine_next_move(board)
    return best_move


#The heuristic function to calculate how good is a certain state of the board
def heuristic_value(board):
    heuristic_value = 0
    for i in range(0, c.GRID_LEN):
        for j in range(0, c.GRID_LEN):
            heuristic_value += math.pow(board[0][1], 3)
    return heuristic_value

    
    

#This function check if two boards are the same
def boardsEquality(board_1, board_2):
    for i in range(0, c.GRID_LEN):
        for j in range(0, c.GRID_LEN):
            if board_1[i][j] != board_2[i][j]:
                return False
    return True


#Recursion, simulating out every possible human and computer move for a certain number of steps
def calculate_move_score(board, currDepth, depthLimit):
    bestScore = 0
    moves = ['RIGHT', 'UP', 'LEFT', 'DOWN']
    for m in moves:
        if m == 'RIGHT':
            newBoard, done= logic.right(board)
        if m == 'UP':
            newBoard, done= logic.up(board)
        if m == 'LEFT':
            newBoard, done= logic.left(board)
        if m == 'DOWN':
            newBoard, done= logic.down(board)
        if not boardsEquality(newBoard, board):
            score = generate_score(newBoard, currDepth + 1, depthLimit)
            bestScore = max(score, bestScore)
    return bestScore





#Recursion, simulating out every possible human and computer move for a certain number of steps
def generate_score(board, currDepth, depthLimit):
    if currDepth >= depthLimit:
        return heuristic_value(board)

    totalScore = 0
    for i in range(0, c.GRID_LEN):
        for j in range(0, c.GRID_LEN):
            if board[i][j] == 0:
                newBoard2 = board
                newBoard2[i][j] = 2
                moveScore2 = calculate_move_score(newBoard2, currDepth, depthLimit)
                totalScore += 0.9*moveScore2

                newBoard4 = board
                newBoard4[i][j] = 4
                moveScore4 = calculate_move_score(newBoard4, currDepth, depthLimit)
                totalScore += 0.1*moveScore4
    return totalScore


#In this function calculated the score after a move
def calculate_score(board, move):
    if move == 'RIGHT':
        newBoard, done= logic.right(board)
    if move == 'UP':
        newBoard, done= logic.up(board)
    if move == 'LEFT':
        newBoard, done= logic.left(board)
    if move == 'DOWN':
        newBoard, done= logic.down(board)

    if boardsEquality(newBoard, board):
        return 0
    return generate_score(newBoard, 0, MAX_DEPTH)




def determine_next_move(board):
    bestMove = ''
    bestScore = 0
    moves = ['RIGHT', 'UP', 'LEFT', 'DOWN']
    for m in moves:
        score = calculate_score(board, m)
        if score > bestScore:
            bestScore = score
            bestMove = m
    return bestMove








