import sys
from cx_Freeze import setup, Executable

setup(name = "ToDo Plus",
      version = "1.0",
      description = "ToDo Plus",
      executables = [Executable("main.py")])