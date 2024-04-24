# Yolov8-OpenImagesv7
This is a project I made to detect owls and sheep using Yolov8 and OpenImages v7 database.

# Approach 1.
## Dataset download
I dowloaded the dataset using OIDv4 ToolKit, which dowloads the latest OpenImages dataset. To do so, first I had to clone the OIDv$ ToolKit github repository using the following command:\
`git clone https://github.com/EscVM/OIDv4_ToolKit.git`\

After that, I downloaded all the requirements using the following command:\
`pip install -r requirements.txt`\

Finally for the dataset download, I downloaded it using the following commands:\
`python main.py downloader --classes Owl --type_csv All`\

![OIDv4 ToolKit owl](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/41d19509-0b97-4a38-9798-0a324bf700a7)

`python main.py downloader --classes Sheep --type_csv All`\

![OIDv4 ToolKit sheep](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/5b35c51c-95f2-46e3-8a99-2d5992806a2b)
Each command downloaded one class. `--type_csv All` argument ensures that we download train, validation and test splits.\

## Converting to Yolov8 format
Next, I uploaded the downloaded images and the accompanying .txt files to Roboflow to convert the downloaded .txt files to Yolov8 format.\
After the annotations were converted to Yolov8 format, I exported the dataset using Roboflow's download link:\
![roboflow_dataset_download_colab](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/0ea855fc-c5f9-4c5a-8966-0282f677d3aa)

## Training
For training, I used Google Colab because it offers free GPUs to use and they are better than the one I have locally. The code used can be found in the [yolov8_oiv7.ipynb](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/yolov8_oiv7.ipynb) file.\
In short, I first had to install some required packages, such as the __ultralytics__ and __roboflow__ packages. Then I had to load the dataset prepared on Roboflow using the block of code seen above. After that, I had to edit the data.yaml file so that the paths leading to the data were correct. Next, I downloaded the pre-trained `yolov8n-oiv7.pt` model. Finally, I trained the model using the downloaded model and dataset.\
Results:\
![colab_results_50e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/6258d4fb-8fa5-4c5e-8590-62294716805f)

## Testing

# Approach 2.
This approach is largely the same, the only difference is that the dataset prepared on Roboflow was downloaded locally as a .zip file.\
![roboflow_dataset_download_local](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/c3c9097f-6091-477c-b747-0ba2afc5067b)
After unzipping the files, I downloaded the pre-trained __yolov8n-oiv7.pt__ model, however, I trained the model via the command line using the following command:\
`yolo detect train data=data.yaml model=yolov8-oiv7.pt epochs=10 imgsz=640`\

![local_command_10e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/c986996b-f7fe-4016-b491-807c307e0f5b)
I trained it only on 10 epochs as the training was too strenuous on my GPU.\
Results:\
![local_results_10e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/9fdce00c-a390-4293-90b1-f052ed9eebd9)

## Testing

# Approach 3.
## Dataset download
In this approach I downloaded the dataset using the [dataset_download.py](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/local_scripts/dataset_download.py) script and I downloaded only Owl and Sheep classes. Along with the images came the detections.csv file which contained relevant information about detections in the images, however, it was not in the Yolov8 format. I also had to download the __fiftyone__ package to execute this script.\
![download_script](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/0a28301a-0d16-43eb-98a9-41866a0c5b9a)

## Converting to Yolov8 format
This format of dataset was not in the Yolov8 format so I had to format it to fit.\
First, I executed the [csv_eliminate.py](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/local_scripts/csv_eliminate.py) script which eliminated any rows in the `detections.csv` file which detected non _owl_ or _sheep_ objects as they were not needed.\
Next, I used the [csv_to_txt.py](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/local_scripts/csv_to_txt.py) script to convert the relevant data in the `detections.csv` file into `.txt` files in the Yolov8 format.

## Training
After converting the given files into the Yolov8 format, I was ready to begin training. The script used can be found in the [yolov8_train.ipynb](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/yolov8_train.ipynb) file. But in essence, the training process was the same as it was in __Approach 1.__\
This model was also only trained on 10 epochs because it was done locally.\
Results:\
![local_rucni_results_10e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/7107d3ca-aa15-48b9-bef8-7c2adda024d5)

## Testing
