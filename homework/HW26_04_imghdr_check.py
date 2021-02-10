import os
import argparse
import imghdr

parser = argparse.ArgumentParser()
parser.add_argument('img_abs_path')
args = parser.parse_args()
img_path = args.img_abs_path
#lis = ['jpeg', 'png', 'bnp']
#if imghdr.what(img_path) in lis:
if imghdr.what(img_path) == 'png':
    print("PNG format")
else:
    print("Not PNG format")
