"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
import turtle  # import turtle library
import time
import sys

wn = turtle.Screen()  # define the turtle screen
wn.bgcolor("black")  # set the background colour
wn.setup(1300, 700)  # setup the dimensions of the working window


# class for the Maze turtle (white square)
class Maze(turtle.Turtle):  # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")  # the turtle shape
        self.color("white")  # colour of the turtle
        self.penup()  # lift up the pen so it do not leave a trail
        self.speed(0)  # sets the speed that the maze is written to the screen


# class for the End marker turtle (green square)
class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)


# class for the sprite turtle (red turtle)
class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)




class Node:
    # Initialize the class
    def __init__(self, position: (1), parent: (1)):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


class NodeGS:
    # Initialize the class
    def __init__(self, position: (1), parent: (1)):
        self.position = position
        self.parent = parent

        self.h = 0  # Distance to goal node

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.h < other.h

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.h))


class UniformNode:
    # Initialize the class
    def __init__(self, position: (1), parent: (1)):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance to start node

    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position

    # Sort nodes
    def __lt__(self, other):
        return self.g > other.g

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.g))



def uniform_search(map, start, end, sprite):

    open = []
    closed = []

    start_node = UniformNode(start, None)
    goal_node = UniformNode(end, None)

    open.append(start_node)


    while len(open) > 0:

        open.sort()

        current_node = open.pop(0)

        closed.append(current_node)


        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent

            return path[::-1]
            print("Finished")
            #endProgram()

        x_walls = round(sprite.xcor(), 0)
        y_walls = round(sprite.ycor(), 0)

        x = x_walls
        y = y_walls

        (x, y) = current_node.position

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


        for next in neighbors:

            map_value = map.get(next)

            if (map_value == '+'):
                continue

            neighbor = UniformNode(next, current_node)

            if (neighbor in closed):
                continue

            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            print("X and Y axies: ", x,y)
            print("Path Cost: ", neighbor.g)

            if (add_to_openUC(open, neighbor) == True):
                open.append(neighbor)
    return None


