#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from playbooks.execute import execute


def main():
    '''
    '''
    try:
        current_dir = Path(".")
        playbooks = [str(p) for p in current_dir.glob(".mondrik/main.yml")]
        res = execute(playbooks)
    except Exception as err:
        print(f"{err}")
        sys.exit(1)

main()
