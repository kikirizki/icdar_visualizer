from visualize import Icdar2019Visualizer
vis = Icdar2019Visualizer(
    "2015",
    "/home/robert/DATASET/license_plate_dataset_13_sep_2019/images/train",
    "/home/robert/DATASET/license_plate_dataset_13_sep_2019/labels/train"
)
vis.slide_show()