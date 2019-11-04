from ftplib import FTP


ftp = FTP("""ftp.pyclass.com""")
msg = ftp.login("student@pyclass.com", "student123")
print("connected: %s " % msg)


def all_sub_dirs(curr_dir):
    curr_path = ftp.pwd()
    print(curr_path)
    tabs = curr_path.count('/')
    if not curr_dir:
        print("\t" * tabs + "empty")
        ftp.cwd("..")
        return
    for directory in [f for f in curr_dir if '.' not in f]:
        ftp.cwd(directory)
        all_sub_dirs(ftp.nlst())
    for file_in_dir in [f for f in curr_dir if '.' in f]:
        print("\t" * tabs + file_in_dir)
    ftp.cwd("..")


print("listing files:")
files = ftp.nlst()
print(files)

# all_sub_dirs(files)

# for directory in [f for f in files if '.' not in f]:
#     print(directory)
#     files = ftp.nlst(directory)
#     print(files)

ftp.close()
print("Closed connection")




