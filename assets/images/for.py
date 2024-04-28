from PIL import Image
import os


for img in os.listdir("orchid_intro"):
    pimg = os.path.join("orchid_intro",img)
    c = Image.open(pimg)
    c.save(os.path.join("orchid_intro",img))