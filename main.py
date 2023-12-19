import argparse
import LaserTracker 

if __name__ == '__main__':
    # laser tracker initialization and running
    parser = argparse.ArgumentParser(description='Run the Laser Tracker')
    parser.add_argument('-W', '--width',
                        default=640,
                        type=int,
                        help='Camera Width')
    parser.add_argument('-H', '--height',
                        default=480,
                        type=int,
                        help='Camera Height')
    parser.add_argument('-u', '--huemin',
                        default=20,
                        type=int,
                        help='Hue Minimum Threshold')
    parser.add_argument('-U', '--huemax',
                        default=160,
                        type=int,
                        help='Hue Maximum Threshold')
    parser.add_argument('-s', '--satmin',
                        default=100,
                        type=int,
                        help='Saturation Minimum Threshold')
    parser.add_argument('-S', '--satmax',
                        default=255,
                        type=int,
                        help='Saturation Maximum Threshold')
    parser.add_argument('-v', '--valmin',
                        default=200,
                        type=int,
                        help='Value Minimum Threshold')
    parser.add_argument('-V', '--valmax',
                        default=255,
                        type=int,
                        help='Value Maximum Threshold')
    parser.add_argument('-d', '--display',
                        action='store_true',
                        help='Display Threshold Windows')
    parser.add_argument('video_file', help='Input video file')
    params = parser.parse_args()

    tracker = LaserTracker(
        cam_width=params.width,
        cam_height=params.height,
        hue_min=params.huemin,
        hue_max=params.huemax,
        sat_min=params.satmin,
        sat_max=params.satmax,
        val_min=params.valmin,
        val_max=params.valmax,
        display_thresholds=params.display
    )
    tracker.run(params.video_file)
    
    # See if the coordinates are in the NO NO SQUARE