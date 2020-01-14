#!/usr/bin/python3
# Fabric script that generates a .tgz archive from content of the web_static

from fabric.api import *
import tarfile
from datetime import datetime
import os


def do_pack():
    "do pack"
    ver = "versions/"
    f_name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if not os.path.exists(ver):
        os.mkdir(ver)
    with tarfile.open(ver + f_name, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(ver + f_name):
        return ver + f_name
    else:
        return None
