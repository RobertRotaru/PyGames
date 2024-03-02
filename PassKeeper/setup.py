from cx_Freeze import setup, Executable

base = None    

executables = [Executable("passKeeper.py", base=base)]

packages = ["idna", "os", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<first_ever>",
    options = options,
    version = "0.11",
    description = ' ',
    executables = executables
)