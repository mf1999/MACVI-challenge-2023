import fiftyone as fo

dataset = fo.load_dataset("boats-test-dataset2")

session = fo.launch_app(dataset)
session.wait()
