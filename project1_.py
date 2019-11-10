import turtle
import random


def draw_sq(t,distance=200):
    # 사각형을 그리는 함수

def add_tri():
    global l_tri
    # 삼각형 터틀을 만들고 랜덤한 위치,랜덤한 방향으로 설정해
    # l_tri의 리스트에 저장하는 함수

def turn_right():
    global right
    right = True

def turn_left():
    global left
    left = True

def turn_up():
    global up
    up = True

def turn_down():
    global down
    down = True

def _turn_right():
    global right
    right = False

def _turn_left():
    global left
    left = False

def _turn_up():
    global up
    up = False

def _turn_down():
    global down
    down = False

def is_touch(x,y,triangle,threshold=20):
    global playing
    # 삼각형들과 거북이가 부딛혔는지 판단해 부딛히면 playing을 False로 바꾸는 함수
    # triangle은 삼각형, threshold는 판단하는 기준거리, x,y는 거북이의 위치

def timer_go():
    global heading
    # heading은 거북이의 방향
    # 거북이들을 입력대로 움직이는코드
    # 삼각형들이 벽에 부딛히면 튕기게 방향을 바꾸는 코드
    # 위 함수를 이용해 삼각형들이 거북이와 부딛혔는지 확인
    # 삼각형들을 움직이는 코드
    # playing이 아닐때 FAIL을 출력하는 코드


up = False
down = False
right = False
left = False
playing = True
heading = 0
l_tri = []

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
draw_sq(t)
screen = t.screen


screen.onkeypress(turn_right, 'Right')
screen.onkeypress(turn_left, 'Left')
screen.onkeypress(turn_up, 'Up')
screen.onkeypress(turn_down, 'Down')
screen.onkeyrelease(_turn_right, 'Right')
screen.onkeyrelease(_turn_left, 'Left')
screen.onkeyrelease(_turn_up, 'Up')
screen.onkeyrelease(_turn_down, 'Down')


for i in range(5):
    add_tri()

for i in range(1,200):
    time = i*100
    screen.ontimer(timer_go, time)

# 끝나고 성공했으면 success를 쓰는 함수

screen.listen()
screen.mainloop()