import numpy as np
import time
from plot_utils import ImagePlot

class MazeGame:
    def __init__(self, plot = False):
        self.maze =  np.array([  
                                1,1,0,1,0,1,0,0,0,0,1,1,1,
                                0,1,1,1,0,1,0,0,1,0,0,0,1,
                                0,0,0,1,0,1,1,1,1,1,1,1,1,
                                0,1,1,1,1,1,0,0,1,0,0,0,1,
                                0,0,1,0,0,1,0,1,1,1,0,0,1,
                                0,1,1,0,0,1,0,0,0,0,1,0,0,
                                0,1,0,1,1,1,1,0,1,0,1,1,1,
                                0,1,0,1,0,0,1,0,1,0,0,1,0,
                                0,1,1,0,1,1,1,1,1,1,1,1,0,
                                0,0,1,0,0,1,0,1,0,1,0,1,0,
                                1,1,1,1,0,1,1,0,1,1,0,1,2,        
                                ])
                        

        self.game_plot = ImagePlot('Maze', active=plot)

        self.nRows = 11
        self.nCols = 13
        self.startpos = 0
        self.pos = self.startpos
        self.moveVec = [-self.nCols, self.nCols, 1, -1]        
        self.possibleActions = 4
        self.nStates = self.maze.shape[0]

    def getOpenRoads(self):
        ret = np.array([False, False, False, False])
        #Test up    
        if self.pos >= self.nCols: #Not first row
            if self.maze[self.pos - self.nCols]:
                ret[0] = True
        #Test down
        if self.pos//self.nCols < (self.nRows-1):
            if self.maze[self.pos + self.nCols]:
                ret[1] = True
        #Test right
        if self.pos%self.nCols != (self.nCols-1):
            if self.maze[self.pos+1]:
                ret[2] = True
        #Test left
        if self.pos%self.nCols > 0:
            if self.maze[self.pos-1]:
                ret[3] = True
        return ret

    def win(self):
        return self.maze[self.pos]==2
    
    def plot(self, episode = 0, stepnumber = 0):
        if self.game_plot.active:
           mask = np.zeros_like(self.maze)
           mask[self.pos] = 3           
           step = int(np.round(stepnumber/10.)*10)
           self.game_plot.window_title=f"Episode {episode} Steps: {step}"
           self.game_plot.imshow((self.maze+mask).reshape(self.nRows,self.nCols))
           time.sleep(0.01)
    def getState(self):
        return self.pos
    def move(self, action):
        self.pos += (self.getOpenRoads()*self.moveVec)[action]
        return self.pos
    def restart(self):
        self.pos = self.startpos