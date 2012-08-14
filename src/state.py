screen_states = []

class GameState():
    
    """ Game state manages a group of display objects and an update loop""" 
    def __init__(self):
        screen_states = []
        
    def clear(self):
        screen_states = []
        
    def add_state(self, gstate):
        screen_states.append(gstate)
        
    def remove_state(self, gstate):
        for gs in screen_states:
           if gs == gstate:
               screen_states.remove(gs)
                  
    def update(self):
        for s_state in screen_states:
            s_state.update()
        


