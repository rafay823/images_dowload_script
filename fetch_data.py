import json
import argparse
import glob
import requests
import shutil
import os
import validators

parser = argparse.ArgumentParser(description='Fetching images from url example.')
parser.add_argument('--urlfile', type=str, help='txt file')

args = parser.parse_args()


def url_validator(url):
    if validators.url(url):
        return True
    else:
        return False


def count_images_url(urls_lines):
    return len(urls_lines)


def check_save_images(dir):
    return len(os.listdir(dir))


def main(args):
    file = open(args.urlfile, "r")
    file_lines = file.readlines()
    for url in file_lines:
        filename = url.split("/")[-1]
        savepath = os.path.join('images', filename)
    if url_validator(url):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(savepath, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
                print("image saved")
        else:
            print("image url exists no more")
    else:
        print("image url is not correct")

    if count_images_url(file_lines) == check_save_images('images'):
        print("All images downloaded")
    else:
        print("some images got missing")


if __name__ == '__main__':
    main(args)
