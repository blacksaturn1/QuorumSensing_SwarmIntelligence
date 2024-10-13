from gridworld import Grid
#from model import Model
import random
# import model
class Agent:
    SusceptibleState = "Susceptible"
    RefractoryState = "Refractory"
    def __init__(self,width, height,index,signalWaveProbability, refractoryTimer,model):
        
        self._height = height
        self._width = width
        self._index = index
        self._state = Agent.SusceptibleState
        self.SIGNAL_WAVE_PROBABILITY=signalWaveProbability
        self.REFRACTORY_TIMER=refractoryTimer
        self._refractoryTimerCountDown=self.REFRACTORY_TIMER
        self.susceptibleStateTimerCount=0
        self.maxSusceptibleStateTimerCount = 1 / self.SIGNAL_WAVE_PROBABILITY
        self.groupSize = 0
        self._initiatedSignal = False
        self.emittingSignal = False
        self.upLeftRightDown= [    [0,-1],
                               [-1,0],     [1,0],
                                    [0,1]
                              ]
        self._model = model
        self.IsDone = False
    
    def IsNeighborEmittingSignal(self):
        x = self._index % self._height
        y = (self._index) // self._height
        for x_delta, y_delta in self.upLeftRightDown:
            index = (y+y_delta)*self._height+(x+x_delta)
            if index>=0 and index < self._height*self._width:
                if self._model.states[index].emittingSignal:
                    return True 

    def step(self):
        
        if self.IsDone==False:
            if self._state==Agent.SusceptibleState:
                self.susceptibleStateTimerCount = self.susceptibleStateTimerCount + 1
                isNeighborEmittingSignal = self.IsNeighborEmittingSignal()
                if isNeighborEmittingSignal:
                    self.emittingSignal = True
                    self._state = Agent.RefractoryState
                    self._refractoryTimerCountDown = self.REFRACTORY_TIMER
                    self.groupSize = self.groupSize + 1
                    self.susceptibleStateTimerCount = 0
                elif not self._initiatedSignal and random.random() < self.SIGNAL_WAVE_PROBABILITY:
                    self.emittingSignal = True
                    self._state = Agent.RefractoryState
                    self._refractoryTimerCountDown = self.REFRACTORY_TIMER
                    self.groupSize = self.groupSize + 1
                    self._initiatedSignal = True
                    self.susceptibleStateTimerCount=0
                
                if self.susceptibleStateTimerCount >= self.maxSusceptibleStateTimerCount:
                    self.IsDone = True
                    print("Size:",self.groupSize)
            else:
                self.emittingSignal = False
                self._refractoryTimerCountDown = self._refractoryTimerCountDown - 1
                if self._refractoryTimerCountDown <=0:
                    self._state= Agent.SusceptibleState
        return

if __name__ == '__main__':
    height = 10
    width = 10
    grid = Grid(width, height, 16, 16, title='Test', margin=1)
    model = model.Model(grid,.5,10)
    agent = Agent(width, height, 13,.5,10,model)
    agent.step()
    