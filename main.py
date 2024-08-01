import tkinter as tk

def clear_text():
    text_box.delete('1.0', tk.END)

def start_clear_timer(event=None):
    global timer
    # Cancel the previous timer if it exists
    if timer is not None:
        root.after_cancel(timer)
    # Set a new timer to clear the text box after 5 seconds (5000 milliseconds)
    timer = root.after(5000, clear_text)

# Create the main application window
root = tk.Tk()
root.title("My Tkinter Window")
root.geometry("600x400")  # Width x Height

# Add a label to the window
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 18))
label.pack(pady=20)

# Add a big text box to the window
text_box = tk.Text(root, wrap='word', font=("Arial", 12), width=50, height=10)
text_box.pack(pady=20)

# Initialize the timer variable
timer = None

# Bind the <KeyRelease> event to the text box to start the timer after writing
text_box.bind('<KeyRelease>', start_clear_timer)

# Add a button to the window


# Run the application
root.mainloop()
