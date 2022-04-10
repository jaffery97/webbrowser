import subprocess

# if the script don't need output.
subprocess.call("php /file/index.php")

# if you want output
proc = subprocess.Popen("php /file/index.php", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()