#!/bin/sh -ex

blender \
  --background \
  main.blend \
  --python make-render.py

for f in preview*.png
do
  OUTPUT=`echo "$f" | sed 's/png$/jpg/g'`
  convert "$f" -scale '50%' "${OUTPUT}"
done
