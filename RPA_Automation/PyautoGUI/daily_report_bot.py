import pyautogui
import time
import subprocess
from datetime import datetime

# =====================================================
# SETTINGS
# =====================================================

pyautogui.FAILSAFE = True

TYPE_SPEED = 0.08

# =====================================================
# STEP 1 - GET DATE & TIME
# =====================================================

now = datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")
date_str = now.strftime("%Y-%m-%d")

comment = "Daily sports update from ESPN"
source = "ESPN India Sports News"

print("===================================")
print("Starting Daily Report Bot...")
print("===================================")

# =====================================================
# STEP 2 - OPEN CHROME
# =====================================================

print("Opening Spotlight...")

time.sleep(5)

pyautogui.hotkey('command', 'space')

time.sleep(2)

print("Typing Chrome...")

pyautogui.write('chrome', interval=TYPE_SPEED)

time.sleep(1)

pyautogui.press('enter')

print("Chrome Opening...")

time.sleep(10)

# =====================================================
# STEP 3 - BRING CHROME TO FRONT
# =====================================================

subprocess.run([
    "osascript",
    "-e",
    'tell application "Google Chrome" to activate'
])

time.sleep(2)

# =====================================================
# STEP 4 - OPEN ESPN
# =====================================================

print("Opening ESPN...")

pyautogui.hotkey('command', 'l')

time.sleep(2)

pyautogui.write(
    'https://www.espn.in/',
    interval=0.05
)

time.sleep(1)

pyautogui.press('enter')

print("Waiting for ESPN to load...")

time.sleep(8)

# =====================================================
# STEP 5 - COPY CONTENT
# =====================================================

print("Copying ESPN Content...")

pyautogui.hotkey('command', 'a')

time.sleep(2)

pyautogui.hotkey('command', 'c')

time.sleep(2)

print("Content Copied")

# =====================================================
# STEP 6 - OPEN EXCEL
# =====================================================

print("Opening Excel...")

pyautogui.hotkey('command', 'space')

time.sleep(2)

pyautogui.write('excel', interval=TYPE_SPEED)

time.sleep(1)

pyautogui.press('enter')

print("Waiting for Excel...")

time.sleep(10)

# =====================================================
# STEP 7 - CREATE NEW WORKBOOK
# =====================================================

print("Creating New Workbook...")

pyautogui.hotkey('command', 'n')

time.sleep(8)

# If Excel template screen appears
pyautogui.press('enter')

time.sleep(5)

print("Workbook Ready")

# =====================================================
# STEP 8 - CREATE HEADERS
# =====================================================

print("Adding Headers...")

pyautogui.write(
    "Date & Time",
    interval=TYPE_SPEED
)

pyautogui.press('tab')

pyautogui.write(
    "Source",
    interval=TYPE_SPEED
)

pyautogui.press('tab')

pyautogui.write(
    "Comment",
    interval=TYPE_SPEED
)

pyautogui.press('enter')

time.sleep(2)

# =====================================================
# STEP 9 - ADD REPORT DATA
# =====================================================

print("Adding Report Data...")

pyautogui.write(
    date_time,
    interval=TYPE_SPEED
)

pyautogui.press('tab')

pyautogui.write(
    source,
    interval=TYPE_SPEED
)

pyautogui.press('tab')

pyautogui.write(
    comment,
    interval=TYPE_SPEED
)

pyautogui.press('enter')

print("Report Row Added")

time.sleep(2)

# =====================================================
# STEP 10 - SAVE FILE
# =====================================================

print("Saving Workbook...")

pyautogui.hotkey('command', 's')

time.sleep(5)

filename = f"daily_report_{date_str}"

pyautogui.write(
    filename,
    interval=TYPE_SPEED
)

time.sleep(2)

pyautogui.press('enter')

print("Workbook Saved")

time.sleep(5)

# =====================================================
# STEP 11 - TAKE SCREENSHOT
# =====================================================

print("Taking Screenshot...")

screenshot = pyautogui.screenshot()

screenshot.save(
    f"daily_report_{date_str}.png"
)

print("Screenshot Saved")

time.sleep(2)

# =====================================================
# STEP 12 - FINISH
# =====================================================

print("===================================")
print("Assignment Completed Successfully!")
print("===================================")

print(f"Excel File : {filename}")
print(f"Screenshot : daily_report_{date_str}.png")