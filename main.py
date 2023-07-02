from turtle import Turtle, Screen
# import colorgram
import random

# colours = colorgram.extract('hirst_spot.jpg', 20)

#membuat sebuah funtion untuk mendapatkan extract warna dari sebuah foto
# def get_color():
#     for colour in colours:
#         r = colour.rgb.r
#         g = colour.rgb.g
#         b = colour.rgb.b
#
#         new_colour = (r, g, b)
#         colour_list.append(new_colour)
#
# get_color()
# print(colour_list)

colour_list = [(236, 252, 244), (249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.speed(0)

# Menentukan ukuran dari sebuah window
width = 800
height = 600
screen.setup(width, height)

# Menentukan baris dan kolom untuk pembuatan hirst point
rows = 10
cols = 10

# Menentukan lebar dan tinggi sebuah kotak berdasarkan jumlah baris dan kolom
box_width = width / cols # 80
box_height = height / rows # 60

# Menggambar sebuah hirst point
for row in range(rows):
    for col in range(cols):
        # Menentukan posisi x awal dari pembuatan hirst point
        x_position = col * box_width - width / 2 # E.G -400
        # Menetukan posisi x hirst point agar tidak keluar dari Window
        x = x_position + box_width / 2 # E.G -360
        # Menentukan posisi y awal dari pembuatan hirst point
        y_position = row * box_height - height / 2 # E.G -300
        # Menentukan posisi y hirst point agar tidak keluar dari window
        y = y_position + box_height / 2 # E.G - 240

        # Merubah posisi dari turtle
        tim.penup()
        tim.goto(x, y)

        # Melukis sebuah titik di posisi yang telah ditentukan
        tim.pendown()
        colour_choose = random.choice(colour_list)
        # print(colour_choose)
        tim.dot(20, colour_choose)



# Program akan berhenti ketika mengclick layar
screen.exitonclick()
