from device_command_runner import run_ssh_command, DeviceCommandError


def test_linux_uptime(host, username, password):
    cmd = "uptime -p"
    try:
        output = run_ssh_command(host, username, password, cmd)
    except DeviceCommandError as e:
        return False, f"SSH command error after retries: {e}"

    if not output:
        return False, "No uptime output received"

    # Simple check if system has been up for at least 1 minute
    if "up" in output and ("minute" in output or "hour" in output or "day" in output):
        return True, f"System uptime is: {output}"
    else:
        return False, f"Unexpected uptime output: {output}"
