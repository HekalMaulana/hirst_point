from turtle import Turtle, Screen
import random

# List dari sebuah warna yang digunakan untuk setiap dots di hirst point
colour_list = [(249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9),
               (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154),
               (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51),
               (55, 24, 11), (228, 165, 9), (61, 200, 232)]

# Membuat sebuah variabel untuk memanggil class Turle() dan Screen()
tim = Turtle()
screen = Screen()

# Fungsi di turtle module untuk menentukan wanra RGB,kecepatan turlte, dan menyembunyikan turtle(cursor)
screen.colormode(255)
tim.speed("fastest")
tim.hideturtle()

# Menentukan posisi awal turtle untuk membuat dots
tim.setheading(215)
tim.penup()
tim.forward(350)
tim.setheading(0)


# Perulangan untuk membuat sebuah dots
for dots_count in range(1, 100 + 1):
    # Membuat sebuah dots dan maju 50 langkah
    tim.dot(15, random.choice(colour_list))
    tim.forward(50)

    # Membuat sebuah kondisi dimana ketika sudah membuat 50 dots akan kembali ke sisi kiri dan naik 50 langkah ke atasnya
    if dots_count % 10 == 0 and dots_count < 100:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# sebuah function di turtle module yang berguna untuk memberhentikan program ketika mengclick window
screen.exitonclick()
