import subprocess
import paramiko
import socket
import time
from functools import wraps

class DeviceCommandError(Exception):
    pass

def retry(exceptions, tries=3, delay=2):
    """
    Retry decorator.
    Args:
        exceptions: Exception or tuple of exceptions to catch
        tries: Number of attempts
        delay: Seconds to wait between retries
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = tries
            while attempts > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Warning: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempts -= 1
            # Last attempt, exceptions will be raised if any
            return func(*args, **kwargs)
        return wrapper
    return decorator


@retry(DeviceCommandError, tries=3, delay=2)
def run_adb_command(cmd):
    full_cmd = f"adb shell {cmd}"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        raise DeviceCommandError(f"ADB command failed: {result.stderr.strip()}")
    return result.stdout.strip()


def is_android_device_connected():
    try:
        result = subprocess.run(
            ["adb", "devices"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.strip().splitlines()
        # The first line is always "List of devices attached"
        devices = [line for line in lines[1:] if line.strip() and 'device' in line]
        return len(devices) > 0
    except subprocess.CalledProcessError as e:
        print(f"ADB check failed: {e}")
        return False


def is_ssh_reachable(host, port=22, timeout=5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error) as e:
        print(f"SSH not reachable: {e}")
        return False
