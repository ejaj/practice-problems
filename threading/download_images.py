#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : download_images.py
@Time : 4/4/22 2:47 PM
@Desc: 
"""
import time
import requests
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1627156863760-f49b81d8ab77',
    'https://images.unsplash.com/photo-1416339306562-f3d12fefd36f'
]


def download_images(img_url):
    img_byte = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_byte)
        print(f'{img_name} was downloaded...')


def main():
    """
    Main function for drive code
    Returns:

    """
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_images, img_urls)
    end = time.perf_counter()
    print(f'Finished in {end - start} seconds')


if __name__ == '__main__':
    main()
