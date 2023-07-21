import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axes
fig, ax = plt.subplots()

# Draw five horizontal lines for the staff
for i in range(5):
    ax.hlines(i, 0, 10, color='black')

# Function to draw a note
def draw_note(note_position, time):
    circle = plt.Circle((time, note_position), 0.2, color='black')
    ax.add_artist(circle)

# Draw some notes
draw_note(2, 1)  # A note on the third line at time 1
draw_note(0, 2)  # A note on the first line at time 2
draw_note(4, 3)  # A note on the fifth line at time 3

# Set the y limits to show all the lines
ax.set_ylim(-1, 5)

# Show the plot
plt.show()
