
import cv2
import numpy as np
import mediapipe as mp
from scipy.spatial import distance as dist
import time
from datetime import datetime

class ExamProctor:
    def __init__(self):
        # Initialize Mediapipe Face Mesh
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils

        # Thresholds and counters
        self.EYE_AR_THRESH = 0.25
        self.EYE_AR_CONSEC_FRAMES = 20
        self.SUSPICIOUS_MOVEMENT_THRESH = 50
        self.counter = 0
        self.alerts = []
        
        # Video capture
        self.cap = cv2.VideoCapture(0)
        
        # Movement tracking
        self.prev_position = None
        self.suspicious_count = 0

    def eye_aspect_ratio(self, eye_landmarks, landmarks, image_shape):
        """Calculate the eye aspect ratio (EAR) using Mediapipe landmarks"""
        h, w = image_shape[:2]
        eye_coords = [(int(landmarks[p].x * w), int(landmarks[p].y * h)) for p in eye_landmarks]
        A = dist.euclidean(eye_coords[1], eye_coords[5])
        B = dist.euclidean(eye_coords[2], eye_coords[4])
        C = dist.euclidean(eye_coords[0], eye_coords[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def detect_suspicious_behavior(self, frame):
        """Detect suspicious behavior including eye movement and head position"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)

        if results.multi_face_landmarks:
            if len(results.multi_face_landmarks) > 1:
                self.alerts.append(f"[{datetime.now()}] Multiple faces detected")
                cv2.putText(frame, "MULTIPLE FACES DETECTED!", (10, 90),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                return frame

            # Process single face
            face_landmarks = results.multi_face_landmarks[0].landmark
            
            # Define eye landmark indices (Mediapipe uses different indices than dlib)
            LEFT_EYE = [33, 160, 158, 133, 153, 144]  # Approximate left eye points
            RIGHT_EYE = [362, 385, 387, 263, 373, 380]  # Approximate right eye points

            # Calculate eye aspect ratio
            leftEAR = self.eye_aspect_ratio(LEFT_EYE, face_landmarks, frame.shape)
            rightEAR = self.eye_aspect_ratio(RIGHT_EYE, face_landmarks, frame.shape)
            ear = (leftEAR + rightEAR) / 2.0

            if ear < self.EYE_AR_THRESH:
                self.counter += 1
                if self.counter >= self.EYE_AR_CONSEC_FRAMES:
                    self.alerts.append(f"[{datetime.now()}] Potential cheating: Eyes closed")
                    cv2.putText(frame, "EYES CLOSED!", (10, 30),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            else:
                self.counter = 0

            # Head movement detection (using nose tip as reference)
            nose_tip = (int(face_landmarks[1].x * frame.shape[1]), int(face_landmarks[1].y * frame.shape[0]))
            if self.prev_position is not None:
                movement = dist.euclidean(self.prev_position, nose_tip)
                if movement > self.SUSPICIOUS_MOVEMENT_THRESH:
                    self.suspicious_count += 1
                    if self.suspicious_count > 5:
                        self.alerts.append(f"[{datetime.now()}] Suspicious head movement detected")
                        cv2.putText(frame, "SUSPICIOUS MOVEMENT!", (10, 60),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    self.suspicious_count = max(0, self.suspicious_count - 1)
            self.prev_position = nose_tip

            # Draw eye regions (optional visualization)
            for idx in LEFT_EYE + RIGHT_EYE:
                pt = (int(face_landmarks[idx].x * frame.shape[1]), int(face_landmarks[idx].y * frame.shape[0]))
                cv2.circle(frame, pt, 2, (0, 255, 0), -1)

        else:
            self.alerts.append(f"[{datetime.now()}] No face detected")
            cv2.putText(frame, "NO FACE DETECTED!", (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        return frame

    def run(self):
        """Main loop for proctoring"""
        print("Starting exam proctoring... Press 'q' to quit")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture video")
                break

            frame = self.detect_suspicious_behavior(frame)

            cv2.imshow("Exam Proctor", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cleanup()

    def cleanup(self):
        """Clean up resources and save alerts"""
        self.cap.release()
        cv2.destroyAllWindows()
        self.face_mesh.close()
        
        with open("proctoring_log.txt", "w") as f:
            f.write("\n".join(self.alerts))
        print("Proctoring ended. Alerts saved to proctoring_log.txt")

    def __del__(self):
        self.cleanup()

if __name__ == "__main__":
    proctor = ExamProctor()
    try:
        proctor.run()
    except KeyboardInterrupt:
        proctor.cleanup()