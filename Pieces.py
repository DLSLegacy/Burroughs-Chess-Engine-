from random import shuffle, randint
import sys, json, datetime

class unit:
    def __init__(self, x, y, power, owner):
        self.pos_x = x
        self.pos_y = y
        self.owner = owner

        i = pawn
        R = rook
        N = knight
        LB = Left Bishop
        RB = Right Bishop
        Q = queen
        K = king

        self.power = power

    def getPowerString(self):
        if self.power == i:
            return "pawn"
        elif self.power == R:
            return "rook"
        elif self.power == N:
            return "knight"
        elif self.power == LB:
            return "bishop"
        elif self.power == RB:
            return "bishop
        elif self.power == Q:
            return "queen"
        elif self.power == K:
            return "king"
        else:
            return "ERROR"

        def getPos_x(self):
            return self.pos_x

        def setPos_x(self, pos_x):
            self.pos_x = pos_x
            
