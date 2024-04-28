import datetime
import time

# Constants for light schedules
light_schedules = [
    ('07:00', '09:00'),  # Morning schedule
    ('18:00', '23:00')   # Evening schedule
]

def control_light(turn_on):
    if turn_on:
        print("Light turned on")
    else:
        print("Light turned off")

def is_within_schedule(now, start, end):
    start_time = datetime.datetime.strptime(start, '%H:%M').time()
    end_time = datetime.datetime.strptime(end, '%H:%M').time()
    return start_time <= now.time() <= end_time

def check_and_update_lights():
    now = datetime.datetime.now()
    light_on = any(is_within_schedule(now, start, end) for start, end in light_schedules)
    control_light(light_on)

def main():
    while True:
        check_and_update_lights()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":

    main()
# Bathrooom or Hall lights working for automatic
import time
from unittest.mock import patch, MagicMock

# Constants for the API
LIGHT_API_URL = "http://example.com/api/light"  # Example API endpoint
MOTION_SENSOR_STATUS_URL = "http://example.com/api/motion"  # Example API endpoint
HEADERS = {'Authorization': 'Bearer your_api_token'}

def get_motion_sensor_status():
    response = requests.get(MOTION_SENSOR_STATUS_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['motion_detected']
    else:
        print(f"Failed to get sensor status: {response.status_code} {response.text}")
        return False

def control_light(turn_on):
    data = {'on': turn_on}
    response = requests.post(LIGHT_API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        print("Light turned", "on" if turn_on else "off")
    else:
        print(f"Failed to control light: {response.status_code} {response.text}")

def main():
    last_status = False
    while True:
        current_status = get_motion_sensor_status()
        if current_status != last_status:
            control_light(current_status)
            last_status = current_status
        time.sleep(1)  # Check every second

# Creating a mock response object for get
mock_get_response = MagicMock()
mock_get_response.status_code = 200
mock_get_response.json.return_value = {'motion_detected': True}

# Creating a mock response object for post
mock_post_response = MagicMock()
mock_post_response.status_code = 200

# Using unittest.mock to patch 'requests.get' and 'requests.post' calls
with patch('requests.get', return_value=mock_get_response), \
     patch('requests.post', return_value=mock_post_response):
    if name == "main":
        main()

#For Blindfolds working system automatic
import datetime
import time
import requests  # Ensure this import is included
from unittest.mock import patch, MagicMock

# Constants
BRIGHTNESS_SENSOR_URL = "http://your-brightness-sensor-api.com/brightness"
HEADERS = {'Authorization': 'Bearer your_api_token'}
BRIGHTNESS_THRESHOLD = 80  # Example threshold value for brightness level
TIME_START = "08:00"  # Start time in HH:MM format
TIME_END = "18:00"  # End time in HH:MM format

def get_current_brightness():
    # Fetch the current brightness from the sensor.
    response = requests.get(BRIGHTNESS_SENSOR_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()['brightness']
    else:
        print("Failed to fetch brightness")
        return None

def is_within_time_range():
    # Check if current time is within the specified range.
    now = datetime.datetime.now()
    start_time = datetime.datetime.strptime(TIME_START, '%H:%M').time()
    end_time = datetime.datetime.strptime(TIME_END, '%H:%M').time()
    return start_time <= now.time() <= end_time

def control_blinds(close):
    # Simulate sending a command to control the blinds.
    if close:
        print("Closing blinds")
    else:
        print("Opening blinds")

def main():
    while True:
        current_brightness = get_current_brightness()
        if current_brightness is not None:
            if current_brightness > BRIGHTNESS_THRESHOLD and is_within_time_range():
                control_blinds(True)
            else:
                control_blinds(False)
        time.sleep(60)  # Check every minute

# Creating a mock response object for get
mock_get_response = MagicMock()
mock_get_response.status_code = 200
mock_get_response.json.return_value = {'brightness': 85}  # Example mock brightness above threshold

# Using unittest.mock to patch 'requests.get' call
with patch('requests.get', return_value=mock_get_response):
    if name == "main":
        main()


#Override system to make it manual.
import tkinter as tk
import datetime
import time
from threading import Thread

# Predefined schedules that can be overridden by user input
light_schedules = []

def turn_on():
    print("Turned On successfully")
    create_appliance_window()

def turn_off():
    print("Turned Off successfully")
    root.destroy()

def create_appliance_window():
    top = tk.Toplevel()
    top.title("Select Appliance")
    top.geometry("500x250")

    label = tk.Label(top, text="Which appliance do you need to change to manual?",
                     wraplength=500)
    label.pack(pady=20)

    frame = tk.Frame(top)
    frame.pack()

    blindfolds_button = tk.Button(frame, text="Blindfolds", command=create_blindfolds_interface, width=20, height=4)
    blindfolds_button.pack(side=tk.LEFT, padx=20, pady=10)

    light_bulbs_button = tk.Button(frame, text="Light Bulbs", command=create_light_interface, width=20, height=4)
    light_bulbs_button.pack(side=tk.LEFT, padx=20, pady=10)

def create_blindfolds_interface():
    top = tk.Toplevel()
    top.title("Blindfolds Control")
    top.geometry("500x250")

    label = tk.Label(top, text="For what duration do you want your blindfolds to be closed?",
                     wraplength=500)
    label.pack(pady=20)

    frame = tk.Frame(top)
    frame.pack()

    set_duration_button = tk.Button(frame, text="Set Duration", command=set_blindfold_schedule, width=20, height=4)
    set_duration_button.pack(padx=20, pady=10)
def set_blindfold_schedule():
    top = tk.Toplevel()
    top.title("Set Blindfolds Schedule")
    top.geometry("500x250")

    start_label = tk.Label(top, text="Enter start time for blindfolds to be closed (HH:MM):")
    start_label.pack()

    start_entry = tk.Entry(top, width=10)
    start_entry.pack()

    end_label = tk.Label(top, text="Enter end time for blindfolds to be closed (HH:MM):")
    end_label.pack()

    end_entry = tk.Entry(top, width=10)
    end_entry.pack()

    def submit_schedule():
        start = start_entry.get()
        end = end_entry.get()
        try:
            datetime.datetime.strptime(start, '%H:%M')
            datetime.datetime.strptime(end, '%H:%M')
            if start < end:
                print(f"Blindfolds schedule set from {start} to {end}")
                top.destroy()
            else:
                tk.messagebox.showerror("Error", "Start time must be before end time.")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")

    submit_button = tk.Button(top, text="Submit", command=submit_schedule)
    submit_button.pack(pady=10)

def blindfold_control_loop():
    """Continuously checks and updates the blindfold status based on the user-defined schedule."""
    while True:
        now = datetime.datetime.now()
        blindfold_closed = False
        for schedule in blindfold_schedules:
            start, end = schedule
            start_time = datetime.datetime.strptime(start, '%H:%M').time()
            end_time = datetime.datetime.strptime(end, '%H:%M').time()
            if start_time <= now.time() <= end_time:
                blindfold_closed = True
                break
        if blindfold_closed:
            print("Blindfolds are CLOSED")
        else:
            print("Blindfolds are OPEN")
        time.sleep(60)  # Check every minute

def create_light_interface():
    top = tk.Toplevel()
    top.title("Light Bulbs Schedule")
    top.geometry("500x250")

    label = tk.Label(top, text="At what time do you want your lights to be on?",
                     wraplength=500)
    label.pack(pady=20)

    frame = tk.Frame(top)
    frame.pack()

    morning_button = tk.Button(frame, text="Set Morning Schedule", command=lambda: set_schedule('morning'), width=20, height=4)
    morning_button.pack(side=tk.LEFT, padx=20, pady=10)

    evening_button = tk.Button(frame, text="Set Evening Schedule", command=lambda: set_schedule('evening'), width=20, height=4)
    evening_button.pack(side=tk.LEFT, padx=20, pady=10)

def set_schedule(period):
    top = tk.Toplevel()
    top.title(f"Set {period.capitalize()} Schedule")
    top.geometry("500x250")

    start_label = tk.Label(top, text=f"Enter start time for the {period} schedule (HH:MM):")
    start_label.pack()

    start_entry = tk.Entry(top, width=10)
    start_entry.pack()

    end_label = tk.Label(top, text=f"Enter end time for the {period} schedule (HH:MM):")
    end_label.pack()

    end_entry = tk.Entry(top, width=10)
    end_entry.pack()

    def submit_schedule():
        start = start_entry.get()
        end = end_entry.get()
        try:
            # Validate time format
            datetime.datetime.strptime(start, '%H:%M')
            datetime.datetime.strptime(end, '%H:%M')
            if start < end:
                # Override or set new schedule
                light_schedules.append((period, start, end))
                print(f"{period.capitalize()} schedule set from {start} to {end}")
                top.destroy()
            else:
                tk.messagebox.showerror("Error", "Start time must be before end time.")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format. Please use HH:MM format.")

    submit_button = tk.Button(top, text="Submit", command=submit_schedule)
    submit_button.pack(pady=10)

def light_control_loop():
    # Continuously checks and updates the light status based on the user-defined schedule.
    while True:
        now = datetime.datetime.now()
        light_on = False
        for schedule in light_schedules:
            period, start, end = schedule
            start_time = datetime.datetime.strptime(start, '%H:%M').time()
            end_time = datetime.datetime.strptime(end, '%H:%M').time()
            if start_time <= now.time() <= end_time:
                light_on = True
                break
        if light_on:
            print("Light turned ON")
        else:
            print("Light turned OFF")
        time.sleep(60)  # Check every minute

# Run the light control loop in a separate thread
thread = Thread(target=light_control_loop)
thread.daemon = True
thread.start()

root = tk.Tk()
root.title("Control Interface")
root.geometry("500x250")

label = tk.Label(root, text="Do you want to change from Automatic to Manual for some time?",
                 wraplength=500)
label.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

on_button = tk.Button(frame, text="On", command=turn_on, width=20, height=4)
on_button.pack(side=tk.LEFT, padx=20, pady=10)

off_button = tk.Button(frame, text="Off", command=turn_off, width=20, height=4)
off_button.pack(side=tk.LEFT, padx=20, pady=10)

root.mainloop()

