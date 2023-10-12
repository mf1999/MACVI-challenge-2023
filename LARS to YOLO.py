import json
import cv2
import os


def main():
    img_folder_path = os.path.normpath("./datasets/LARS/train/images")

    with open('LARS Annotations/train/panoptic_annotations.json') as json_file:
        data = dict(json.load(json_file))

        for img_info in data['images']:
            for image_detail in data['annotations']:
                if img_info['id'] == image_detail['image_id']:
                    img_path = os.path.join(img_folder_path, image_detail['file_name'])
                    img_path = img_path.split('.')[0] + ".jpg"
                    img = cv2.imread(img_path)
                    h, w, _ = img.shape
                    print(img_path)
                    for segment_info in image_detail['segments_info']:
                        cat_id = segment_info['category_id']
                        if cat_id == 1:
                            cat_id = 0
                        elif cat_id == 3:
                            cat_id = 1
                        elif cat_id == 5:
                            cat_id = 2
                        elif cat_id == 11:
                            cat_id = 3
                        elif cat_id == 12:
                            cat_id = 4
                        elif cat_id == 13:
                            cat_id = 5
                        elif cat_id == 14:
                            cat_id = 6
                        elif cat_id == 15:
                            cat_id = 7
                        elif cat_id == 16:
                            cat_id = 8
                        elif cat_id == 17:
                            cat_id = 9
                        elif cat_id == 19:
                            cat_id = 10
                        else:
                            print("IMPOSSIBLE")
                        bbox = segment_info['bbox']
                        category = data['categories']
                        color = category[cat_id]["color"]
                        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), color, 1)

                        if category[cat_id]['isthing']:

                            cv2.putText(img,
                                        f"{category[cat_id]['supercategory']}: {category[cat_id]['name']}",
                                        (bbox[0], bbox[1]),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.65,
                                        (0, 255, 0),
                                        2)
                        else:
                            cv2.putText(img,
                                        f"{category[cat_id]['supercategory']}: {category[cat_id]['name']}",
                                        (int(bbox[0] + bbox[2] / 2), int(bbox[1] + 20)),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.65,
                                        (0, 255, 0),
                                        2)

                        #  divide x_center and width by image width, and y_center and height by image height
                        x_center_norm = (bbox[0] + bbox[2] / 2) / w
                        width = bbox[2] / w
                        y_center_norm = (bbox[1] + bbox[3] / 2) / h
                        height = bbox[3] / h
                        print(cat_id, x_center_norm, y_center_norm, width, height)
                        annotation_file = f"./customanns train/{image_detail['file_name'].split('.')[0] + '.txt'}"
                        with open(annotation_file, 'a') as txt_file:
                            txt_file.write(f'{cat_id} {x_center_norm} {y_center_norm} {width} {height}\n')
                    # cv2.imshow("aaa", img)
                    # cv2.waitKey(0)


if __name__ == '__main__':
    main()
