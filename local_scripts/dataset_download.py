import fiftyone as fo
import fiftyone.zoo as foz

#
# Load only point labels (potentially negative or mixed) for 25 samples
# from the validation split for tortoise and sea turtle classes
#
# Images that contain all `label_types` and `classes` will be
# prioritized first, followed by images that contain at least one of
# the required `classes`. If there are not enough images matching
# `classes` in the split to meet `max_samples`, only the available
# images will be loaded.
#
# Images will only be downloaded if necessary
#

dataset = foz.load_zoo_dataset(
    "open-images-v7",
    classes = ["Owl", "Sheep"],
    label_types=["detections", "classifications"],
)
session = fo.launch_app(dataset)
session.dataset = dataset