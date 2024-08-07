# Purpose  : General purpose utility to display Dual clock on Desktop
# Author   : Aniket Khedkar
# Language : Python
# Version  : 1.0
# Date     : 07-08-2024

import tkinter as tk
from datetime import datetime
import pytz
import threading
import time

def update_clock():
    while True:
        # Get the current time in UTC
        utc_now = datetime.now(pytz.utc)

        # Convert UTC to IST and Central Time
        ist_time = utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
        central_time = utc_now.astimezone(pytz.timezone('America/Chicago'))

        # Format the times to include AM/PM
        ist_str = ist_time.strftime('%I:%M:%S %p\n%d:%m:%Y')
        central_str = central_time.strftime('%I:%M:%S %p\n%d:%m:%Y')

        # Update the labels
        ist_label.config(text=ist_str)
        central_label.config(text=central_str)

        # Wait for a second before updating the clock again
        time.sleep(1)
    #Loop Ends
#Def ends
    

# Create the main window
root = tk.Tk()
root.title('Futuristic Dual Clock Widget')
root.configure(bg='#0e0e0e')  # Dark background for a futuristic look

# Define a custom digital font if available
digital_font = ('DS-Digital', 18)

# Define the color for the text and the border
color = '#7cfc00'  # Bright green color

# Create frames for the clock labels with a border color
ist_frame = tk.Frame(root, bg=color, bd=1)
central_frame = tk.Frame(root, bg=color, bd=1)

# Create labels for the display names with a futuristic style
ist_name_label = tk.Label(root, text='IST Time - Bharat', font=('Calibri', 12), bg='#0e0e0e', fg='#7cfc00', borderwidth=2, relief='flat')
ist_name_label.pack()

# Create labels for IST Time
ist_label = tk.Label(ist_frame, font=digital_font, bg='#0e0e0e', fg='#7cfc00', borderwidth=2, relief='flat')
ist_label.pack(padx=2,pady=2)

# Pack the frames with a little padding to create the border effect
ist_frame.pack(padx=2, pady=2)
# Pack the labels into the frames
ist_label.pack()

# Create labels Central Time with a futuristic style
central_name_label = tk.Label(root, text='USA Time - Houston, Texas', font=('Calibri', 12), bg='#0e0e0e', fg='#7cfc00', borderwidth=2, relief='flat')
central_name_label.pack()

# Create labels for Central Time
central_label = tk.Label(central_frame, font=digital_font, bg='#0e0e0e', fg='#7cfc00', borderwidth=2, relief='flat')
central_label.pack(padx=2,pady=2)

# Pack the frames with a little padding to create the border effect
central_frame.pack(padx=2, pady=2)
# Pack the labels into the frames
central_label.pack()

# Start the thread that updates the clocks
clock_thread = threading.Thread(target=update_clock)
clock_thread.daemon = True
clock_thread.start()

# Run the main event loop
root.mainloop()