from PIL import Image, ImageOps
import os, cv2

# make padding under img_dir:"images_unpadding"

def has_img_ext(fname):
    ext = os.path.splitext(fname)[1]
    return ext in ('.jpg', '.jpeg', '.png')

def search(dir):
    files = os.listdir(dir)
    for file in files:
        fullFilename = os.path.join(dir, file)
        print(fullFilename)

# padding size
padding_size = 512
dir = "pretreatment/images_unpadding"
img_dir = os.path.realpath(dir)
print(os.path.realpath(img_dir))
img_paths = [os.path.join(dir, k) for k in sorted(os.listdir(img_dir)) if has_img_ext(k)]
for i, img_path in enumerate(img_paths, 1):
    print('[{:3d}/{:3d}] padding image... '.format(i, len(img_paths)))
    img = Image.open(img_path)

    old_size = img.size  # old_size[0] is in (width, height) format

    ratio = float(padding_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    img = img.resize(new_size, Image.ANTIALIAS)
    new_im = Image.new("RGB", (padding_size, padding_size))
    new_im.paste(img, ((padding_size-new_size[0])//2,
                    (padding_size-new_size[1])//2))
    padding_path = os.path.join("./pretreatment/images_unmaking", os.path.basename(img_path)+"mask" + '.png')
    new_im.save(padding_path)
