import cv2
import argparse
import mediapipe as mp
from utils import is_point_inside_circle, is_point_inside_rectangle
# from run import SCORE


class PoseAnalyzer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.mp_pose = mp.solutions.pose
        self.mp_draw = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose()
        SCORE = 0

    def process_pose(self, img):
        results = self.pose.process(img)
        return results

    def analyze(self):
        cap = cv2.VideoCapture(self.video_path)

        # Skip to the Nth frame
        N = 1  # Replace with your desired frame number
        with open('frame_index.txt', 'r') as file:
            content = file.read()
        N = int(content)
        cap.set(cv2.CAP_PROP_POS_FRAMES, N)

        _, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        results = self.process_pose(img)

        height, width, _ = img.shape
        center_x, center_y = 0, 0
        x_circum, y_circum = 0, 0

        with open('coordinates.txt', 'r') as file:
            content = file.read()
        try:
            numbers = tuple(map(int, content.strip('()\n').split(', ')))
            x_check, y_check = numbers
        except:
            numbers = None
            x_check, y_check = 0, 0
        print(x_check, y_check)

        rect_a_x, rect_a_y = 0, 0
        rect_b_x, rect_b_y = 0, 0
        rect_c_x, rect_c_y = 0, 0
        rect_d_x, rect_d_y = 0, 0

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

        cap.release()
        cv2.destroyAllWindows()

        is_inside_circle = is_point_inside_circle(center_x, center_y, x_circum, y_circum, x_check, y_check)
        is_inside_rect = is_point_inside_rectangle(rect_a_x, rect_a_y, rect_b_x, rect_b_y, rect_c_x, rect_c_y, rect_d_x, rect_d_y, x_check, y_check)

        if is_inside_circle:
            self.SCORE += 10
            print("Your score is ", self.SCORE)
        elif is_inside_rect:
            self.SCORE += 7
            print("Your score is ", self.SCORE)
        elif is_inside_circle and is_inside_rect:
            self.SCORE += 10
            print("Your score is ", self.SCORE)
        elif not is_inside_circle and not is_inside_rect:
            self.SCORE -= 3
            print("Your score is ", self.SCORE)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process video with pose estimation.")
    parser.add_argument('--video', type=str, required=True, help='Path to the input video file.')
    args = parser.parse_args()
    
    pose_analyzer = PoseAnalyzer(args.video)
    pose_analyzer.analyze()
