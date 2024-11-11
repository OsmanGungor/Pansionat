import logging
from plyer import notification
import winsound
import os
from collections import Counter

def read_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return None

def write_file(file_path, lines):
    with open(file_path, 'w',encoding='utf-8') as file:
        file.writelines(lines)



def compare_and_update_file(file_path, new_content):
    current_content = read_file(file_path)
    if current_content is not None:
        current_content = [line.strip() for line in current_content]
    new_content = [f"{line.strip()}\n" for line in new_content]
    stripped_new_content = [item.strip() for item in new_content]

    if Counter(current_content) != Counter(stripped_new_content):
        write_file(file_path, new_content)
        logging.info("The file was updated.")

        notification.notify(
            title='New Registered Company has been found!!!',
            message='New Company has been added to the list!!',
            app_icon=None,
            timeout=20,
        )

        # Play a Windows sound
        winsound.MessageBeep(winsound.MB_ICONASTERISK)

        return True
    else:
        notification.notify(
            title='No new company!',
            message='The list has NOT been changed.',
            timeout=20,
        )

        # Play a Windows sound
        winsound.MessageBeep(winsound.MB_ICONASTERISK)
        logging.info("The file content is the same. No update is required.")
        return False