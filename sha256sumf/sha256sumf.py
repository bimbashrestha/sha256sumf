# -*- coding: utf-8 -*-
"""sha256sumf.sha256sumf: provides entry point main()."""

from __future__ import print_function

__version__ = "1.0.0"

import os
import sys
import argparse
import hashlib

CHUNK_SIZE = 2**17


def get_paths(path):
    paths = []
    for root, dirs, files in os.walk(path):
        for d in dirs:
            paths.append(os.path.join(root, d))
        for f in files:
            paths.append(os.path.join(root, f))
    return paths


def gen_chunks(path):
    with open(path, "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if len(chunk) == 0:
                break
            yield chunk


def sha256sumf_update_on_file(shasum, path):
    for chunk in gen_chunks(path):
        shasum.update(chunk)


def sha256sumf_folder(args):
    paths = sorted(get_paths(args.path))
    shasum = hashlib.sha256()
    for path in paths:
        root_path = path[len(args.path):]
        shasum.update(root_path.encode())
        if os.path.isfile(path):
            sha256sumf_update_on_file(shasum, path)
    print(shasum.hexdigest() + "  " + os.path.basename(args.path))


def sha256sumf_file(args):
    shasum = hashlib.sha256()
    sha256sumf_update_on_file(shasum, args.path)
    print(shasum.hexdigest() + "  " + os.path.basename(args.path))


def sha256sumf(args):
    if os.path.isfile(args.path):
        return sha256sumf_file(args)
    return sha256sumf_folder(args)


def main():
    parser = argparse.ArgumentParser(
        "sha256sumf",
        description=
        "A simple command line utility for producing recursive SHA 256 checksums of folders "
        "using file contents and sub-paths. Performs identically to the original sha256sum " 
        "when used on a single file.",
    )
    parser.add_argument(
        "path",
        type=str,
        help="The path of the directory to checksum (works on files too)",
    )
    args = parser.parse_args()
    sha256sumf(args)
