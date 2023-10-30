import json
import os
from ultralytics import YOLO
import cv2


def fix_id(idd):
    if idd == 0:
        return 1

    elif idd == 1:
        return 3

    elif idd == 2:
        return 5

    elif idd == 3:
        return 11

    elif idd == 4:
        return 12

    elif idd == 5:
        return 13

    elif idd == 6:
        return 14

    elif idd == 7:
        return 15

    elif idd == 8:
        return 16

    elif idd == 9:
        return 17

    elif idd == 10:
        return 19

    else:
        print("UNKNOWN ID:", idd)
        return None


if __name__ == "__main__":
    imgs_fpath = "C:/Users/matej/Downloads/LARS dataset/datasets/val/images"
    yolo_fpath = "C:/Users/matej/Downloads/LARS dataset/Sibenik and LARS yolov8x.pt"
    empty_results_fpath = "C:/Users/matej/PycharmProjects/macvi-usv-odce-toolkit-2024/lars_val_empty.json"

    print(f"Loading YOLO model from: {yolo_fpath}")
    model = YOLO(yolo_fpath)

    with open(empty_results_fpath) as json_file:
        data = dict(json.load(json_file))
        ctr = 0
        for annotation in data["annotations"]:
            ctr += 1
            print(ctr/len(data["annotations"]))

            img_name = annotation["file_name"].split('.')[0] + ".jpg"
            img_path = os.path.join(imgs_fpath, img_name)
            img = cv2.imread(img_path)

            results = model(img)
            for result in results:
                boxes = result.boxes.xywh.numpy()
                classes = result.boxes.cls.numpy()
                for cls, box in zip(classes, boxes):

                    cls = int(cls)
                    cls = fix_id(cls)
                    box = [int(round(x)) for x in box]
                    detection = {"id": cls, "bbox": box}
                    annotation["detections"].append(detection)

        with open('result.json', 'w') as fp:
            json.dump(data, fp)
