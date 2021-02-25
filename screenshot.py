from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from PIL import Image
import sys
import os
import argparse
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Target url.', dest='url')
parser.add_argument('-o', help='Output file name.', dest='output')
parser.add_argument('-t', help='File type. png webp jpeg...', dest='filetype')
parser.add_argument('-q', help='Quality. 0-100. Default 50', type=int, dest='quality', default=50)
parser.add_argument('--timeout', help='Timeout. Maximum number of seconds to wait while requesting a web page. Default 15', type=int, dest='timeout', default=15)
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


profile = webdriver.FirefoxProfile()
# From eyewitness
extension_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'dismissauth.xpi')
profile.add_extension(extension_path)

profile.set_preference('app.update.enabled', False)
profile.set_preference('browser.search.update', False)
profile.set_preference('extensions.update.enabled', False)

capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities.update({'acceptInsecureCerts': True})

options = Options()
options.add_argument("--headless")

profile.update_preferences()



driver = webdriver.Firefox(profile, capabilities=capabilities, options=options, service_log_path=os.path.devnull)
driver.set_page_load_timeout(args.timeout)


try:
    driver.get(url)
except:
    print('Screen shot error: ' + url)
    driver.close()
    exit(1)

driver.implicitly_wait(10)
driver.get_screenshot_as_file(output + ".png")
img = Image.open(output + ".png")
img = img.convert('RGB')
img.save(output + "." + filetype, filetype, quality=quality, optimize=True)
driver.close()
os.remove(output + ".png")