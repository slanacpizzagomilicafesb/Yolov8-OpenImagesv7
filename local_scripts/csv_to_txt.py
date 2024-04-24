import csv
import pandas as pd
import os

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

save_folder_train = r"D:\Documents\codeasy\datasets\open-images-v7\train\labels"
save_folder_valid = r"D:\Documents\codeasy\datasets\open-images-v7\validation\labels"
save_folder_test = r"D:\Documents\codeasy\datasets\open-images-v7\test\labels"

detections_train_csv = r"D:\Documents\codeasy\datasets\open-images-v7\train\annots\detections.csv"
detections_valid_csv = r"D:\Documents\codeasy\datasets\open-images-v7\validation\annots\detections.csv"
detections_test_csv = r"D:\Documents\codeasy\datasets\open-images-v7\test\annots\detections.csv"   

detection_train = pd.read_csv(detections_train_csv)

for index, row in detection_train.iterrows():
    #with open(os.path.join(save_folder_train, f'{row["ImageID"]}.txt'), 'a') as file:
    XMin = float(row['XMin'])
    XMax = float(row['XMax'])
    YMin = float(row['YMin'])
    YMax = float(row['YMax'])
    x_center = str((XMax - XMin)/2 + XMin)
    y_center = str((YMax - YMin)/2 + YMin)
    width = str(XMax - XMin)
    height = str(YMax - YMin)
    if row['LabelName'] == owl_class_label:
        class_index = '0'
    elif row['LabelName'] == sheep_class_label:
        class_index = '1'
    file = open(os.path.join(save_folder_train, f'{row["ImageID"]}.txt'), 'a')
    file.write(class_index)
    file.write(" ")
    file.write(x_center)
    file.write(" ")
    file.write(y_center)
    file.write(" ")
    file.write(width)
    file.write(" ")
    file.write(height)
    file.write(" ")
    file.write("\n")
    file.close()

detection_valid = pd.read_csv(detections_valid_csv)

for index, row in detection_valid.iterrows():
    #with open(os.path.join(save_folder_train, f'{row["ImageID"]}.txt'), 'a') as file:
    XMin = float(row['XMin'])
    XMax = float(row['XMax'])
    YMin = float(row['YMin'])
    YMax = float(row['YMax'])
    x_center = str((XMax - XMin)/2 + XMin)
    y_center = str((YMax - YMin)/2 + YMin)
    width = str(XMax - XMin)
    height = str(YMax - YMin)
    if row['LabelName'] == owl_class_label:
        class_index = '0'
    elif row['LabelName'] == sheep_class_label:
        class_index = '1'
    file = open(os.path.join(save_folder_valid, f'{row["ImageID"]}.txt'), 'a')
    file.write(class_index)
    file.write(" ")
    file.write(x_center)
    file.write(" ")
    file.write(y_center)
    file.write(" ")
    file.write(width)
    file.write(" ")
    file.write(height)
    file.write(" ")
    file.write("\n")
    file.close()
        
detection_test = pd.read_csv(detections_test_csv)

for index, row in detection_test.iterrows():
    #with open(os.path.join(save_folder_train, f'{row["ImageID"]}.txt'), 'a') as file:
    XMin = float(row['XMin'])
    XMax = float(row['XMax'])
    YMin = float(row['YMin'])
    YMax = float(row['YMax'])
    x_center = str((XMax - XMin)/2 + XMin)
    y_center = str((YMax - YMin)/2 + YMin)
    width = str(XMax - XMin)
    height = str(YMax - YMin)
    if row['LabelName'] == owl_class_label:
        class_index = '0'
    elif row['LabelName'] == sheep_class_label:
        class_index = '1'
    file = open(os.path.join(save_folder_test, f'{row["ImageID"]}.txt'), 'a')
    file.write(class_index)
    file.write(" ")
    file.write(x_center)
    file.write(" ")
    file.write(y_center)
    file.write(" ")
    file.write(width)
    file.write(" ")
    file.write(height)
    file.write(" ")
    file.write("\n")
    file.close()