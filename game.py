from player import Player

MINIMAL_POINTS_TO_ADVANTAGE = 3
MINIMAL_POINTS_TO_WIN = 4
MINIMAL_POINTS_DIFFERENCE_TO_SCORE_SET = 2
SCORES = {
    0: 'Love',
    1: 'Fifteen',
    2: 'Thirty',
    3: 'Forty'
}


class Game:
    def __init__(self, player_1_name, player_2_name):
        self.player1 = Player(player_1_name)
        self.player2 = Player(player_2_name)

    def won_point(self, player_name):
        if player_name == self.player1.get_name():
            self.player_1_score_point()
        else:
            self.player_2_score_point()

    def score(self):
        if self.is_game_tied():
            result = self.get_tied_score(self.player1.get_points())

        elif self.is_p1_in_advantage():
            result = "Advantage " + self.player1.get_name()

        elif self.is_p2_in_advantage():
            result = "Advantage " + self.player2.get_name()

        elif self.is_player_in_set_point(self.player1.get_points()) and self.is_game_winnable(self.get_p1_p2_difference()):
            result = "Win for " + self.player1.get_name()

        elif self.is_player_in_set_point(self.player2.get_points()) and self.is_game_winnable(self.get_p2_p1_difference()):
            result = "Win for " + self.player2.get_name()
        else:
            player_1_score = self.get_score(self.player1.get_points())
            player_2_score = self.get_score(self.player2.get_points())
            result = player_1_score + "-" + player_2_score

        return result

    def is_game_winnable(self, difference):
        return difference >= MINIMAL_POINTS_DIFFERENCE_TO_SCORE_SET

    def get_p1_p2_difference(self):
        return self.player1.get_points() - self.player2.get_points()

    def get_p2_p1_difference(self):
        return self.player2.get_points() - self.player1.get_points()

    def is_player_in_set_point(self, points):
        return points >= MINIMAL_POINTS_TO_WIN

    def is_p2_in_advantage(self):
        return self.player2.get_points() > self.player1.get_points() >= MINIMAL_POINTS_TO_ADVANTAGE

    def is_p1_in_advantage(self):
        return self.player1.get_points() > self.player2.get_points() >= MINIMAL_POINTS_TO_ADVANTAGE

    def is_game_tied(self):
        return self.player1.get_points() == self.player2.get_points() and self.player1.get_points() < MINIMAL_POINTS_TO_ADVANTAGE

    def get_tied_score(self, points):
        if points >= MINIMAL_POINTS_TO_ADVANTAGE:
            return "Deuce"
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
        self.player1.set_points(self.player1.get_points() + 1)

    def player_2_score_point(self):
        self.player2.set_points(self.player2.get_points() + 1)
