import os
import requests
import sys

VERSION_URL = "https://drive.google.com/file/d/1YODZ4u3AxsMbyR3NGkaofo0RbbsAALNi/view?usp=drive_link"
DOWNLOAD_URL = "https://drive.google.com/file/d/1kfKhs2oi_WgwgrBnrCWeNnsJ8lHzjBvb/view?usp=sharing"
CURRENT_VERSION = "1.0.0"

def check_for_updates(current_version):
    try:
        response = requests.get(VERSION_URL)
        latest_version = response.text.strip()
        if latest_version != current_version:
            return latest_version
    except Exception as e:
        print(f"Failed to check for updates: {e}")
    return None

def download_latest_version():
    try:
        response = requests.get(DOWNLOAD_URL, stream=True)
        with open("revenue_report_new.exe", "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        return True
    except Exception as e:
        print(f"Failed to download the latest version: {e}")
    return False

def update_application():
    latest_version = check_for_updates(CURRENT_VERSION)
    if latest_version:
        print(f"New version available: {latest_version}")
        user_input = input("Do you want to update to the latest version? (yes/no): ").strip().lower()
        if user_input == "yes":
            if download_latest_version():
                os.replace("revenue_report_new.exe", "revenue_report.exe")
                print("Application updated successfully.")
                return True
    return False

if __name__ == "__main__":
    if update_application():
        print("Restarting application...")
        exe_path = os.path.abspath("revenue_report.exe")
        os.execv(sys.executable, [sys.executable, exe_path])
    else:
        # Main application logic here
        print("Running application...")
