import cv2
import mediapipe as mp

def human_detection():

    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    cap = cv2.VideoCapture("wagya2.mp4")

    # Set the desired frame number
    desired_frame_number = 1  # Change this to the frame number you want

    # Initialize a counter variable
    frame_count = 0

    while True:
        ret, img = cap.read()
        if not ret:
            break

        frame_count += 1

        if frame_count == desired_frame_number:
            img = cv2.resize(img, (400, 800))

            results = pose.process(img)

            if results.pose_landmarks:
                # Get image dimensions
                h, w, c = img.shape

                # Extract 2D pixel coordinates of landmarks
                landmark_px = []
                for landmark in results.pose_landmarks.landmark:
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)
                    landmark_px.append((x, y))

                # Print 2D pixel coordinates
                print(f"Landmarks for frame {frame_count}:")
                print(landmark_px)

                # Draw the landmarks on the original image
                mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_draw.DrawingSpec((255, 0, 0), 2, 2),
                                    mp_draw.DrawingSpec((255, 0, 255), 5, 5))

                # Display pose on original video/live stream
                cv2.imshow("Pose Estimation", img)

                # Exit the loop after obtaining landmarks for the desired frame
                break

        cv2.waitKey(1)

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()
    
    return landmark_px