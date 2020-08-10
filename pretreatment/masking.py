from PIL import Image, ImageOps
import os, cv2

# make padding under img_dir:"images_unpadding"

def has_img_ext(fname):
    ext = os.path.splitext(fname)[1]
    return ext in ('.jpg', '.jpeg', '.png')

# padding size
padding_size = 512
dir = "images_unmaking"
img_dir = os.path.realpath(dir)
print(os.path.realpath(img_dir))
img_paths = [os.path.join(dir, k) for k in sorted(os.listdir(img_dir)) if has_img_ext(k)]


for i, img_path in enumerate(img_paths, 1):
    print('[{:3d}/{:3d}] masking image... '.format(i, len(img_paths)))
    img = Image.open(img_path)
    img = img.convert("RGBA")
    datas = img.getdata()
    print(len(datas))
    print(img.size[0])
    y = img.size[0]
    print(img.size[1])
    x = img.size[1]

    img_f = []
    img_mask_f = []

    for item, index in zip(datas, range(0, len(datas) + 1)):
        print(item)
        if item[0] == 0 and item[1] == 0 and item[2] == 0 and item[3] == 255:
            # 검정으로 masking
            img_mask_f.append((0, 0, 0, 255))
            img_f.append((0, 0, 0, 255))
        else:
            img_f.append(item)
            img_mask_f.append((255, 255, 255, 255))
        # print(index)

    img.putdata(img_mask_f)
    img.save("../sample_images/ryota_mask.png", "PNG")
    img.putdata(img_f)
    img.save("../sample_images/ryota.png", "PNG")