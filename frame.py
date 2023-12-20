# 0 and 7 nose to ear (50% variance)
# 11,12 and 23,24 shoulder to hip
import cv2
import argparse
import mediapipe as mp
from utils import is_point_inside_circle, is_point_inside_rectangle

SCORE = 0

if __name__ == "__main__":
        # Initialize argument parser
    parser = argparse.ArgumentParser(description="Process video with pose estimation.")
    
    # Add argument for video filename
    parser.add_argument('--video', type=str, required=True, help='Path to the input video file.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Use the video filename from the command-line arguments
    video = args.video

    # Initialize mediapipe pose solution
    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils
    pose = mp_pose.Pose()
    # Take video input for pose detection
    cap = cv2.VideoCapture(video)

    # Skip to the Nth frame
    N = 1  # Replace with your desired frame number
    with open('frame_index.txt', 'r') as  file:
        content = file.read()
    N = int(content)
    cap.set(cv2.CAP_PROP_POS_FRAMES, N)

    # Read the Nth frame/image from the capture object
    ret, img = cap.read()
    img = cv2.resize(img, (400, 800))

    # Do Pose detection
    results = pose.process(img)

    # Get the height and width of the frame
    height, width, _ = img.shape

    # Initialize circle coordinates
    center_x, center_y = 0, 0
    x_circum, y_circum = 0, 0

    # Point to be checked (you can replace this with any other point to test)
    # x_check, y_check = 0, 0
    with open('coordinates.txt', 'r') as file:
        content = file.read()
    try:
        numbers = tuple(map(int, content.strip('()\n').split(', ')))
        x_check, y_check = numbers
    except:
        numbers = None
        x_check, y_check = 0, 0
    print(x_check, y_check)

    # Initialize rectangle coordinates
    rect_a_x, rect_a_y = 0, 0
    rect_b_x, rect_b_y = 0, 0
    rect_c_x, rect_c_y = 0, 0
    rect_d_x, rect_d_y = 0, 0
    

    # Print the coordinates of the landmarks in terms of pixel values
    for index, landmark in enumerate(results.pose_landmarks.landmark):
        if index == 0:
            center_x = int(landmark.x * width)
            center_y = int(landmark.y * height)
        if index == 7:
            x_circum, y_circum = int(landmark.x * width), int(landmark.y * height)
        if index == 11:
            rect_a_x, rect_a_y = int(landmark.x * width), int(landmark.y * height)
        if index == 12:
            rect_b_x, rect_b_y = int(landmark.x * width), int(landmark.y * height)
        if index == 23:
            rect_c_x, rect_c_y = int(landmark.x * width), int(landmark.y * height)
        if index == 24:
            rect_d_x, rect_d_y = int(landmark.x * width), int(landmark.y * height)
    cv2.waitKey(0)

    # Release the video capture object
    cap.release()

    # Close all windows
    cv2.destroyAllWindows()

    is_inside_circle = is_point_inside_circle(center_x, center_y, x_circum, y_circum, x_check, y_check)

    is_inside_rect = is_point_inside_rectangle(rect_a_x, rect_a_y, rect_b_x, rect_b_y, rect_c_x, rect_c_y, rect_d_x, rect_d_y, x_check, y_check)
    
    if is_inside_circle == True:
        SCORE += 10
        print("Your score is ", SCORE)
    elif is_inside_rect == True:
        SCORE += 7
        print("Your score is ", SCORE)
    elif is_inside_circle == True and is_inside_rect == True:
        SCORE += 10
        print("Your score is ", SCORE)
    elif is_inside_circle == False and is_inside_rect == False:
        SCORE -= 3
        print("Your score is ", SCORE)