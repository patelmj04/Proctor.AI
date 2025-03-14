# ProctorAI

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)

**ProctorAI** is an AI-powered tool for monitoring student behavior during online proctored exams. Using computer vision and machine learning, it detects suspicious activities, tracks eye movements, and ensures exam integrity.

## Key Features
- **Eye Tracking**: Monitors eye closure and unusual movements via Eye Aspect Ratio (EAR).
- **Head Movement Detection**: Flags excessive head motion as potential cheating.
- **Face Monitoring**: Alerts on multiple faces or no face detection.
- **Real-Time Alerts**: Displays warnings on-screen during monitoring.
- **Activity Logging**: Records suspicious events with timestamps.

## Installation

### Requirements
- Python 3.8+
- Webcam
- Adequate lighting

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/patelmj04/ProctorAI.git
   cd ProctorAI
   ```

2. **Set Up Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install opencv-python dlib numpy scipy imutils
   ```

4. **Download Facial Landmark Model**
   - Download `shape_predictor_68_face_landmarks.dat` from [dlib.net](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2).
   - Extract and place it in the project root.

## Usage
1. **Run the Application**
   ```bash
   python proctor.py
   ```
2. Position yourself in front of the webcam.
3. Press `q` to stop the session.
4. Review `proctoring_log.txt` for logged alerts.

## How It Works
- **Face Detection**: Uses dlib's frontal face detector to identify faces.
- **Eye Tracking**: Calculates EAR to detect eye closure or shifts.
- **Movement Analysis**: Tracks head position changes for suspicious activity.
- **Alert System**: Logs and displays real-time warnings.

## Customization
Modify these parameters in `proctor.py`:
- `EYE_AR_THRESH` (0.25): Eye closure sensitivity.
- `EYE_AR_CONSEC_FRAMES` (20): Frames needed to trigger an eye closure alert.
- `SUSPICIOUS_MOVEMENT_THRESH` (50): Head movement threshold.

## Limitations
- Requires good lighting and camera positioning.
- Basic ML model—accuracy can be improved with deep learning.
- May need tuning for diverse face shapes or distances.

## Future Enhancements
- Audio monitoring integration.
- Screen recording capabilities.
- Deep learning for enhanced detection.
- Remote reporting and database support.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Submit a Pull Request.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
- **PatelMJ04**  
  GitHub: [patelmj04](https://github.com/patelmj04)

## Acknowledgments
- Built with [OpenCV](https://opencv.org/), [dlib](http://dlib.net/), and open-source tools.
- Inspired by the demand for secure online exam solutions.

---

### Notes
- **Headings**: Used `#` for the main title, `##` for sections, and `###` for subsections to improve hierarchy.
- **GitHub Setup**: Push this to your repo with:
  ```bash
  git init
  git add README.md proctor.py
  git commit -m "Initial commit with README and code"
  git remote add origin https://github.com/patelmj04/ProctorAI.git
  git push -u origin main
  ```
