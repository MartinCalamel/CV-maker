from concurrent.futures import thread
import webbrowser
import os
import sys
import time
import subprocess
import pyautogui
import signal

def save_cv(html_file : str, cv_name : str) -> None :

    cv_html_file = html_file
    
    os.chdir("code/site/")

    server = subprocess.Popen(["python", "-m", "http.server", "8000"])

    webbrowser.open(f'http://localhost:8000/{cv_html_file}')
    time.sleep(5)

    pyautogui.hotkey("ctrl", "p")
    time.sleep(3)

    pyautogui.press("enter")
    time.sleep(3)

    pyautogui.typewrite(cv_name)
    pyautogui.press("enter")

    os.kill(server.pid, signal.SIGTERM)
    
    return None

if __name__ == "__main__":
    save_cv("index.html","Martin CV")