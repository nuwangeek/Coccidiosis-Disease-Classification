"""
This file is used to create generic files and directories for a project.
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"
# here defines the list of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "dvc.yml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# This for loop creates the files and directories
for filepath in list_of_files:
    path = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file:: {filepath}")

    else:
        logging.info(f"File already exists: {filename}")