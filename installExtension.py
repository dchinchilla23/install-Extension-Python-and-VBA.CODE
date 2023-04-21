import subprocess
import sys
import os
import shutil
from os.path import expanduser

try:
    import vscode_extapi as vs
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'vscode-extapi'])
    import vscode_extapi as vs

extension_name = "ms-python.python"

try:
    vs.extensions.install(extension_name)
    print(f"{extension_name} instalada correctamente")
except Exception as e:
    print(f"Error al instalar {extension_name}: {e}")
