import os
import wget
import shutil

run_file = open("todoplus.txt", "w") #name of the final launch executable

temp = '"cd Program && python ./main.py"' #"Program" is a folder containing all project files, "mainmockup.py" is the name of the main python file which launches the program

code = ["import os \n", "os.system('cmd /k " + temp +" ')"]  

run_file.writelines(code) 

run_file = 'todoplus.txt'
base = os.path.splitext(run_file)[0]
os.rename(run_file, base + '.py')

os.system('cmd /k "pip install numpy && pyinstaller todoplus.py -F"')

path = "./dist/todoplus.exe"

destination = "./"

dest = shutil.move(path, destination)

os.rmdir("./dist")