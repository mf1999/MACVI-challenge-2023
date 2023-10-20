import fiftyone as fo

dataset = fo.load_dataset("open-images-v7-train-20000")

# Retrieve a saved view
boats_view = dataset.load_saved_view("boat")
print(boats_view)


# The Dataset or DatasetView containing the samples you wish to export
dataset_or_view = boats_view

dataset_type = fo.types.COCODetectionDataset  # for example

# Export the dataset
# Export the labels in the `ground_truth` field in COCO format, and
# move (rather than copy) the source media to the output directory
dataset_or_view.export(
    export_dir="./exported",
    dataset_type=fo.types.COCODetectionDataset,
    label_field="ground_truth",
    export_media="move",
)
