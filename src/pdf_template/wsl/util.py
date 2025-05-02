import subprocess

def open_in_windows_browser(url):
    try:
        subprocess.run(["powershell.exe", "Start-Process", url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to open browser: {e}")