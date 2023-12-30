import os
import argparse
import subprocess
import time

SCORE = 0

def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True)
        process.wait()

    except KeyboardInterrupt:
        process.terminate()
        try:
            process.wait(timeout=5)  # Wait for the process to terminate
        except subprocess.TimeoutExpired:
            process.kill()  # If it didn't terminate, kill it

if __name__ == "__main__":
    while True:
        # Initialize argument parser
        parser = argparse.ArgumentParser(description="Process video with pose estimation.")
        
        # Add argument for video filename
        parser.add_argument('--video', type=str, required=True, help='Path to the input video file.')
        
        # Parse the arguments
        args = parser.parse_args()

        # Execute the first command
        run_command("python main.py -W 1280 -H 720 -u 20 -U 160 -s 100 -S 255 -v 200 -V 255")

        # Wait for a short time to allow the first command to terminate
        time.sleep(2)

        # Execute the second command
        os.system(f"python frame.py --video {args.video}")
