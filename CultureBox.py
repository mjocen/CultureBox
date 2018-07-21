import random
class Shuffler:
    
    def __init__(self, insults, compliments):
        self.insults = insults
        self.compliments = compliments
        self.insultsCounter = 0
        self.complimentsCounter = 0
        self.firstInsult = insults[0]
        self.firstCompliment = compliments[0]
        self.complimentEvents = 0
        self.insultEvents = 0
        self.totalEvents = 0
        
    def shuffle(self, textList):
        return random.shuffle(textList)
        
        
    def randomInsults(self):
        if self.insultsCounter == 0:
            if self.insults[0] == self.firstInsult:
                self.shuffle(self.insults)
                return self.insults[self.insultsCounter]
        else:
            if self.insultsCounter >= len(self.insults):
                self.firstInsult = self.insults[0]
                self.insultsCounter = 0
                self.shuffle(self.insults)
                return self.insults[self.insultsCounter]
            else:
                return self.insults[self.insultsCounter]
            
    def randomCompliments(self):
        if self.complimentsCounter == 0:
            if self.compliments[0] == self.firstCompliment:
                self.shuffle(self.compliments)
                return self.compliments[self.complimentsCounter]
        else:
            if self.complimentsCounter >= len(self.compliments):
                self.firstCompliment = self.compliments[0]
                self.complimentsCounter = 0
                self.shuffle(self.compliments)
                return self.compliments[self.complimentsCounter]
            else:
                return self.compliments[self.complimentsCounter]
            
    def identifyText(self):
        randomChoice = random.randint(0,1)
        if randomChoice == 0:
            textChoice = self.randomInsults()
            self.insultsCounter += 1
            self.insultEvents += 1
        else:
            textChoice = self.randomCompliments()
            self.complimentsCounter += 1
            self.complimentEvents += 1
            
            
        self.totalEvents += 1
        return textChoice