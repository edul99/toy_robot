
# Online Python - IDE, Editor, Compiler, Interpreter

class ToyRobot:
    def __init__(self):
        self.x = None
        self.y = None
        self.f = None
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    def place(self, x, y, f):
        """Place the robot on the table in position X,Y and facing NORTH, SOUTH, EAST, or WEST"""
        if 0 <= x < 5 and 0 <= y < 5 and f in self.directions:
            self.x = x
            self.y = y
            self.f = f
        else:
            print("Invalid placement.")

    def move(self):
        """Move the robot one unit forward in the direction it is currently facing"""
        if self.x is not None and self.y is not None:
            if self.f == "NORTH" and self.y < 4:
                self.y += 1
            elif self.f == "EAST" and self.x < 4:
                self.x += 1
            elif self.f == "SOUTH" and self.y > 0:
                self.y -= 1
            elif self.f == "WEST" and self.x > 0:
                self.x -= 1

    def left(self):
        """Rotate the robot 90 degrees to the left without changing its position"""
        if self.f:
            self.f = self.directions[(self.directions.index(self.f) - 1) % len(self.directions)]

    def right(self):
        """Rotate the robot 90 degrees to the right without changing its position"""
        if self.f:
            self.f = self.directions[(self.directions.index(self.f) + 1) % len(self.directions)]

    def report(self):
        """Announce the X,Y coordinates and the direction the robot is facing"""
        if self.x is not None and self.y is not None and self.f:
            print(f"Output: {self.x},{self.y},{self.f}")

def main():
    robot = ToyRobot()
    "MODIFY YOUR COMMANDS HERE"
    commands = [
        "PLACE 2,2,NORTH",
        "MOVE",
        "RIGHT",
        "MOVE",
        "REPORT"
    ]

    for command in commands:
        if command.startswith("PLACE"):
            parts = command.split()  # Splitting by space first to separate "PLACE" from the coordinates and direction
            _, position = parts  # This will separate "PLACE" from "0,0,NORTH"
            x, y, f = position.split(',')  # Now splitting by comma to get x, y, and f
            robot.place(int(x), int(y), f)  # Converting x and y to integers before passing
        elif command == "MOVE":
            robot.move()
        elif command == "LEFT":
            robot.left()
        elif command == "RIGHT":
            robot.right()
        elif command == "REPORT":
            robot.report()

if __name__ == "__main__":
    main()

