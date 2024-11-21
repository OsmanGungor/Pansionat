from plyer import notification
import winsound
from collections import Counter
from utils.mailsender import send_mail
from structlog import get_logger
logger = get_logger()

def read_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        return None

def write_file(file_path, lines):
    with open(file_path, 'w',encoding='utf-8') as file:
        file.writelines(lines)

def compare_and_write_file(file_path, new_content):
    current_content = read_file(file_path)
    if current_content is not None:
        current_content = [line.strip() for line in current_content]
    new_content = [f"{line.strip()}\n" for line in new_content]
    stripped_new_content = [item.strip() for item in new_content]

    if Counter(current_content) != Counter(stripped_new_content):
        write_file(file_path, new_content)
        logger.info("The file was updated.")
        return True
    else:
        logger.info("The file content is the same. No update is required.")
        return False

def send_windows_notification(is_updated):

    if is_updated:
        notification.notify(
            title='New Registered Company has been found!!!',
            message='New Company has been added to the list!!',
            app_icon=None,
            timeout=20,
        )
    else:
        notification.notify(
            title='No new company!',
            message='The list has NOT been changed.',
            timeout=20,
        )
    winsound.MessageBeep(winsound.MB_ICONASTERISK)
    logger.info("Windows notification has been sent")


def send_email_notification(is_updated):
    if is_updated:
        title="New Registered Company has been found!!!"
        body="New Company has been added to the list!!"
    else:
        title = "No new company!"
        body = "The list has NOT been changed."
    send_mail(title,body)
    logger.info("E_mail notification has been sent")

