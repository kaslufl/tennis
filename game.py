MINIMAL_POINTS_TO_ADVANTAGE = 3
MINIMAL_POINTS_TO_WIN = 4
MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET = 2


class Game:
    def __init__(self, player_1_name, player_2_name):
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player_1_name:
            self.player_1_score_point()
        else:
            self.player_2_score_point()

    def score(self):
        result = ""
        if self.is_game_tied():
            result = self.get_tied_score(self.p1points)

        player_1_score = ""
        player_2_score = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                player_1_score = "Fifteen"
            if (self.p1points == 2):
                player_1_score = "Thirty"
            if (self.p1points == 3):
                player_1_score = "Forty"

            player_2_score = "Love"
            result = player_1_score + "-" + player_2_score
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                player_2_score = "Fifteen"
            if (self.p2points == 2):
                player_2_score = "Thirty"
            if (self.p2points == 3):
                player_2_score = "Forty"

            player_1_score = "Love"
            result = player_1_score + "-" + player_2_score

        if (self.p1points > self.p2points and self.p1points < MINIMAL_POINTS_TO_WIN):
            if (self.p1points == 2):
                player_1_score = "Thirty"
            if (self.p1points == 3):
                player_1_score = "Forty"
            if (self.p2points == 1):
                player_2_score = "Fifteen"
            if (self.p2points == 2):
                player_2_score = "Thirty"
            result = player_1_score + "-" + player_2_score
        if (self.p2points > self.p1points and self.p2points < MINIMAL_POINTS_TO_WIN):
            if (self.p2points == 2):
                player_2_score = "Thirty"
            if (self.p2points == 3):
                player_2_score = "Forty"
            if (self.p1points == 1):
                player_1_score = "Fifteen"
            if (self.p1points == 2):
                player_1_score = "Thirty"
            result = player_1_score + "-" + player_2_score

        if (self.p1points > self.p2points and self.p2points >= MINIMAL_POINTS_TO_ADVANTAGE):
            result = "Advantage " + self.player_1_name

        if (self.p2points > self.p1points and self.p1points >= MINIMAL_POINTS_TO_ADVANTAGE):
            result = "Advantage " + self.player_2_name

        if (self.p1points >= MINIMAL_POINTS_TO_WIN and self.p2points >= 0 and (self.p1points - self.p2points) >= MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET):
            result = "Win for " + self.player_1_name
        if (self.p2points >= MINIMAL_POINTS_TO_WIN and self.p1points >= 0 and (self.p2points - self.p1points) >= MINIMAL_POINTS_DIFERENCE_TO_SCORE_SET):
            result = "Win for " + self.player_2_name
        return result

    def is_game_tied(self):
        return self.p1points == self.p2points and self.p1points < MINIMAL_POINTS_TO_ADVANTAGE

    def get_tied_score(self, points):
        result = None
        if points >= MINIMAL_POINTS_TO_ADVANTAGE:
            result = "Deuce"
            return result
        if points == 0:
            result = "Love"
        if points == 1:
            result = "Fifteen"
        if points == 2:
            result = "Thirty"
        result += "-All"

        return result

    def set_player_1_score(self, number):
        for i in range(number):
            self.player_1_score_point()

    def set_player_2_score(self, number):
        for i in range(number):
            self.player_2_score_point()

    def player_1_score_point(self):
        self.p1points += 1

    def player_2_score_point(self):
        self.p2points += 1
