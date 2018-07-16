import os
def rename_file():
    file_list = os.listdir (r"C:\Users\STEPHEN\Desktop\INTERNSHIP\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("working directory is "+saved_path)
    os.chdir(r"C:\Users\STEPHEN\Desktop\INTERNSHIP\prank\prank")
    
    #rename each file.
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_file()
