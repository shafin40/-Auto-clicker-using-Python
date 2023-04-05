# Import necessary libraries
import pyautogui
import keyboard

# Print instructions for the user
print("Press 'm' to start/stop clicking")

# Set initial clicking state to False and done state to False
clicking = False
done = False

# Start infinite loop until done is True
while not done:
    # If 'm' key is pressed, toggle clicking state
    if keyboard.is_pressed('m'):
        if not clicking:
            print("Clicking started")
            clicking = True
        else:
            print("Clicking stopped")
            clicking = False
    # If 'q' key is pressed, exit the loop
    elif keyboard.is_pressed('q'):
        done = True

    # If clicking state is True, simulate mouse clicks using pyautogui
    if clicking:
        pyautogui.click(clicks=100, interval=0.01)

# Print "Done" when loop is exited
print("Done")
