import os
import urllib.request

DEST_PATH = "haarcascade_frontalface_default.xml"
URL = "https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml"

if not os.path.isfile(DEST_PATH):
    print("[INFO] Haar cascade file missing, downloading...")
    urllib.request.urlretrieve(URL, DEST_PATH)
    print("[INFO] Download complete.")
else:
    print("[INFO] Haar cascade file already present.")
