import os

if __name__ == "__main__":
    root_folder = os.path.normpath("E:/MACVI/v7/train")
    imgs_folder = os.path.join(root_folder, "images")

    for img_name in os.listdir(imgs_folder):
        img_prefix = img_name.split(".", 1)[0]
        same = [img_name]
        for img_namee in os.listdir(imgs_folder):
            if img_name == img_namee:
                continue
            img_prefixx = img_namee.split(".", 1)[0]
            if img_prefix == img_prefixx:
                same.append(img_namee)
        if len(same) != 1:
            for e in same:
                print(e)
            print()