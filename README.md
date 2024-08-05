# Parallax

<p align="center">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="Made with Love" />
    <img src="https://img.shields.io/badge/Made%20with-love-red" alt="MIT License"/>
</p>

**Parallax** is a simple **CLI tool** to join multiple .png's and output a layered .gif parallax animation.

## Demo

```sh
parallax.py -i l1.png l2.png l3.png l4.png -os 2.0 -ls 1 2 4 8 -o forest
```

Output:

```
Loading l1.png
Loading l2.png
Loading l3.png
Loading l4.png
Layer speeds: [1, 2, 4, 8]
Saving 'forest.gif', 180 frames, (360, 180) px
Done!
```

![Output](img/forest.gif)

## Installation

To use this tool, ensure you have Python installed. You can install the required dependencies using pip:

```sh
pip install -r requirements.txt
```

## Usage

Fastest way to use it is `parallax.py`.
This will get all .png's in `cwd` and set layer speeds automatically.

```
usage: parallax.py [-h] [-i [INPUT ...]] [-fd FRAME_DURATION] [-os OUTPUT_SCALE] [-ls [LAYER_SPEEDS ...]] [-d DIRECTION] [-o OUTPUT]

Takes multiple .png's and creates a scrolling parallax animation with them.

options:
  -h, --help            show this help message and exit
  -i [INPUT ...], --input [INPUT ...]
                        Paths to the .png layer files to use in the animation, if not specified, it will use all .png's in current folder.
  -fd FRAME_DURATION, --frame-duration FRAME_DURATION
                        Length of the animation in frames, default to the width in pixels.
  -os OUTPUT_SCALE, --output-scale OUTPUT_SCALE
                        Scale factor for output image, defaults to 1.0.
  -ls [LAYER_SPEEDS ...], --layer-speeds [LAYER_SPEEDS ...]
                        Sets the speed in pixels per frame for each layer. Number of elements needs to be the same as the amount of layers. Leave empty for automatic speeds.
  -d DIRECTION, --direction DIRECTION
                        Sets the movement direction of the animation. (1) - Left (default) (-1) - Right
  -o OUTPUT, --output OUTPUT
                        Sets the output filename.
```
