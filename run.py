import os
import argparse

if __name__ == "__main__":
        # Initialize argument parser
    parser = argparse.ArgumentParser(description="Process video with pose estimation.")
    
    # Add argument for video filename
    parser.add_argument('--video', type=str, required=True, help='Path to the input video file.')
    
    # Parse the arguments
    args = parser.parse_args()

    os.system(f"python main.py -W 640 -H 480 -u 20 -U 160 -s 100 -S 255 -v 200 -V 255 -d {args.video}")
    os.system(f"python frame.py --video {args.video}")
