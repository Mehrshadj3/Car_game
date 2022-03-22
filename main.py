import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
sleep_time = 0.1
screen.setup(width=600, height=600)

screen.title('Turtle Pass')
screen.tracer(0)
screen.update()
screen.listen()
screen.onkey(player.move, 'w')



game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.creat_cars()
    car_manager.car_move()
    screen.update()
    for car in car_manager.cars:
        if player.distance(car) < 20:
           game_is_on = False
           scoreboard.game_is_over()
    if player.ycor() > 280:
        player.level_up()
        scoreboard.add_score()
        screen.update()
        time.sleep(sleep_time * 0.8)


screen.exitonclick()







