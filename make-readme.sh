#!/bin/sh -ex

exec blender \
  --background \
  main.blend \
  --python make-readme.py

