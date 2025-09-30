# %%
import os
import sys
import shutil

# %%
images_path = r"C:\Users\sterl\AppData\Roaming\marktext\images"
assets_path = r"C:\Users\sterl\Documents\DataTalksClub\ml-zoomcamp\notes-and-tools\assets"
notes_path = r"C:\Users\sterl\Documents\DataTalksClub\ml-zoomcamp\notes-and-tools"

# %%
l_images = os.listdir(images_path)

# %%
for i in l_images:
    shutil.copy(images_path + "\\" + i, assets_path + "\\" + i)

# %%
for n in os.listdir(notes_path):
    if os.path.splitext(notes_path + "\\" + n)[1] == ".md":
        with open(notes_path + "\\" + n, "rb") as file:
            filedata = file.read()
        
        filedata = filedata.decode("utf-8").replace(images_path + "\\", "assets/")

        with open(notes_path + "\\" + n, "w") as file:
            file.write(filedata)

# %%



