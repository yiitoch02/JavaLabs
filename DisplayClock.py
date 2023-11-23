import tkinter as tk
import time
import math # For the math functions

# Define the clock face
def draw_clock_face(canvas):
    # Draw the clock face circle
    canvas.create_oval(0, 0, 200, 200, fill="#ffffff")

    # Draw the hour marks
    for i in range(12):
        angle = i * 30
        start_x, start_y = 100 + 80 * math.cos(math.radians(angle)), 100 + 80 * math.sin(math.radians(angle))
        end_x, end_y = 100 + 60 * math.cos(math.radians(angle)), 100 + 60 * math.sin(math.radians(angle))
        canvas.create_line(start_x, start_y, end_x, end_y, width=5, fill="#000000")

    # Draw the minute marks
    for i in range(60):
        angle = i * 6
        start_x, start_y = 100 + 70 * math.cos(math.radians(angle)), 100 + 70 * math.sin(math.radians(angle))
        end_x, end_y = 100 + 50 * math.cos(math.radians(angle)), 100 + 50 * math.sin(math.radians(angle))
        canvas.create_line(start_x, start_y, end_x, end_y, width=2, fill="#000000")

    # Draw the center dot
    canvas.create_oval(95, 95, 105, 105, fill="#000000")

# Define the clock hands
def draw_clock_hands(canvas, hour, minute, second):
    # Draw the hour hand
    hour_angle = hour * 30 + minute * 0.5
    start_x, start_y = 100, 100
    end_x, end_y = 100 + 40 * math.cos(math.radians(hour_angle)), 100 + 40 * math.sin(math.radians(hour_angle))
    canvas.create_line(start_x, start_y, end_x, end_y, width=8, fill="#000000")

    # Draw the minute hand
    minute_angle = minute * 6 + second * 0.1
    start_x, start_y = 100, 100
    end_x, end_y = 100 + 30 * math.cos(math.radians(minute_angle)), 100 + 30 * math.sin(math.radians(minute_angle))
    canvas.create_line(start_x, start_y, end_x, end_y, width=5, fill="#000000")

    # Draw the second hand
    second_angle = second * 6
    start_x, start_y = 100, 100
    end_x, end_y = 100 + 20 * math.cos(math.radians(second_angle)), 100 + 20 * math.sin(math.radians(second_angle))
    canvas.create_line(start_x, start_y, end_x, end_y, width=2, fill="#000000")

# Create the main window
root = tk.Tk()
root.title("Still Clock")
root.geometry("200x200")

# Create the canvas
canvas = tk.Canvas(root, width=200, height=200, bg="#ffffff")
canvas.pack()

# Draw the clock face
draw_clock_face(canvas)

# Get the current time
hour = time.strftime("%H")
minute = time.strftime("%M")
second = time.strftime("%S")

# Draw the clock hands
draw_clock_hands(canvas, int(hour), int(minute), int(second))

# Start the main loop
root.mainloop()
