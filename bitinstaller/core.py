import subprocess
import os

"""
Install Order
Format selected drive
Mount selected ISO
Copy ISO files
Split Wim File

"""

class InstallationEngine:
    def __init__(self, selectedISOPath, selectedDrive):
        self.selectedISO = selectedISOPath
        self.selectedDrive = selectedDrive

        self.mountedISO = ""

    def splitWimfile(self):
        self.copyISOCommand = subprocess.Popen(
                ["wimlib-imagex", "split", self.mountedISO + "/sources/install.wim", "/Volumes/WIN10/sources/install.swm", "3800"], stdout=subprocess.PIPE
        )
        self.copyOutput, self.copyError = self.copyISOCommand.communicate()

    def copyISOFiles(self):
        
        os.system(f"rsync -vha --exclude=sources/install.wim {self.mountedISO}/* /Volumes/WIN10")
        #self.copyISOCommand = subprocess.Popen(
        #        [f"rsync -vha --exclude=sources/install.wim+{self.mountedISO}+/* /Volumes/WIN10"], stdout=subprocess.PIPE
        #)
        #self.copyOutput, self.copyError = self.copyISOCommand.communicate()

    def mountSelectedISO(self):
        
        self.mountISOCommand = subprocess.Popen(
                ["hdiutil", "mount", self.selectedISO], stdout=subprocess.PIPE
        )
        self.mountOutput, self.mountError = self.mountISOCommand.communicate()
        
        parts = self.mountOutput.split()  # Split the string using default whitespace delimiter
        self.mountedISO = parts[-1]  # Select the last element of the list
        self.mountedISO = self.mountedISO.decode('utf-8')
        del parts

    def formatDrive(self):
        """
        Attempts to format the drive
        in GPT and tries MBR if GPT where
        to fail
        """
        try:
            self.formatDiskCommand = subprocess.Popen(
                ["diskutil", "eraseDisk", "MS-DOS", "WIN10", "GPT", self.selectedDrive], stdout=subprocess.PIPE
            )
            self.formatOutput, self.formatError = self.formatDiskCommand.communicate()
        except Exception:
            try:
                self.formatDiskCommand = subprocess.Popen(
                    ["diskutil", "eraseDisk", "MS-DOS", "WIN10", "MBR", self.selectedDrive], stdout=subprocess.PIPE
                )
                self.formatOutput, self.formatError = self.formatDiskCommand.communicate()
            except Exception:
                return False
            
        if self.formatError != None:
            return True