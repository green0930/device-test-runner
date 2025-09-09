from device_command_runner import is_android_device_connected, is_ssh_reachable
from tests import test_memory, test_uptime
import os
import sys

LINUX_HOST = "192.168.1.100"
LINUX_USER = "pi"
LINUX_PASS = "yourpassword"


def run_all_tests():
    results = []

    if not is_android_device_connected():
        print("Android device not connected. Skipping Android tests.")
        results.append(("Android Memory Test", False, "Device not connected"))
    else:
        print("Running Android memory test...")
        passed, message = test_memory.test_android_memory_minimum()
        results.append(("Android Memory Test", passed, message))
        print(f"Result: {'PASS' if passed else 'FAIL'} - {message}\n")

    if not is_ssh_reachable(LINUX_HOST):
        print(f"Linux device {LINUX_HOST} not reachable via SSH. Skipping Linux tests.")
        results.append(("Linux Uptime Test", False, "Device not reachable"))
    else:
        print("Running Linux uptime test...")
        passed, message = test_uptime.test_linux_uptime(LINUX_HOST, LINUX_USER, LINUX_PASS)
        results.append(("Linux Uptime Test", passed, message))
        print(f"Result: {'PASS' if passed else 'FAIL'} - {message}\n")

    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "test_report.txt")
    with open(report_path, "w") as f:
        for test_name, passed, message in results:
            f.write(f"{test_name}: {'PASS' if passed else 'FAIL'} - {message}\n")

    print(f"Test report saved to {report_path}")

    return results  # <-- Ensure results are returned


if __name__ == "__main__":
    results = run_all_tests()
    # Exit with 0 if all tests passed, else 1
    if all(passed for _, passed, _ in results):
        sys.exit(0)
    else:
        sys.exit(1)

    """
    
---

# Step 7: What Next

- Run your tests regularly and extend with new scenarios (power cycle, network tests).
- Upload to GitHub with a good README to showcase your embedded testing skills.
- Link this project in your resume!

---

If you want, I can help you **generate the full zipped project** ready to upload or walk you through any step. How would you like to proceed?

    """