# Greedysearch ##################################################################################################################################
def GreedySearch(map, start, end, sprite):

    open = []
    closed = []

    start_node = NodeGS(start, None)
    goal_node = NodeGS(end, None)

    open.append(start_node)


    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
                # Return reversed path
            return path[::-1]
            print("Finished")
            
        # Unzip the current node position
        x_walls = round(sprite.xcor(), 0)
        y_walls = round(sprite.ycor(), 0)
        # print("The X - Axis :", x_walls, "The Y - Axis :", y_walls)
        x = x_walls
        y = y_walls
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        # Loop neighbors
        for next in neighbors:
            # Get value from maze
            map_value = map.get(next)
            # Check if the node is a wall
            if (map_value == '+'):
                continue
            # Create a neighbor node
            neighbor = NodeGS(next, current_node)
            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue
            # Generate heuristics (Manhattan distance)

            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            print("Heuristic", neighbor.h)
            print("X and Y axies: ", x, y)
            # Check if neighbor is in open list and if it has a lower f value
            if (add_to_openGS(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
    # Return None, no path is found
    return None


# A* search ##################################################################################################################################
def astar_search(map, start, end, sprite):

    open = []
    closed = []

    start_node = Node(start, None)
    goal_node = Node(end, None)

    open.append(start_node)

    print("This Is The Start Node In The Func " , start_node , "This Is The Goal Node In The Func " , goal_node)


    while len(open) > 0:

        open.sort()

        current_node = open.pop(0)

        closed.append(current_node)

        print("=====================================================================")
        print("The Current Node Is " , current_node)

        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent

            print("Finished")
            return path[::-1]

            #endProgram()

        x_walls = round(sprite.xcor(), 0)
        y_walls = round(sprite.ycor(), 0)
        #print("The X - Axis :", x_walls, "The Y - Axis :", y_walls)
        x = x_walls
        y = y_walls
        (x, y) = current_node.position

        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


        for next in neighbors:

            map_value = map.get(next)

            if (map_value == '+'):
                continue

            neighbor = Node(next, current_node)

            if (neighbor in closed):
                continue

            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(
                neighbor.position[1] - start_node.position[1])
            neighbor.h = abs(neighbor.position[0] - goal_node.position[0]) + abs(
                neighbor.position[1] - goal_node.position[1])
            neighbor.f = neighbor.g + neighbor.h

            print("The Path Cost IS : ", neighbor.g)
            print("The Heuristicc IS : " , neighbor.h)


            if neighbor.h == 0:
                print("The End X-Axis :  " , x , "The End Y-Axis :  " , y)

            if (add_to_open(open, neighbor) == True):

                open.append(neighbor)

    return None


def add_to_openGS(open, neighbor):
    for NodeGS in open:
        if (neighbor == NodeGS and neighbor.h >= NodeGS.h):
            return False
    return True




def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

def add_to_openUC(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.g >= node.g):
            return False
    return True

grid = [
"++++++++++++++++++++++++++++++++++++++++++",
"+s          +                            +",
"+ +++++++++ +++++++++++  +++++++  ++++++++",
"+       +             +       +         ++",
"+ +++++ +++++++++++ ++++++++++++++++++++++",
"+ +   + +         + +                   ++",
"+ + + + + + ++++  + + ++++++++++++++++++++",
"+ + + + + + +     + + + +        +   +++++",
"+ + +++ + +++++++++ + + +++++++  + ++    +",
"+ +   + +                        + +++++ +",
"+ +++ + +++++++++++++++ ++++++++++ +++++ +",
"+   + +                   ++             +",
"+++ + +++++++++++++++++++ ++  ++++++++++ +",
"+ + +                         +    + +   +",
"+ + ++++  +++++++++++++ +  ++++  + + + +++",
"+ + + +   +     +    ++ +  +     +   + +++",
"+ + + +++++++  ++++  ++    + +++++++++ +++",
"+                       +  +             +",
"+++++++++++++++++++++++e++++++++++++++++++",
]

# ############ main program starts here  ######################



def main():
    # Get a maze (grid)
    map = {}
    chars = ['c']
    startMap = None
    endMap = None
    width = 0
    height = 0
    walls = []  # create walls coordinate list
    finish = []  # enable the finish array
    maze = Maze()  # enable the maze class
    end = End()  # enable End position class

    # Open a file
    fp = open('Mazee Design2.txt', 'r')

    # Loop until there is no more lines
    while len(chars) > 0:
        # Get chars in a line
        chars = [str(i) for i in fp.readline().strip()]
        # Calculate the width
        width = len(chars) if width == 0 else width
        # Add chars to map
        for x in range(len(chars)):
            map[(x, height)] = chars[x]
            if (chars[x] == 's'):
                startMap = (x, height)
            elif (chars[x] == 'e'):
                endMap = (x, height)

        # Increase the height of the map
        if (len(chars) > 0):
            height += 1
    # Close the file pointer
    fp.close()

    for y in range(len(grid)):  # select each line in the grid
        for x in range(len(grid[y])):  # identify each character in the line
            character = grid[y][x]  # assign the grid reference to the variable character
            screen_x = -588 + (x * 24)  # assign screen_x to screen starting position for x ie -588
            screen_y = 288 - (y * 24)  # assign screen_y to screen starting position for y ie  288

            if character == "+":  # if grid character contains an +
                maze.goto(screen_x, screen_y)  # move turtle to the x and y location and
                maze.stamp()  # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))  # add coordinate to walls list

            if character == "e":  # if grid character contains an e
                #endd = (screen_x)
                end.goto(screen_x, screen_y)  # move turtle to the x and y location and
                end.stamp()  # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if character == "s":  # if the grid character contains an s
                #start = (screen_x)
                StartPosX = screen_x
                StartPosY = screen_y
                sprite.goto(screen_x, screen_y)  # move turtle to the x and y location
    #StartPosX += 24
    #StartPosY -= 24
    # Find the closest path from start(@) to end($)
    print("The Start Value Is ", startMap)
    print("The End Value Is ", endMap)

    print("Choose 1 If You Want To Solve Using A*")
    print("Choose 2 If You Want To Solve Using Greedy")
    print("Choose 3 If You Want To Solve Using Uniform Cost")
    Choice = input("Enter Your Choice: ")

    if Choice == '1':
        path = astar_search(map, startMap, endMap, sprite)

    if Choice == '2':
        path = GreedySearch(map, startMap, endMap, sprite)

    if Choice == '3':
        path = uniform_search(map, startMap, endMap, sprite)


    FL = 0
    FR = 0
    FF = 0
    FB = 0
    FStart = 0


    for i in range (len(path)):
        Pos1X = path[i][0]
        Pos1Y = path[i][1]
        if i+1 != (len(path)):
            Pos2X = path[i+1][0]
            Pos2Y = path[i+1][1]

        if Pos2X > Pos1X:
            if FStart == 0:
                StartPosX += 24
                FStart = 1

            if FL == 0:
                if FF == 1:
                    sprite.right(90)
                else:
                    sprite.left(90)
                FL = 1
                FR = 0

            StartPosX += 24
            sprite.goto(StartPosX , StartPosY)

        if Pos2X < Pos1X:
            if FStart == 0:
                StartPosX -= 24
                FStart = 1

            sprite.right(90)
            StartPosX -= 24
            sprite.goto(StartPosX , StartPosY)

        if Pos2Y > Pos1Y:
            if FStart == 0:
                StartPosY -= 24
                FStart = 1

            if FR == 0:
                sprite.right(90)
                FR = 1
                FL = 0
            StartPosY -= 24
            sprite.goto(StartPosX, StartPosY)

        if Pos2Y < Pos1Y:
            if FStart == 0:
                StartPosY += 24
                FStart = 1

            if FF == 0:
                sprite.left(90)
                FF = 1
                FL = 0
            StartPosY += 24
            sprite.goto(StartPosX, StartPosY)

        time.sleep(0.5)



    print()
    print(path)
    print()
    # draw_grid(maze, width, height, spacing=1, path=path, start=start, goal=end)
    print()
    print('Steps to goal: {0}'.format(len(path)))
    print()


# Tell python to run main method
if __name__ == "__main__":
    sprite = sprite()  # enable the sprite  class
    main()
