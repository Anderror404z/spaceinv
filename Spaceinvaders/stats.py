class Stats():
    """tracking statistic """

    def __init__(self):
        """initialization statistic"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """statistic that change during the game"""
        self.health = 2
        self.score = 0
        self.guns_left = 3
    def reset_health(self):
        self.health = 2
