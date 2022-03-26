from downloader.constants import *
from downloader.utils import *

import time
import codecs

from selenium import webdriver


if __name__ == "__main__":
    url = input("twitter broadcast url: ")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script(XHR_SCRIPT)

    time.sleep(TIMEOUT)
    sniffed = driver.execute_script(GET_SNIFFED_VALUES)
    driver.quit()

    # file = codecs.open("temp", "w", "utf-8")
    # file.write(sniffed)
    # file.close()

    # sniffed = open("temp", "r", encoding="utf-8").read()
    m3u8_url = extract_m3u8_url(sniffed)

    download(m3u8_url)
    # remove_file("temp")

    print("Done!")