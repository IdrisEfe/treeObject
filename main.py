import pandas as pd


class Deneyap:
    
    def __init__(self, names, teams, points):
        
        self.names = names
        self.teams = teams
        self.points = points
        self.names = self.reverse(names)
        self.teams = self.reverse(teams)
        self.points = self.reverse(points)
        
        self.myDict = {'names': self.names,
                       'teams': self.teams,
                       'points': self.points}
        
        self.myFrame = pd.DataFrame(self.myDict)
        print(self.myFrame)
        
    def reverse(self, obj):
        
        self.obj = obj
        self.new_obj = obj[::-1]
        return self.new_obj
    
if __name__ == '__main__':
    
    thing = None
    names = []
    teams = []
    points = []
    
    while thing != "0":
        thing = input('Enter a name (Enter zer0 (0) if you want to quit)')
        if thing != "0":
            names.append(thing)
        
    thing = None
    
    
    while thing != "0":
        thing = input('Enter a team (Enter zer0 (0) if you want to quit)')
        if thing != "0":
            teams.append(thing)
    
    thing = None
        
    while thing != "0":
        thing = input('Enter a point (Enter zer0 (0) if you want to quit)')
        if thing != "0":
            points.append(thing)
        
    app = Deneyap(names, teams, points)
    
    
    
        
        
    

        
        
        
