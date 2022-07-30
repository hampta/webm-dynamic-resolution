import os
import random
import subprocess

from PIL import Image

from config import FFMPEG_BIN, IMAGE_DIR, SOUND_NAME, VIDEO_NAME, WEBM_DIR
from utils import check_dirs, delete_temp_files


def extract(video):
    print("Converting video to sequence")
    # extract frames from video
    subprocess.run([FFMPEG_BIN, '-i', video, './temp/%03d.jpg'],
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    # extract sound
    subprocess.run([FFMPEG_BIN, '-i', video, '-vn', SOUND_NAME],
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def convert_images():
    images = os.listdir(IMAGE_DIR)
    images_count = len(images)
    with open('mylist.txt', 'w') as file_list:
        for image in images:
            image_name = image.split('.')[0]
            print(f"Resizing image {image_name}/{images_count}")
            img = Image.open(IMAGE_DIR + image)
            if image_name == '000':
                img = img.resize((2048, 2048), Image.ANTIALIAS)
            img = img.resize(
                (random.randint(10, 2048), random.randint(10, 2048)), Image.ANTIALIAS)
            # save the image
            img.save(IMAGE_DIR + image)
            img.close()
            subprocess.run([FFMPEG_BIN, '-i', IMAGE_DIR + str(image_name) + '.jpg', '-r', '25', '-c:v', 'libvpx',
                            WEBM_DIR + str(image_name) + ".webm"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            file_list.write(f"file '{WEBM_DIR}{image_name}.webm'\n")


def compress():
    image = Image.open('image.png').convert('RGB')
    with open('mylist.txt', 'w') as file_list:
        for i in range(600, 10, -1):
            print(f"Resizing image {i}")
            img = image.resize((600, i))
            image_dir = IMAGE_DIR + str(i) + '.jpg'
            img.save(image_dir)
            img.close()
            subprocess.run([FFMPEG_BIN, '-i', image_dir, '-r', '60', '-c:v', 'libvpx',
                            WEBM_DIR + str(i) + ".webm"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            file_list.write(f"file '{WEBM_DIR}{i}.webm'\n")


def create_webm():
    subprocess.run([FFMPEG_BIN, '-f', 'concat', '-r', '25', '-safe',
                   '0', '-i', 'mylist.txt', '-c', 'copy', './temp.webm'])
    # add sound
    subprocess.run([FFMPEG_BIN, '-i', SOUND_NAME, '-i',
                   './temp.webm', '-c', 'copy', './output.webm'])


def main():
    while True:
        print("Starting...")
        mode = input("Mode: \n1 - Random scale\n2 - Press scale\n")
        if mode not in ['1', '2']:
            print("Invalid mode")
            continue
        check_dirs()
        if mode == '1':
            extract(VIDEO_NAME)
            convert_images()
        elif mode == '2':
            compress()
        create_webm()
        delete_temp_files()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        delete_temp_files()
        exit(0)
