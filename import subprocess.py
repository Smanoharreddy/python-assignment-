import subprocess



list_files = subprocess.run(["docker", "images"])

print("The exit code was: %d" % list_files.returncode)