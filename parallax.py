import os
import colorama
from args import get_arguments
from colorama import Fore
from pathlib import Path
from PIL import Image, ImageChops

colorama.init(autoreset=True)

SPEED_FACTOR = 16

args = get_arguments()
layers = []
layer_speeds = []
frames = []


def load_layers(file_paths):
    for f in file_paths:
        try:
            print(f"{Fore.GREEN}Loading {f}")
            layers.append(Image.open(f))
        except:
            print(f"{Fore.RED}Couldn't load {f}")
            exit(1)


if args.input:
    load_layers(args.input)
else:
    png_files = (f for f in os.listdir() if Path(f).suffix == ".png")
    load_layers(png_files)
assert len(layers) != 0, "No input images."

image_size = layers[0].size
frame_duration = image_size[0] if not args.frame_duration else args.frame_duration

if not args.layer_speeds:
    for i in range(len(layers), 0, -1):
        speed = (frame_duration / SPEED_FACTOR) / (i + 1)
        layer_speeds.append(round(speed))
else:
    layer_speeds = args.layer_speeds
print(f"{Fore.CYAN}Layer speeds: {layer_speeds}")

if len(layers) != len(layer_speeds):
    raise ValueError(
        f"{Fore.RED}There are {len(layers)} layers, however {len(layer_speeds)} layer speeds were specified."
    )

for i in range(frame_duration):
    frame_img = Image.new("RGB", layers[0].size, (255, 0, 255))

    for j in range(len(layers)):
        layers[j] = ImageChops.offset(layers[j], args.direction * layer_speeds[j], 0)
        frame_img.paste(layers[j], mask=layers[j].convert("RGBA"))
    frames.append(frame_img)

if args.output_scale != 1.0:
    for i, f in enumerate(frames):
        frame_size = (
            round(f.size[0] * args.output_scale),
            round(f.size[1] * args.output_scale),
        )
        frames[i] = f.resize(frame_size, Image.NEAREST)

filename = f"{args.output}.gif"
print(f"{Fore.GREEN}Saving '{filename}', {frame_duration} frames, {frames[0].size} px")
frames[0].save(filename, save_all=True, append_images=frames[1:], duration=0, loop=0)
print(f"{Fore.GREEN}Done!")
