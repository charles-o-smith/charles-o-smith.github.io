from PIL import Image
import os

# set image locations
image_dir = "/Users/charles/codebase/charles-o-smith.github.io/images/"
thumb_dir = "/Users/charles/codebase/charles-o-smith.github.io/thumbs/"

#single = "budding_abolitionist.jpg"
#single = "me_my_demons.jpeg"
single = "zeke.jpeg"

def gen_all(image_dir, thumb_dir):
    for file in os.listdir(image_dir):
        thumb = (thumb_dir+"thumb_" + file)
        try:
            image = Image.open(image_dir+file)
            h = image.size[0]
            w = image.size[1]
            if h > 1000:
                thumb_h = h//10
                thumb_w = w//10
                image.thumbnail((thumb_h, thumb_w))
                image.save(thumb, "JPEG")
            else:
                image.thumbnail((h, w))
                image.save(thumb, "JPEG")
        except:
            print(f'Not processing {file}')

#gen_all(image_dir, thumb_dir)

def gen_one(single):
    thumb = (thumb_dir+"thumb_" + single)
    try:
        image = Image.open(image_dir+single)
        h = image.size[0]
        w = image.size[1]
        if h > 1000:
            thumb_h = h//10
            thumb_w = w//10
            image.thumbnail((thumb_h, thumb_w))
            image.save(thumb, "JPEG")
        else:
            image.thumbnail((h, w))
            image.save(thumb, "JPEG")
    except:
                print(f'Not processing {single}')

gen_one(single)