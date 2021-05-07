#!/usr/bin/env python3
# -*- coding:utf-8; mode:python; -*-
'''
Open a child process that listens to wob
'''


import os
from pathlib import Path
from time import sleep
import daemon
from subprocess import Popen, PIPE, TimeoutExpired


def wobfeed(wobproc: Popen):
    '''
    open wob subprocess child daemon
    '''
    # Parent process
    for vol in range(0, 101, 25):
        wobproc.stdin.write(f'{vol}\n')
        wobproc.stdin.flush()


if __name__ == "__main__":
    wobpipe = open_pipe()
    wobfeed(wobpipe)
