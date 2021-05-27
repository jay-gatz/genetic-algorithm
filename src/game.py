class Game:
    def __init__(self, levels, gumpa_kill = True):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps
        self.gumpa_kill = gumpa_kill
        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0

    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])

    def get_score(self, actions):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        current_level = self.levels[self.current_level_index]
        step = 0
        score = 0
        max_score = 0
        mushroom = 0
        for i in range(self.current_level_len - 1):
            current_step = current_level[i]
            if actions[i-1] != '0':
                score -= 1
            if (current_step == '_'):
                step += 1
            elif (current_step == 'G'):
                if actions[i - 1] == '1':
                    step += 1
                elif actions[i - 2] == '1' and self.gumpa_kill and i != 1:
                    score += 2
                    step += 1
            elif (current_step == 'L' and actions[i - 1] == '2'):
                step += 1
            elif (current_step == 'M'):
                step += 1
                if actions[i-1] != '1':
                    mushroom += 2
            else:
                step = 0
            if step + score > max_score:
                max_score = step + score
        return step == self.current_level_len - 1, max_score + mushroom


if __name__ == '__main__':
    g = Game(["_G_________", "___G_M___L_"])
    g.load_next_level()

    # This outputs (False, 4)
    print(g.get_score("0000000000"))
