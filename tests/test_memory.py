from device_command_runner import run_adb_command, DeviceCommandError


def parse_meminfo(output):
    """
    Parses MemAvailable line from /proc/meminfo output.
    Returns available memory in kB or None if parsing fails.
    """
    try:
        # Expected format: "MemAvailable: 1234567 kB"
        parts = output.split()
        if len(parts) >= 2 and parts[0].startswith("MemAvailable"):
            return int(parts[1])
    except Exception:
        return None


def test_android_memory_minimum():
    cmd = "cat /proc/meminfo | grep MemAvailable"
    try:
        output = run_adb_command(cmd)
    except DeviceCommandError as e:
        return False, f"ADB command error after retries: {e}"

    if not output:
        return False, "No output from device"

    try:
        mem_kb = int(output.split()[1])
    except Exception as e:
        return False, f"Parse error: {e}"

    if mem_kb > 500000:
        return True, f"Memory available is sufficient: {mem_kb} kB"
    else:
        return False, f"Low memory warning: {mem_kb} kB"
