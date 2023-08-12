import subprocess


class InstallationEngine:
    def __init__(self, selectedISOPath, selectedDrive):
        self.selectedISO = selectedISOPath
        self.selectedDrive = selectedDrive

    def mountSelectedISO(self):
        
        self.mountISOCommand = subprocess.Popen(
                ["hdiutil", "mount", self.selectedISO], stdout=subprocess.PIPE
        )
        self.mountOutput, self.mountError = self.mountISOCommand.communicate()
        
        parts = self.mountOutput.split()  # Split the string using default whitespace delimiter
        last_part = parts[-1]  # Select the last element of the list

    def formatDrive(self):
        """
        Attempts to format the drive
        in GPT and tries MBR if GPT where
        to fail

        
        Takes type of string ex:"/dev/drive0"

        Returns True if execution was successful
        Returns False if execution resulted in failure
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