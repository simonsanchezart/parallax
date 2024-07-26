import argparse

DEFAULT_FRAME_DURATION = None
DEFAULT_OUTPUT_SCALE = 1.0
DEFAULT_LAYER_SPEEDS = None
DEFAULT_DIRECTION = 1
DEFAULT_OUTPUT = "parallax_output"


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Takes multiple .png's and creates a scrolling parallax animation with them."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        nargs="*",
        help="Paths to the .png layer files to use in the animation, if not specified, it will use all .png's in current folder.",
    )
    parser.add_argument(
        "-fd",
        "--frame-duration",
        type=int,
        default=DEFAULT_FRAME_DURATION,
        help="Length of the animation in frames, default to the width in pixels.",
    )
    parser.add_argument(
        "-os",
        "--output-scale",
        type=float,
        default=DEFAULT_OUTPUT_SCALE,
        help="Scale factor for output image, defaults to 1.0.",
    )
    parser.add_argument(
        "-ls",
        "--layer-speeds",
        type=int,
        default=DEFAULT_LAYER_SPEEDS,
        nargs="*",
        help="Sets the speed in pixels per frame for each layer. Number of elements needs to be the same as the amount of layers. Leave empty for automatic speeds.",
    )
    parser.add_argument(
        "-d",
        "--direction",
        type=int,
        default=DEFAULT_DIRECTION,
        help="Sets the movement direction of the animation. (1) - Left (default) (-1) - Right",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=DEFAULT_OUTPUT,
        help="Sets the output filename.",
    )

    return parser.parse_args()
