# 👉 Run "./connect" (or "connect.cmd" on Windows) in the terminal to get started
class Bot:
    def __init__(self, config):
        print("Hello World!", config)
        pass

    def move(self, board):
        print(board)  # 3x3 array with values "x" or "o" or "empty"

        # Return the spot you'd like to move here.
        # 1st value: x, should be an integer between 0 and 2
        # 2nd value: y, should be an integer between 0 and 2
        return (0, 1)

    def end(self, board):
        print("Good game!")
