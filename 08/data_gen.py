#!/usr/bin/python
# -*- coding:utf-8 -*-

import flickrapi
import urllib.request
import numpy as np
import skimage.io
import skimage.transform
import requests
import os
import warnings
from io import BytesIO

def save_data(photos, dir_name, keyword, nimage):
    dir_exists = os.path.isdir(dir_name+'/'+keyword)
    if not dir_exists:
        print("Making directory %s/%s" % (dir_name, keyword))
        if not os.path.isdir(dir_name):
            print("Making directory %s" % dir_name)
            os.mkdir(dir_name)
        os.mkdir(dir_name+'/'+keyword)
    else:
        print("Will store images in directory %s/%s" % (dir_name, keyword))

    i = 0
    nrow = 224
    ncol = 224
    for photo in photos:
        url=photo.get('url_c')
        if not (url is None):

            # Create a file from the URL
            # This may only work in Python3
            response = requests.get(url)
            file = BytesIO(response.content)

            # Read image from file
            im = skimage.io.imread(file)

            # Resize images
            im1 = skimage.transform.resize(im,(nrow,ncol),mode='constant')

            # Convert to uint8, suppress the warning about the precision loss
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                im2 = skimage.img_as_ubyte(im1)

            # Save the image
            local_name = '{0:s}/{1:s}/{1:s}_{2:04d}.jpg'.format(dir_name, keyword, i)
            skimage.io.imsave(local_name, im2)
            print(local_name)
            i = i + 1
        if (i >= nimage):
            break

def main():
    api_key = u'4c69827283b7884994a68a119067055a'
    api_secret = u'fcdb7596e94fbed6'
    flickr = flickrapi.FlickrAPI(api_key, api_secret)
    keywords = ['car', 'bicycle']
    dir_name = ['./train', './test']
    nimage = [1000, 300]
    for keyword in keywords:
        for i in range(len(dir_name)):
            photos = flickr.walk(text=keyword,
                tag_mode='all',
            tags=keyword,
            extras='url_c',
            sort='relevance',per_page=100)
            save_data(photos, dir_name[i], keyword, nimage[i])

if __name__=='__main__':
    main()
