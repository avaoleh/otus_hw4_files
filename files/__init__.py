import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_FILE = get_path("books.csv")
JSON_FILE = get_path("users.json")
JSON_FILE_W = get_path("users_w.json")
