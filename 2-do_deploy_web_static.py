#!/usr/bin/python3
"""
 script that distributes an archive to your web servers
"""
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path

env.hosts = ["35.229.16.216", "34.73.228.13"]

def do_deploy(archive_path):
    if(os.path.isfile(archive_path) is false):
        return False

    try:
        pth_new = archive_path.split("/")[-1]
        save_in = ("/data/web_static/releases/" + pth_new.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(save_in))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(pth_new, save_in))
        run("sudo rm /tmp/{}".format(pth_new))
        run("sudo mv {}/web_static/* {}/".format(save_in, save_in ))
        run("sudo rm -rf {}/web_static".format(save_in))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(save_in))
        return True
    except:
        return False
