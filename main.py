from downloader.utils import *

# import codecs

from selenium import webdriver


if __name__ == "__main__":
    url = input("twitter broadcast url: ")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script(open("downloader/listener.js", "r").read())

    data = ""

    while not data:
        for i in driver.get_log("browser"):
            if (
                "message" in i
                and "source" in i
                and i["source"] == "console-api"
                and ".m3u8" in i["message"]
            ):
                data = i["message"]

    driver.quit()

    # file = codecs.open("temp", "w", "utf-8")
    # file.write(data)
    # file.close()

    # data = open("temp", "r", encoding="utf-8").read()
    m3u8_url = extract_m3u8_url(data)

    download(m3u8_url)
    # remove_file("temp")
    print("Done!")
