import subprocess

formatDiskCommand = subprocess.Popen(
            ["jfvkuayfv"], stdout=subprocess.PIPE
        )
out, err = formatDiskCommand.communicate()

print("OUTPUT")
print(out)
print("ERROR")
print(err)