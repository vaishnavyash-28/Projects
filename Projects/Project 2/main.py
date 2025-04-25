import pyautogui
import time
import pyperclip

# Pause to allow switching to the correct screen (e.g., 3 seconds)
time.sleep(3)

# Step 1: Click the icon
pyautogui.click(1803, 59)
time.sleep(1)  # Wait for any response (e.g., window opening)

# Step 2: Drag to select the text
pyautogui.moveTo(1149, 164)
pyautogui.mouseDown()
pyautogui.moveTo(1825, 976, duration=1)  # Drag duration makes it smoother
pyautogui.mouseUp()
time.sleep(0.5)

# Step 3: Copy the text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for clipboard to update

# Step 4: Retrieve from clipboard
copied_text = pyperclip.paste()

print("Copied text:")
print(copied_text)
