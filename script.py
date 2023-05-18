import subprocess

def git_pull():
    try:
        # Run git pull command in the current directory
        subprocess.check_output(['git', 'pull'])
        print("Git pull successful.")
    except subprocess.CalledProcessError as e:
        print("Error executing git pull command:", e.output.decode())

# Call the function to perform the git pull
git_pull()