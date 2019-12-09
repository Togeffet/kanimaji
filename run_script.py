import subprocess
import os

for filename in os.listdir("kanji/"):
  if filename == '.DS_Store':
    continue

  os.system("python kanimaji.py kanji/" + filename)