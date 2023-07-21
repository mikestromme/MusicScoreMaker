import tkinter as tk

# Create a root window
root = tk.Tk()

# Create a canvas to draw on
canvas = tk.Canvas(root, width=600, height=200)
canvas.pack()

# Draw five horizontal lines for the staff
for i in range(5):
    canvas.create_line(50, 50 + i*20, 550, 50 + i*20)

# Assign names to each line and space
staff_positions = {
    'E5': 50,
    'D5': 70,
    'C5': 90,
    'B4': 110,
    'A4': 130,
    'G4': 150,
    'F4': 170,
    'E4': 190
}

# Function to draw a note
def draw_note():
    note_name = note_entry.get()
    time = int(time_entry.get())
    y = staff_positions[note_name]
    x = 50 + time * 20
    canvas.create_oval(x-10, y-10, x+10, y+10, fill='black')

# Create Entry widgets for note name and time
note_entry = tk.Entry(root)
note_entry.pack()
note_entry.insert(0, 'E5')

time_entry = tk.Entry(root)
time_entry.pack()
time_entry.insert(0, '1')

# Create a Button to draw the note
draw_button = tk.Button(root, text='Draw Note', command=draw_note)
draw_button.pack()

# Run the Tkinter event loop
root.mainloop()
