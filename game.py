MINIMAL_POINTS_TO_ADVANTAGE = 3
MINIMAL_POINTS_TO_WIN = 4
MINIMAL_POINTS_DIFFERENCE_TO_SCORE_SET = 2
SCORES = {
    0: 'Love',
    1: 'Fifteen',
    2: 'Trirty',
    3: 'Forty'
}

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
        if self.is_game_tied():
            result = self.get_tied_score(self.p1points)

        elif self.is_p1_in_advantage():
            result = "Advantage " + self.player_1_name

        elif self.is_p2_in_advantage():
            result = "Advantage " + self.player_2_name

        elif self.is_player_in_set_point(self.p1points) and self.is_game_winnable(self.get_p1_p2_difference()):
            result = "Win for " + self.player_1_name

        elif self.is_player_in_set_point(self.p2points) and self.is_game_winnable(self.get_p2_p1_difference()):
            result = "Win for " + self.player_2_name
        else:
            player_1_score = self.get_score(self.p1points)
            player_2_score = self.get_score(self.p2points)
            result = player_1_score + "-" + player_2_score

        return result

    def is_game_winnable(self, difference):
        return difference >= MINIMAL_POINTS_DIFFERENCE_TO_SCORE_SET

    def get_p1_p2_difference(self):
        return self.p1points - self.p2points

    def get_p2_p1_difference(self):
        return self.p2points - self.p1points

    def is_player_in_set_point(self, points):
        return points >= MINIMAL_POINTS_TO_WIN

    def is_p2_in_advantage(self):
        return self.p2points > self.p1points >= MINIMAL_POINTS_TO_ADVANTAGE

    def is_p1_in_advantage(self):
        return self.p1points > self.p2points >= MINIMAL_POINTS_TO_ADVANTAGE

    def is_game_tied(self):
        return self.p1points == self.p2points and self.p1points < MINIMAL_POINTS_TO_ADVANTAGE

    def get_tied_score(self, points):
        result = None
        if points >= MINIMAL_POINTS_TO_ADVANTAGE:
            result = "Deuce"
            return result
        result = self.get_score(points)
        result += "-All"

        return result

    def get_score(self, points):
        return SCORES[points]

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
