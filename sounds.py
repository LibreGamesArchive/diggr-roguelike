#!/usr/bin/env python

from ctypes import *
import os
import time
import sys

_sound = CDLL('./libsound.so')

_sound.sound_play.restype = c_int




class Engine:
    def __init__(self, enabled=True):

        if not enabled:
            return
 
        exe = 'scsynth'
        cwd = os.getcwd()
        wd = os.path.join(cwd, 'sound')
        exedir = os.path.join(wd, '')
        synthdir = os.path.join(wd, 'synths')
        plugindir os.path.join(wd, 'plugins')

        if os.name == 'nt':
            exe += '.exe'

        _sound.sound_init(exe, exedir, synthdir, plugindir)


    def __del__(self):
        _sound.sound_stop()

    def play(self, name, **args):
        return _sound.sound_play(name, args[0], c_float(args[1]))

    def set(self, n, **args):
        _sound.sound_set(n, args[0], c_float(args[1]))

    def stop(self, n):
        _sound.sound_free(n)

    def toggle_mute(self):
        _sound.toggle_mute()

def main():
    e = Engine()
    time.sleep(1)
    e.play("plang")
    time.sleep(0.1)
    e.play("wobble")
    for x in xrange(4):
        e.play("plang", out=x%2)
        time.sleep(1)


if __name__ == '__main__':
    main()
