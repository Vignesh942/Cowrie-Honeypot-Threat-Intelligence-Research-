import subprocess
from config import KEY_PATH, HOST, REMOTE_LOG, LOCAL_LOG


def download_logs():
    print("=" * 50)
    print("Downloading latest Cowrie logs...")
    print("=" * 50)

    command = [
        "scp",
        "-i",
        KEY_PATH,
        f"{HOST}:{REMOTE_LOG}",
        LOCAL_LOG,
    ]

    result = subprocess.run(command)

    if result.returncode == 0:
        print("Download completed successfully.\n")
        return True

    print("Download failed.\n")
    return False