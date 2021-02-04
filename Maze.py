import numpy as np
import time
from plot_utils import ImagePlot

class MazeGame:
    def __init__(self, plot = False):
        self.maze =  np.array([  
                                1,1,0,1,0,1,0,0,0,0,4,1,1,
                                0,1,1,1,0,1,0,0,1,0,0,0,1,
                                0,0,0,1,0,1,1,1,1,1,1,1,1,
                                0,1,1,1,1,1,0,0,1,0,0,0,1,
                                0,0,1,0,0,1,0,1,1,1,0,0,1,
                                0,1,1,0,0,1,0,0,0,0,1,0,0,
                                0,1,0,1,1,1,1,0,1,0,1,1,1,
                                0,1,0,1,0,0,1,0,1,0,0,1,0,
                                0,1,1,0,1,1,1,1,1,1,1,1,0,
                                0,0,1,0,0,1,0,1,0,1,0,1,0,
                                5,1,1,1,0,1,1,0,1,1,0,1,2,        
                                ])
                        

        self.game_plot = ImagePlot('Maze', active=plot)

        self.nRows = 11
        self.nCols = 13
        self.startpos = 0
        self.pos = self.startpos
        self.moveVec = [-self.nCols, self.nCols, 1, -1]        
        self.possibleActions = 4
        self.action_space = np.arange(0,self.possibleActions)
        self.nStates = self.maze.shape[0]
        self.playerColor = 3
        self.goals = {4:False, 2: False, 5: False}
        self.goals = {4:False, 2: False}
        self.goals = {2: False}
        
        self.debug=False
    
    def size(self):
            return self.maze.shape[0]
        
    def randomAction(self):
        return np.random.choice(self.action_space)
    
    def checkGoal(self):
        key = self.maze[self.pos]
        if key in self.goals:
            self.goals[key] = True
            print("Found ")
            return True            
        else:
            return False
    def checkGoal2(self):
        maze_val = self.maze[self.pos]
            
        for i,key in enumerate(self.goals.keys()):
            if key != maze_val:
                if self.goals[key] == True:
                    continue
                else:
                    return False
            else:
                self.goals[key] = True                                
                return True            

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
        self.checkGoal2()        
        allTrue = True if False not in self.goals.values() else False
        return allTrue
    
    def plot(self, episode = 0, stepnumber = 0):
        if self.game_plot.active:
           mask = np.zeros_like(self.maze)
           mask[self.pos] = self.playerColor          
           step = int(np.round(stepnumber/10.)*10)
           self.game_plot.window_title=f"Episode {episode} Steps: {step}"           
           self.game_plot.imshow(np.maximum(self.maze,mask).reshape(self.nRows,self.nCols))
           time.sleep(0.01)
    def getState(self):
        return self.pos
    def step(self, action):
        self.pos += (self.getOpenRoads()*self.moveVec)[action]                
        self.checkGoal2()    
        tmp = np.array(list(self.goals.values()))
        #r = tmp[tmp==True].shape[0]/tmp.shape[0]
        r = 1 if self.win() else 0
        return self.pos, r, False
    def reset(self):
        self.pos = self.startpos
        for key in self.goals.keys():
            self.goals[key] = False
            