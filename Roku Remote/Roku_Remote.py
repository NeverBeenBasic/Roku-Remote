import requests
import tkinter as tk

# Set the IP address of your Roku TV
ip_address = input("Enter the IP address of your Roku TV: ")

# Define the URL of the Roku API endpoint
url = f"http://{ip_address}:8060/keypress/"

# Define the key codes for various commands
key_codes = {
    "home": "Home",
    "back": "Back",
    "up": "Up",
    "down": "Down",
    "left": "Left",
    "right": "Right",
    "select": "Select",
    "play": "Play",
    "pause": "Play",
    "forward": "Forward",
    "reverse": "Reverse",
    "volume_up": "VolumeUp",
    "volume_down": "VolumeDown",
}

# Define a function to send a key press command to the Roku TV
def send_key(key):
    if key in key_codes:
        key_code = key_codes[key]
        requests.post(url + key_code)
    else:
        print(f"Invalid key: {key}")

# Define a function to create the Roku remote GUI
def create_remote():
    # Create the main window and set its title
    window = tk.Tk()
    window.title("Roku Remote")

    # Define the buttons for various commands
    buttons = [
        ["back", "home", "select"],
        ["reverse", "play", "forward"],
        ["volume_down", "up", "volume_up"],
        ["left", "down", "right"]
    ]

    # Define a function to create a button with a command
    def create_button(frame, key):
        if key is None:
            return
        button = tk.Button(frame, text=key, font=("Arial", 16), padx=20, pady=10, command=lambda: send_key(key))
        button.pack(side=tk.LEFT, padx=5, pady=5)

    # Create a button frame for each row of buttons
    for row in buttons:
        frame = tk.Frame(window)
        frame.pack()
        for key in row:
            create_button(frame, key)

    # Start the main loop to handle GUI events
    window.mainloop()

# Create the Roku remote GUI
create_remote()
