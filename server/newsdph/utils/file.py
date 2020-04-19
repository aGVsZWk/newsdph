try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for, current_app, flash
import os
import uuid
import requests
import PIL
from PIL import Image
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import tarfile
import zipfile

from newsdph.extensions import db
from newsdph.models import User
from newsdph.settings import Operations

def rename_image(old_filename):
    ext = os.path.splitext(old_filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


def resize_image(image, filename, base_width):
    filename, ext = os.path.splitext(filename)
    img = Image.open(image)
    if img.size[0] <= base_width:
        return filename + ext
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size), PIL.Image.ANTIALIAS)

    filename += current_app.config['ALBUMY_PHOTO_SUFFIX'][base_width] + ext
    img.save(os.path.join(current_app.config['ALBUMY_UPLOAD_PATH'], filename), optimize=True, quality=85)
    return filename



def compress_file_list(input_file_list, out_file_path):
    with tarfile.open(out_file_path, "w:") as tar:
        for file_path in input_file_list:
            tar.add(file_path, arcname=os.path.basename(file_path))


def uzip_zip_file(zip_file_path, file_dir):
    with zipfile.ZipFile(zip_file_path, "r") as z:
        for f in z.namelist():
            z.extract(f, file_dir)


def download_with_url(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
