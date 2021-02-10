from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from PIL import Image
import sys
import os
import argparse


options = Options()
options.headless = True

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Target url.', dest='url')
parser.add_argument('-o', help='Output file name.', dest='output')
parser.add_argument('-t', help='File type. png webp jpeg...', dest='filetype')
parser.add_argument('-q', help='Quality. 0-100. Default 50', type=int, dest='quality', default=50)
args = parser.parse_args()

url = args.url
output = args.output
filetype = args.filetype
quality = args.quality

if url is None or filetype is None:
    print("Require url and type. Use \"python3 screenshot.py -h\" for help.")
    exit()

if output is None:
    output = url.replace('.', '_').replace('://', '_')

driver = webdriver.Firefox(options=options)
driver.get(url)
driver.implicitly_wait(10)
driver.get_screenshot_as_file(output + ".png")
img = Image.open(output + ".png")
img = img.convert('RGB')
img.save(output + "." + filetype, filetype, quality=quality, optimize=True)
driver.close()
os.remove(output + ".png")