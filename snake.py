from turtle import Turtle, Screen
import time

X_LINE = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

      def __init__(self):
          self.snakes = []
          self.create_snake()
          self.head = self.snakes[0]

      def create_snake(self):
          for position in X_LINE:
              self.add_snake(position)



      def add_snake(self, position):
          new_snake = Turtle("square")
          new_snake.color("white")
          new_snake.penup()
          new_snake.goto(position)
          self.snakes.append(new_snake)


      def reset(self):
          for sna in self.snakes:
              sna.goto(1000, 1000)
          self.snakes.clear()
          self.create_snake()
          self.head = self.snakes[0]

      def extent(self):
          self.add_snake(self.snakes[-1].position())




      def move(self):
          for snake_num in range(len(self.snakes) - 1, 0, -1):
              new_x = self.snakes[snake_num - 1].xcor()
              new_y = self.snakes[snake_num - 1].ycor()
              self.snakes[snake_num].goto(new_x, new_y)
          self.head.fd(MOVE_DIS)

      def move_up (self):
          if self.head.heading() != DOWN:
              self.head.setheading(UP)


      def move_down(self):
          if self.head.heading() != UP:
              self.head.setheading(DOWN)

      def move_left(self):
          if self.head.heading() != RIGHT:
              self.head.setheading(LEFT)

      def move_right(self):
          if self.head.heading() != LEFT:
              self.head.setheading(RIGHT)


