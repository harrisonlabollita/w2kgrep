import glob
import os
import shutil

from setuptools import setup

setup(name="w2kgrep",
      version="0.0.1",
      author="Harrison LaBollita",
      author_email="hlabolli@asu.edu",
      description="A grep-like tool for quickly extracting information from a Wien2k scf file.",
      url="https://github.com/harrisonlabollita/w2kgrep",
      packages=['w2kgrep'],
      license='MIT',
      entry_points={
          "console_scripts": [
              "w2kgrep = w2kgrep.w2kgrep:main",
          ]
      },
      )
