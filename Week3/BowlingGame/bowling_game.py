class BowlingGame:
    def __init__(self,rolls):
        self.validate_values(rolls)

        self.rolls = rolls
        self.result = 0

    def calculateScore(self):

        index = 0
        score = 0
        
        for i in range(10):
            if self.rolls[index] == 10:
                score += self.getStrikeScore(index)
                index += 1
            elif self.rolls[index] + self.rolls[index + 1] == 10:
                score += self.getSpareScore(index)
                index += 2 
            else:
                score += self.getOpenFrameScore(index)
                index += 2
        
        return score

    def getStrikeScore(self,index):
        return self.rolls[index + 1] + self.rolls[index + 2] + 10

    def getSpareScore(self,index):
        return self.rolls[index + 2] + 10

    def getOpenFrameScore(self,index):
        return self.rolls[index] + self.rolls[index + 1]


    @staticmethod
    def validate_values(rolls):
        if not isinstance(rolls,list):
            raise TypeError('Wrong input - you have to enter list of positive integers')
        for elem in rolls:
            if not isinstance(elem,int):
                raise TypeError('Wrong input - a value in the list is not integer')
            if elem < 0:
                raise ValueError('Wrong value - a value in the list is negative - all values must be positive integers')
            if elem > 10:
                raise ValueError('Wrong value - all values must be positive integers not greater than 10')