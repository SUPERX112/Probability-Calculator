import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**args):
        self.contents=[]
        self.ball=[]
        self.contents_draw=[]
        
        for key in args:     #add balls
            value=args[key]
            for x in range(0,value):
                self.contents.append(key)
                self.ball.append(key)

    def draw(self, number):
        self.contents_draw=[]
        self.contents=[]
        for elem in self.ball:
            self.contents.append(elem)
            
        if number >= len(self.contents):
            self.contents_draw=self.contents
            return self.contents
        
        for x in range(0,number):
            num=random.randint(0,len(self.contents)-1)
            self.contents_draw.append(self.contents[num])
            del self.contents[num]
        
        return self.contents_draw
            
            

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N=num_experiments
    M=0
    for ex in range(0,N):
        present=[]       #Check if there is the right number of items
        hat.draw(num_balls_drawn)
        for elem in expected_balls:
            count=0
            if count_how_many(elem,hat.contents_draw)>=expected_balls[elem]:
                present.append(10)        #10 is a marker
            for elem in present:
                if elem==10:                #10 is a marker
                    count+=1
            if count==len(expected_balls):
                M+=1
    return M/N

def count_how_many(value, arr):       #Check how many times the value in the list
    count=0
    for elem in arr:
        if value==elem:
            count+=1
    return count
