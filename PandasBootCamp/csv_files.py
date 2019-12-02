from os.path import join as join_path

CSV_PATH = join_path("""C:\\Users\\elevy\\Downloads\\Udemy py\\pandas\\Video_Lecture_NBs""")


def get_path_for_file(csv_name):
    return join_path(CSV_PATH, csv_name)


if __name__ == "__main__":
    pass