#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools
import shutil

WorkDir = "."
Version =  get.srcVERSION()

def install():
    shutil.rmtree("gogland-%s/jre" % Version)
    pisitools.insinto("/opt/gogland", "gogland-%s/*" % Version)
    pisitools.dosym("/opt/gogland/bin/gogland.sh", "/usr/bin/gogland")
