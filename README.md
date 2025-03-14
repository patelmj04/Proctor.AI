
# ProctorAI

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)

**ProctorAI** is an advanced AI-powered tool designed to monitor student behavior during online proctored exams. Combining computer vision via Mediapipe, machine learning techniques, and a minimalistic Tkinter GUI, it ensures exam integrity with real-time monitoring and logging.
![image](https://github.com/user-attachments/assets/9a85566e-4fe8-43fa-805d-d25c3a65d517)


## Advanced Features

### Eye Tracking
- **Description**: Monitors eye closure and unusual movements using the Eye Aspect Ratio (EAR).
- **Implementation**: Calculates EAR from Mediapipe’s facial landmarks (left eye: `[33, 160, 158, 133, 153, 144]`, right eye: `[362, 385, 387, 263, 373, 380]`).
- **Advantage**: Detects potential cheating behaviors like prolonged eye closure with customizable sensitivity.
![image](https://github.com/user-attachments/assets/4c671668-64da-4090-990c-b9f74a279237)


### Head Movement Detection
- **Description**: Flags excessive head motion as suspicious activity.
- **Implementation**: Tracks the nose tip (landmark `1`) and measures movement using Euclidean distance, with a threshold of 50 pixels.
- **Advantage**: Identifies consistent head turning or shifting, indicating possible off-screen glances.
![image](https://github.com/user-attachments/assets/d61bdfe2-d698-4357-a3e9-74daa9335195)
### Face Monitoring
- **Description**: Detects and alerts on multiple faces or absence of a face.
- **Implementation**: Uses Mediapipe’s Face Mesh to limit detection to 2 faces, ensuring a single examinee.
- **Advantage**: Prevents impersonation or collaboration during exams.

### Real-Time Alerts
- **Description**: Displays immediate warnings on both the video feed and GUI.
- **Implementation**: Integrates `cv2.putText()` for video alerts and a Tkinter scrolled text box for GUI updates via a callback.
- **Advantage**: Provides instant feedback to proctors without delay.
![image](https://github.com/user-attachments/assets/ff2fdeef-a6f2-43fb-933b-9196e8f65f7f)

### Activity Logging
- **Description**: Records all suspicious events with timestamps for post-exam review.
- **Implementation**: Stores alerts in memory and saves them to `proctoring_log.txt` upon session end.
- **Advantage**: Enables detailed analysis and evidence collection.
![image](https://github.com/user-attachments/assets/495dd6bb-d498-4939-8077-fddef05b9c57)
![image](https://github.com/user-attachments/assets/77e5d72b-e2c9-412a-a8e1-6e261b81ac9d)


### GUI Integration
- **Description**: Offers a minimalistic front-end for easy control and monitoring.
- **Implementation**: Built with Tkinter, featuring Start/Stop buttons, a real-time alert display, and log viewer.
- **Advantage**: User-friendly interface that runs alongside video processing in a separate thread.
![Uploading image.png…]()


## Installation

### Requirements
- Python 3.8+
- Webcam
- Stable internet (for initial package installation)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/patelmj04/ProctorAI.git
   cd ProctorAI
   ```

2. **Set Up Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install opencv-python mediapipe numpy scipy
   ```
   - Note: Tkinter is included with Python; no additional installation needed.

## Usage
1. **Run the Application**
   ```bash
   python proctor.py
   ```
2. **Interact with the GUI**:
   - Click **"Start Proctoring"** to begin monitoring (webcam feed opens separately).
   - View real-time alerts in the scrolled text box.
   - Click **"Stop Proctoring"** to end the session.
   - Click **"View Log"** to display `proctoring_log.txt` contents.
3. **Exit**: Close the GUI window or press `q` in the webcam feed.

## How It Works
- **Back-End**: Mediapipe processes webcam frames for face and landmark detection, feeding data to behavior analysis algorithms.
- **Front-End**: Tkinter GUI runs in the main thread, while proctoring runs in a separate thread for responsiveness.
- **Integration**: Alerts are passed from the back-end to the GUI via a callback function.

## Customization
Adjust these parameters in `proctor.py`:
- `EYE_AR_THRESH` (0.25): Sensitivity for eye closure detection.
- `EYE_AR_CONSEC_FRAMES` (20): Frames required to trigger an eye closure alert.
- `SUSPICIOUS_MOVEMENT_THRESH` (50): Threshold for head movement detection.

## Limitations
- Requires consistent lighting and camera alignment.
- Basic ML approach—could benefit from deep learning for higher accuracy.
- GUI is minimalistic; no embedded video feed (runs separately).

## Future Enhancements
- Integrate deep learning models for improved detection.
- Embed webcam feed in the GUI using PIL and Tkinter Canvas.
- Add audio monitoring and screen recording capabilities.
- Implement remote alert notifications.

## Contributing
1. Fork the repository.
2. Create a branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
- **PatelMJ04**  
  GitHub: [patelmj04](https://github.com/patelmj04)

## Acknowledgments
- Powered by [Mediapipe](https://mediapipe.dev/), [OpenCV](https://opencv.org/), and Python’s Tkinter.
- Inspired by the need for robust online exam proctoring solutions.

---

### Notes
- **File Setup**: Save this as `README.md` in your project directory alongside `proctor.py`.
- **GitHub Push**:
  ```bash
  git init
  git add proctor.py README.md
  git commit -m "Add ProctorAI with GUI and README"
  git remote add origin https://github.com/patelmj04/ProctorAI.git
  git push -u origin main
  ```
