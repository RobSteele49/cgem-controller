#!/usr/bin/python3
# killProcess.py

# 2024-12-31 This code does not run correctly on a windows computer.
# Need to look into why and how to resolve this problem.

import subprocess
import os
import platform
import sys

def killProcess(process_name):
    """
    Kills all processes with the given name.

    Args:
        process_name: The name of the process to kill.
    """

    try:
        # Get the operating system
        os_name = platform.system()

        if os_name == 'Linux' or os_name == 'Darwin':  # Linux or macOS
            # Use `ps aux | grep -v grep | grep <process_name>` to find processes
            cmd = f"ps aux | grep -v grep | grep {process_name} | awk '{{print $2}}'"
            output = subprocess.check_output(cmd, shell=True, text=True)
            pids = output.strip().split('\n')

        elif os_name == 'Windows':
            # Use `tasklist /fi "IMAGENAME eq {process_name}"` to find processes
            cmd = f"tasklist /fi \"IMAGENAME eq {process_name}\""
            output = subprocess.check_output(cmd, shell=True, text=True)
            lines = output.splitlines()[4:]  # Skip header lines
            pids = [line.split()[1] for line in lines]

        else:
            raise ValueError(f"Unsupported operating system: {os_name}")

        # Kill each process by its PID
        for pid in pids:
            if pid: # Check if PID is not empty
                try:
                    print (f"PID : {pid}")
                    os.kill(int(pid), 9)  # Send SIGKILL signal
                    print(f"Killed process with PID: {pid}")
                except OSError as e:
                    print(f"Error killing process with PID {pid}: {e}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Example usage
# killProcess('socat')

if __name__ == '__main__':
    # Get the process name from command line arguments (assuming one argument)
    if len(sys.argv) > 1:
        process_name = sys.argv[1]
        killProcess(process_name)
    else:
        print("Usage: killProcess.py <process_name>")

