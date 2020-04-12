from frame import Frame

class BowlingGame:
    def __init__(self,pins):
        self.validate_values(pins)
        self.frames = []

        length = len(pins)
        index = 0
        if length %2 != 0 and pins[length-3] != 10 and pins[length-1] != 10: 
            pins.append(0)  

        while index < len(pins):
            if pins[index] == 10:
                self.frames.append(Frame(10,0))
                index += 1
            else:
                self.frames.append(Frame(pins[index],pins[index + 1]))
                index += 2

    def calculate_score(self):
        result = 0
        length = len(self.frames)

        if length % 2 != 0 and length != 11:
            return 'Invalid number of frames.'
        
        index = 0

        while index < length-1:
            if str(self.frames[index]) == 'Strike':
                result += getattr(self.frames[index], 'first_try')
                if str(self.frames[index+1]) == 'Strike':
                    result += getattr(self.frames[index+1], 'first_try')
                    if index + 2 > length-1:
                        break
                    else:
                        result += getattr(self.frames[index+2], 'first_try')
                        if index + 2 == length-1 and str(self.frames[index+2]) == 'Strike':
                            return result
                else:
                    result += getattr(self.frames[index+1], 'first_try')
                    result += getattr(self.frames[index+1], 'second_try')
            elif str(self.frames[index]) == 'Spare':
                helping_index = index
                result += getattr(self.frames[helping_index], 'first_try')
                result += getattr(self.frames[helping_index], 'second_try')
                result += getattr(self.frames[helping_index+1], 'first_try')
                if helping_index+1 == length-1:
                    return result
            else:
                result += getattr(self.frames[index], 'first_try') + getattr(self.frames[index], 'second_try')
            index += 1

        if str(self.frames[length-1]) == 'Open Frame' and str(self.frames[length-3]) != 'Spare':
            return result + getattr(self.frames[length-1], 'first_try') + getattr(self.frames[length-1], 'second_try')

        return result   

    def __str__(self):
        result = ''
        for i in range(len(self.frames)):
            result += repr(self.frames[i]) + ' '
        return result[:-1]

    @staticmethod
    def validate_values(pins):
        if not isinstance(pins,list):
            raise TypeError('Wrong input - you have to enter list of positive integers')
        elif len(pins) < 10:
            raise TypeError('Wrong input - can not have less than 10 tries')
        elif len(pins) > 21:
            raise TypeError('Wrong input - can not have more than 20 tries')
        for elem in pins:
            if not isinstance(elem,int):
                raise TypeError('Wrong input - you must enter integers for knocked pins')

