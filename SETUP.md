# *Clash Royale AI Setup Guide*

*This guide provide*s installation instructions for running the Clash Royale AI bot on **Chromebook, Linux, Windows**, and **Mac**.

## 🚀 Supported Platforms

### ✅ Chromebook & Linux (Fully Supported)

The AI can be run natively with Linux dependencies.

### ❓ Windows (Requires Emulator - Not Tested Yet)

Windows users will need to use **WSL (Windows Subsystem for Linux)** or a **virtual machine**. Compatibility is unverified.

### ❓ Mac (Possibly Supported, Not Tested)

Mac users may need to adjust installation steps for macOS dependencies.

---

## 🖥️ Installation Instructions

### 📌 **For Chromebook & Linux**

#### 1️⃣ Enable Developer Mode & Linux (Chromebooks only)

1. Hold `Esc` + `Refresh` + Press `Power`
2. Press `Ctrl + D` and follow the on-screen instructions (This will wipe your local data!)
3. Enable Linux (Beta):
   - Go to **Settings** → **Advanced** → **Developers** → **Linux development environment** → **Turn on**

#### 2️⃣ Install Dependencies

Open a **Linux terminal** and run:

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y \
    python3-pip \
    python3-opencv \
    scrot \
    xdotool \
    x11-utils \
    libxcb-xtest0 \
    libxcb-xinerama0 \
    x11-xserver-utils \
    xinput \
    xvfb

# Install Python packages
pip3 install \
    tensorflow==2.12.0 \
    pyautogui==0.9.53 \
    mss==9.0.1 \
    numpy==1.24.3 \
    opencv-python==4.7.0.72
```

#### 3️⃣ Clone and Run the AI

```bash
# Clone repository
git clone https://github.com/FrostdogFN/Clash-royale-Machine-learning.git
cd Clash-royale-Machine-learning

# Grant necessary permissions
sudo chmod 777 /dev/uinput

# Run in test mode first
python3 src/main.py --test-mode --no-input

# Run AI with Chromebook mode
python3 src/main.py --chromebook-mode
```

---

### 📌 **For Windows (Experimental - Requires Emulator)**

1. **Option 1: Use Windows Subsystem for Linux (WSL)**

   - Install WSL: `wsl --install`
   - Install Ubuntu from the Microsoft Store
   - Follow the **Linux installation steps above**

2. **Option 2: Use a Virtual Machine**

   - Install VirtualBox or VMware
   - Set up an Ubuntu VM
   - Follow the **Linux installation steps above**

⚠️ **Windows compatibility is not confirmed yet. Let us know if you test it!**

---

### 📌 **For Mac (Not Tested Yet)**

1. Install Homebrew (if not installed):
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install dependencies:
   ```bash
   brew install python3 opencv xdotool
   pip3 install tensorflow pyautogui mss numpy opencv-python
   ```
3. Clone and run the AI:
   ```bash
   git clone https://github.com/FrostdogFN/Clash-royale-Machine-learning.git
   cd Clash-royale-Machine-learning
   python3 src/main.py --test-mode --no-input
   ```

⚠️ **Mac compatibility is unknown. Let us know if it works!**

---

## ❗ Troubleshooting

| Issue                    | Fix                                        |
| ------------------------ | ------------------------------------------ |
| `pyautogui` not clicking | Run with `sudo` or grant input permissions |
| Screen capture fails     | Use a virtual display with `Xvfb`          |
| TensorFlow too slow      | Use TensorFlow Lite (`model.tflite`)       |

To run in a virtual display:

```bash
Xvfb :1 -screen 0 1024x768x24 &
DISPLAY=:1 python3 src/main.py
```

---

## 💡 Performance Optimization

### 🏎️ Use TensorFlow Lite

Modify `model.py`:

```python
import tflite_runtime.interpreter as tflite

def load_model(model_path):
    interpreter = tflite.Interpreter(model_path="model.tflite")
    interpreter.allocate_tensors()
    return interpreter
```

### 🚀 Limit Memory Usage

```bash
ulimit -Sv 1000000  # Limit to 1GB RAM
python3 src/main.py
```

---

## ❤️ Contributing

If you successfully run the AI on **Windows** or **Mac**, please submit a pull request or report your findings!

---

## 📌 Credits

Developed by **FrostdogFN**

---

Thanks for supporting me!
