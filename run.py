import os
import sys
import subprocess

def install_dependencies():
    try:
        import tensorflow
        import keras
        import cv2
        import pyautogui
        import numpy
        import h5py
    except ImportError:
        print("[INFO] Installing missing dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def start_ai():
    print("[INFO] Starting Clash Royale AI...")
    os.system("python main.py")

if __name__ == "__main__":
    install_dependencies()
    start_ai()
