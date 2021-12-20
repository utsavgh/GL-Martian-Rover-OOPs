from Rover import Rover

class MarsRover(Rover):
    def navigate(self,inp,tc):
        if len(inp) > self.get_charge_left():
            raise Exception('Rover does not have enough charge to reach destination')
        for i in inp :
            if i=='l' or i=='L': 
                self.__move_left(tc)
            elif i=='r' or i=='R': 
                self.__move_right(tc)
            elif i=='f' or i=='F': 
                self.__move_forward(tc)
            elif i=='b' or i=='B': 
                self.__move_backward(tc)
            else : 
                raise Exception('Invalid input given',i)

        #input here is a direction for movement string made of L/l,R/r,F/f,B/b e.g. "LfrrBFllFF", returns success/failure. Stops if it sees any other object in its path. If the rover reaches the destination then it is success else it is failure. Works only when charge is available on the rover, gives update about the charging needed
        # pass
		
    def __move_left(self, tc):
        if self.x - 1 < 0:
            raise Exception("Out of bound on x axis, cannot go further left")
        if (self.x - 1, self.y) in tc : 
            raise Exception("Rover clash !!") 
        self.x -= 1
        self.charge_left -= 1
        #private function
		
    def __move_right(self, tc):
        if self.x + 1 > self.maxx:
            raise Exception("Out of bound on x axis, cannot go further right")
        if (self.x + 1, self.y) in tc : 
            raise Exception("Rover clash !!") 
        self.x += 1
        self.charge_left -= 1
        #private function
        # pass
		
    def __move_forward(self, tc):
        if self.y + 1 > self.maxy:
            raise Exception("Out of bound on y axis, cannot go forward")
        if (self.x, self.y + 1) in tc : 
            raise Exception("Rover clash !!") 
        self.y += 1
        self.charge_left -= 1
        #private function
        # pass
		
    def __move_backward(self, tc):
        if self.y - 1 < 0:
            raise Exception("Out of bound on y axis, cannot go backward")
        if (self.x, self.y - 1) in tc : 
            raise Exception("Rover clash !!") 
        self.y -= 1
        self.charge_left -= 1
        #private function
        # pass