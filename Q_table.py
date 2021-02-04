# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 20:47:30 2021

@author: arasps
"""
import numpy as np
import time
from PyQt5 import QtGui
from Maze import MazeGame

#Setup random seed
np.random.seed(2)

game = MazeGame(plot=True)


Q = np.zeros((game.nStates,game.possibleActions))

lr = .9
y = .9

num_episodes=2000
max_tries = 100000

nsteps = []


for i in range(num_episodes):    
    n=0
    startTime = time.time()
    game.reset()
    while not game.win() and n < max_tries:                                
        game.plot(i,n)        
        n+=1
        state = game.getState()
        action = np.argmax(Q[state,:] + np.random.randn(1,game.possibleActions)*(1./(i+1)))     
        newstate, r = game.step(action)
        #Update Q-Table with new knowledge        
        Q[state,action] = Q[state,action] + lr*(r + y*np.max(Q[newstate,:]) - Q[state,action])        
    nsteps.append(n)
        
    if len(nsteps) > 20 and (np.max(nsteps[-10:-1])-np.min(nsteps[-10:-1]))<3:
        break
    endTime = time.time() - startTime
    if n < max_tries:
        print(f"Epoch {i}: Found exit after {n} steps. Time: {endTime}")
    else:
        print(f"Epoch {i}: Can't find way, restarting.")
QtGui.QApplication.closeAllWindows()
    
    
