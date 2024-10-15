# **Resolution Changer**

## **Description**

**Resolution Changer** is a lightweight Python tool that allows users to easily switch screen resolutions from the system tray. It provides a simple way to adjust display resolutions without going through system settings manually. This tool is ideal for users who frequently switch between different resolutions for **presentations, gaming, or development purposes**.

---

## **Features**

- **Change resolution** directly from the system tray.
- **Predefined resolutions** (e.g., 1920x1080, 1280x960) for quick switching.
- **Tray icon for easy access** without interrupting your workflow.
- **Toast notifications** to confirm resolution changes.
- **Batch script support** for startup usage.
- Simple and lightweight with **minimal dependencies**.

---

## **Installation**

### **1. Clone the Repository:**

```bash
git clone https://github.com/SulaimanS11/Resolution-Changer.git
cd Resolution-Changer
```
### **2. Install Dependencies:**

Ensure you have Python 3.x installed on your system. Install the required Python packages using:
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Running the Application:**

1. Open the terminal and navigate to the Resolution-Changer directory.
2. Run the following command to start the tray icon application:
```bash
python src/ResTray.py
```
3. System Tray Icon:
  - The application will add an icon to your system tray.
  - Right-click the tray icon to see a menu with predefined resolutions and a "Quit" option.

### **Options:**

| **Option**           | **Description**                                   | **Example**                                      |
|----------------------|----------------------------------------------------|-------------------------------------------------|
| `1920x1080`      | Switches the resolution to 1920x1080 pixels.                           | `Select from the tray menu.`                   |
| `1280x960`           | Switches the resolution to 1280x960 pixels.          | `Select from the tray menu.`                    |
| `Quit`            | Exits the tray application. | `Select from the tray menu.`       |

---

## **Batch Processing with Startup Scripts**
You can add the tool to **startup** using the provided batch script:

1. Open Start_upScrpts.bat from the scripts folder.
2. Modify the path to match your Python environment and the ResTray.py file.
3. Add the batch file to Windows Startup:
- Press Win + R and type shell:startup.
- Copy the Start_upScrpts.bat file into the opened folder.

---

## **How It Works**

1. **Tray Icon:**
The tool uses the **pystray** library to create a system tray icon with a menu.

2. **Resolution Switching:**
When a resolution option is selected from the menu, the **Win32 API** is called to change the screen resolution using:
```bash
win32api.ChangeDisplaySettings(devmode, 0)
```
3. Notification:
**win10toast** is used to display a notification whenever the resolution is successfully changed or if an error occurs.

---

## **Supported Resolutions**

By default, the following resolutions are supported:
- 1920x1080
- 1280x960

You can customize the available resolutions by modifying the RESOLUTIONS list in the ResTray.py file:
```python
RESOLUTIONS = [
    ("1920x1080", 1920, 1080),
    ("1280x960", 1280, 960),
]
```

---

## **Limitation**
- **Windows-only:** The tool relies on **Win32 API**, so it works only on Windows operating systems.
- **Fixed Resolutions:** Only the predefined resolutions can be selected. You need to modify the code to add more resolutions.
- **Administrative Access:** In some cases, resolution changes might require administrator privileges.

---

## **Contributing**

Contributions are welcome! If you'd like to improve the project or add new features:

1. **Fork the repository.**
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request.**

---

## **Acknowledgments**

- Built with **Python**.
- Uses the **pystray** library for the system tray icon.
- Uses the **win32api** library to switch screen resolutions.
- **Toast notifications** are powered by the **win10toast** library.

---

## **Contact**

If you encounter any issues, have questions, or would like to suggest improvements, feel free to reach out or open an issue on the [GitHub Issues](https://github.com/SulaimanS11/Resolution-Changer/issues) page.

You can also contact me directly:

- **GitHub:** [SulaimanS11](https://github.com/SulaimanS11)
- **Email:** [sult2271@mylaurier.ca](mailto:sult2271@mylaurier.ca)
- **LinkedIn:** [Mir Sulaiman Sultan](https://www.linkedin.com/in/mirssultan/)

---

## **Changelog**
**v1.0.0**

- Initial release with:
  * Predefined resolutions (1920x1080, 1280x960).
  * System tray icon for quick switching.
  * Toast notifications for success or failure.

---

## **Future Improvements**

- Add support for custom resolutions via a settings file.
- Implement hotkey support for faster resolution switching.
- Add auto-detection of supported resolutions on the device.
- Develop a more intuitive graphical user interface (GUI) for non-technical users.
