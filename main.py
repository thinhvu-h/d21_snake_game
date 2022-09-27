
from turtle import Turtle, Screen

import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="space", fun=snake.restart )
screen.listen()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision to the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision to the wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or \
            snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        scoreboard.game_over()

    # detect collision to the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()