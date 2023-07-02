import turtle
import random

# Menentukan lebar dan tinggi jendela turtle
width = 800
height = 600

# Mengatur ukuran jendela turtle
turtle.setup(width, height) # width = 800, height = 600

# Membuat objek turtle
t = turtle.Turtle()
t.speed(0)  # Mengatur kecepatan turtle menjadi maksimum

# Menentukan jumlah baris dan kolom
rows = 10
cols = 10

# Menghitung lebar dan tinggi kotak berdasarkan jumlah baris dan kolom
box_width = width / cols # box_width = 80
box_height = height / rows # box_height = 60

# Menggambar Hirst Point
for row in range(rows): # 0 - 9
    for col in range(cols): # 0 - 9
        # Mengatur posisi turtle di setiap kotak
        x = col * box_width - width / 2 + box_width / 2 # col * box_width = 0, width / 2 = 400, box_width / 2 = 40, x= 0 - 400 + 40 = -360
        y = row * box_height - height / 2 + box_height / 2 #row * box_height = 0, height / 2 = 300, box_height / 2 = 60, y = 0 - 300 + 60 = -240
        t.penup() # mengangkat pensil
        t.goto(x, y) # mengubah posisi turtle ke (x = -360, y = -240)
        t.pendown() # menurunkan pensil

        # Menggambar titik dengan warna acak
        color = (random.random(), random.random(), random.random()) # menentukan warna rgb acak dengan tupple
        t.dot(20, color) # melukis sebuah lingkaran dengan radius 20 dan warna acak

# Menjaga jendela turtle tetap terbuka
turtle.done()
