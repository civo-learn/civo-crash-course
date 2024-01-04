import subprocess

def run_s3cmd_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode().strip()


# Upload a file
print(run_s3cmd_command("s3cmd put /tmp/demo.txt s3://course/demo.txt"))

# List files in a bucket
print(run_s3cmd_command("s3cmd ls s3://course"))

# Download a file
print(run_s3cmd_command("s3cmd get s3://course/demo.txt /Users/saiyam/demo.txt"))

# Delete a file
print(run_s3cmd_command("s3cmd del s3://course/demo.txt"))


