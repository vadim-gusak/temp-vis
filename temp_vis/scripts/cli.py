#!/usr/bin/env python3
import argparse
from temp_vis.visualization import start_visualization


DESCRIPTION = 'Overlay temperature data into resulting visualization'


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("stl_file",
                        help='Path to .stl file')
    parser.add_argument("json_file",
                        help='Path to .json file with temperature data')
    parser.add_argument("-o", "--opacity", default=1,
                        help='Set opacity level from 0.0 to 1.0')
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        opacity = float(args.opacity)
    except ValueError:
        raise argparse.ArgumentTypeError('Opacity must be float')
    if opacity < 0 or opacity > 1:
        raise argparse.ArgumentTypeError("Opacity not in range [0.0, 1.0]")

    start_visualization(args.stl_file, args.json_file, opacity)


if __name__ == '__main__':
    main()
