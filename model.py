
from gridworld import Grid
import random
from agent import Agent

class Model:
    def __init__(self, grid:Grid,probability, refractoryTimer):
        self.__width = grid.height  # Width and height in number of cells
        self.__height = grid.width
        self.grid = grid
        self.sim_runs=0
        self.upLeftRightDown= [    [0,-1],
                               [-1,0],     [1,0],
                                    [0,1]
                              ]
        self.P=probability
        self.LEN = self.__height * self.__width
        self.REFRACTORY_TIMER = 10
        self.states = [Agent(self.__width,self.__height,index,self.P,self.REFRACTORY_TIMER,self) for index in range(self.LEN)]
        #self.c=[random.random()*self.T for x in range(self.T)]
        a=1
     
     
    def setup(self):
        for y in range(self.__height):        
            for x in range(self.__width):
                self.grid[x,y]='O'
        self.printStats()

    def printStats(self):    
        xCount=0
        oCount=0
        total=0
        for y in range(self.__height):        
            for x in range(self.__width):
                total+=1
                if self.grid[x,y]=='X':
                    xCount+=1
                if self.grid[x,y]=='O':
                    oCount+=1
        print("total:",total)
        print("X %:",xCount/total*100)

        print("O %:",oCount/total*100)

                    
    
   
        
    def run_sim(self):
        BLACK = (0, 0, 0)

        # if self.sim_runs==self.T:
        #     return
  
        for y in range(self.__height):        
            for x in range(self.__width):
                index = y*self.__height+x
                # self.c[index]=self.c[index]+1
                agent = self.states[index]
                agent.step()
                if agent.emittingSignal:
                    self.grid[x,y]="X"
                else:
                    self.grid[x,y]="O"
                

        self.sim_runs+=1

        print("Simulation:",self.sim_runs)

        # if self.sim_runs==self.T:
        #     self.printStats()
    
    
