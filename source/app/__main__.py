#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path

from playbooks.execute import execute


def project_subdirs(path: Path, directory_name=".mondrik"):
    ''' Generate list of subdirs with .mondrik directory
    '''
    project_dir = path / directory_name
    if project_dir.is_dir():
        yield path.resolve()
    else:
        for p in path.iterdir():
            yield from project_subdirs(p, directory_name)


def main():
    '''
    '''
    try:
        for project_dir in project_subdirs(Path("."), ".mondrik"):
            playbooks = [p for p in project_dir.glob(".mondrik/main.yml")]
            context = dict(
                current_directory=str(project_dir)
            )
            try:
                res = execute(playbooks, context=context)
            except Exception as err:
                print(f"{err}")
    except Exception as err:
        print(f"{err}")
        sys.exit(1)


main()
