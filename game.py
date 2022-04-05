MINIMAL_POINTS_TO_SCORE_SET = 3
MINIMAL_SETS_TO_WIN = 4
MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET = 2


class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < MINIMAL_POINTS_TO_SCORE_SET):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p1points < MINIMAL_SETS_TO_WIN):
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.p2points > self.p1points and self.p2points < MINIMAL_SETS_TO_WIN):
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= MINIMAL_POINTS_TO_SCORE_SET):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= MINIMAL_POINTS_TO_SCORE_SET):
            result = "Advantage " + self.player2Name

        if (self.p1points >= MINIMAL_SETS_TO_WIN and self.p2points >= 0 and (self.p1points - self.p2points) >= MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET):
            result = "Win for " + self.player1Name
        if (self.p2points >= MINIMAL_SETS_TO_WIN and self.p1points >= 0 and (self.p2points - self.p1points) >= MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1
