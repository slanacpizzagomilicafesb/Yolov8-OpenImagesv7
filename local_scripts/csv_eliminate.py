import csv

classes_csv = r"D:\Documents\codeasy\datasets\open-images-v7\train\metadata\classes.csv"

owl_class_label = ''
sheep_class_label = ''

with open(classes_csv, 'r') as csvfile:
    classes = csv.reader(csvfile)
    for row in classes:
        if row[1] == 'Owl':
            owl_class_label = row[0]
        elif row[1] == 'Sheep':
            sheep_class_label = row[0]
        elif owl_class_label and sheep_class_label:
            break

detections_train_read = r"D:\Documents\codeasy\datasets\open-images-v7\train\images\detections.csv"
detections_valid_read = r"D:\Documents\codeasy\datasets\open-images-v7\validation\images\detections.csv"
detections_test_read = r"D:\Documents\codeasy\datasets\open-images-v7\test\images\detections.csv"

detections_train_write = r"D:\Documents\codeasy\datasets\open-images-v7\train\annots\detections.csv"
detections_valid_write = r"D:\Documents\codeasy\datasets\open-images-v7\validation\annots\detections.csv"
detections_test_write = r"D:\Documents\codeasy\datasets\open-images-v7\test\annots\detections.csv"

with open(detections_train_read, 'r') as fin, open(detections_train_write, 'w',  newline='') as fout:
    detections_in = csv.reader(fin, skipinitialspace=True)
    detections_out = csv.writer(fout, delimiter=',')

    for row in detections_in:
        if row[2] == owl_class_label or row[2] == sheep_class_label:
            detections_out.writerow((row[:13]))
        elif row[0] == 'ImageID':
            detections_out.writerow((row[:13]))

with open(detections_valid_read, 'r') as fin, open(detections_valid_write, 'w',  newline='') as fout:
    detections_in = csv.reader(fin, skipinitialspace=True)
    detections_out = csv.writer(fout, delimiter=',')

    for row in detections_in:
        if row[2] == owl_class_label or row[2] == sheep_class_label:
            detections_out.writerow((row[:13]))
        elif row[0] == 'ImageID':
            detections_out.writerow((row[:13]))

with open(detections_test_read, 'r') as fin, open(detections_test_write, 'w',  newline='') as fout:
    detections_in = csv.reader(fin, skipinitialspace=True)
    detections_out = csv.writer(fout, delimiter=',')

    for row in detections_in:
        if row[2] == owl_class_label or row[2] == sheep_class_label:
            detections_out.writerow((row[:13]))
        elif row[0] == 'ImageID':
            detections_out.writerow((row[:13]))

