import platform
import subprocess
import re

class GetDiskInfo:
    def __init__(self):
        self.currentos = platform.system()
        self.driveSizes = []
        self.driveNames = []
        self.driveData = {}

        if self.currentos == "Darwin":  # macos returns "Darwin"
            self.grabMacosDisks()

    def grabMacosDisks(self):
        diskName_re = r"(/dev/disk\d+)\s"  # Grab the location of the disks
        selectedLine_re = r"^\s*0:"  # Grab lines that start with "0:"
        diskSize_re = r"(\d+\.\d+)\s+(MB|GB|TB)"  # Grab the size of the disk

        # Read all disks using system "diskutil list"
        process = subprocess.Popen(["diskutil", "list"], stdout=subprocess.PIPE)
        out, err = process.communicate()

        lines = out.decode("utf-8").split("\n")
        selectedDriveSizes = [
            line.strip() for line in lines if re.match(selectedLine_re, line)
        ]
        selectedDisks = re.findall(diskName_re, out.decode("utf-8"))

        for x in selectedDriveSizes:
            size_match = re.search(diskSize_re, x)
            self.driveSizes.append(size_match.group())

        for x in selectedDisks:
            self.driveNames.append(x)

        # ASSEMBLING FINAL DRIVE STRUCTURE
        for x in range(len(self.driveNames)):
            addon = {self.driveNames[x]: self.driveSizes[x]}
            self.driveData.update(addon)

        return self.driveData

if __name__ == '__main__':
    print(GetDiskInfo().driveData)