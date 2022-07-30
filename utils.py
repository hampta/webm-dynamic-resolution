import os
from config import IMAGE_DIR, WEBM_DIR, SOUND_NAME, TEMP_VIDEO, SEQUENCE_LIST


def check_dirs():
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    if not os.path.exists(WEBM_DIR):
        os.makedirs(WEBM_DIR)


def delete_temp_files():
    for file in os.listdir(IMAGE_DIR):
        os.remove(IMAGE_DIR + file)
    for file in os.listdir(WEBM_DIR):
        os.remove(WEBM_DIR + file)
    os.remove(SEQUENCE_LIST)
    os.remove(SOUND_NAME)
    os.remove(TEMP_VIDEO)
