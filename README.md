# Yolov8-OpenImagesv7
This is a project I made to detect owls and sheep using Yolov8 and OpenImages v7 database.

# Approach 1.
## Dataset download
I dowloaded the dataset using OIDv4 ToolKit, which dowloads the latest OpenImages dataset. To do so, first I had to clone the OIDv4 ToolKit github repository using the following command:\
`git clone https://github.com/EscVM/OIDv4_ToolKit.git`

After that, I downloaded all the requirements using the following command:\
`pip install -r requirements.txt`

Finally for the dataset download, I downloaded it using the following commands:\
`python main.py downloader --classes Owl --type_csv All`


![OIDv4 ToolKit owl](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/41d19509-0b97-4a38-9798-0a324bf700a7)

`python main.py downloader --classes Sheep --type_csv All`


![OIDv4 ToolKit sheep](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/5b35c51c-95f2-46e3-8a99-2d5992806a2b)
Each command downloaded one class. `--type_csv All` argument ensures that we download train, validation and test splits.

## Converting to Yolov8 format
Next, I uploaded the downloaded images and the accompanying `.txt` files to [Roboflow](https://roboflow.com/) to convert the downloaded `.txt` files to Yolov8 format.\
After the annotations were converted to Yolov8 format, I exported the dataset using Roboflow's download link:\
![roboflow_dataset_download_colab](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/0ea855fc-c5f9-4c5a-8966-0282f677d3aa)

## Training
For training, I used [Google Colab](https://colab.google/) because it offers free GPUs to use and they are better than the one I have locally. The code used can be found in the [yolov8_oiv7.ipynb](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/yolov8_oiv7.ipynb) file.\
In short, I first had to install some required packages, such as the __ultralytics__ and __roboflow__ packages. Then I had to load the dataset prepared on Roboflow using the block of code seen above. After that, I had to edit the [data.yaml](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/data.yaml) file so that the paths leading to the data were correct. Next, I downloaded the pre-trained `yolov8n-oiv7.pt` model. Finally, I trained the model using the downloaded model and dataset.\
Results:\
![colab_results_50e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/6258d4fb-8fa5-4c5e-8590-62294716805f)

The training lasted a little less than an hour.

## Testing
The testing of the model is done using the following command:\
`!yolo detect predict model=/path/to/model.pt source='/path/to/image'`
specifically in my case:\
`!yolo detect predict model=/content/drive/MyDrive/best_colab_50e.pt source='/content/owl-sheep-1/test/images/2bc6fded1a1ff77f_jpg.rf.d895bdb06e28cdc155bb22daac1b635f.jpg'`
The model was tested on several images, here are a couple of examples:\
![colab_predict_50e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/6a065659-2331-4ff4-97f7-d4c3352f5790)
![colab_predict_50e_2](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/e16409b0-bc99-442d-979e-9c06ec507689)

# Approach 2.
This approach is largely the same, the only difference is that the dataset prepared on Roboflow was downloaded locally as a `.zip` file.\
![roboflow_dataset_download_local](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/c3c9097f-6091-477c-b747-0ba2afc5067b)

After unzipping the files, I downloaded the pre-trained __yolov8n-oiv7.pt__ model, however, I trained the model via the command line using the following command:\
`yolo detect train data=data.yaml model=yolov8-oiv7.pt epochs=10 imgsz=640`


![local_command_10e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/c986996b-f7fe-4016-b491-807c307e0f5b)

I trained it only for 10 epochs as the training was too strenuous on my GPU.\
Results:\
![local_results_10e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/9fdce00c-a390-4293-90b1-f052ed9eebd9)

The training lasted about two hours.

## Testing
Testing the local model was done using the same command, but with adjusted paths.\
Here are a couple of results:\
![1a75900918483d0d_jpg rf 7a631a7ec17a68c5b9dd67f1c9fe5cd1](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/6a6d439f-4d0f-4c07-9c2b-f8aeb7880342)
![4b628115bbe657a0_jpg rf 3bf4963d20bb8727a3d735f935769377](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/11250018-d6eb-46f6-a214-10a631d4ee7a)

# Approach 3.
## Dataset download
In this approach I downloaded the dataset using the [dataset_download.py](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/blob/main/local_scripts/dataset_download.py) script and I downloaded only Owl and Sheep classes. Along with the images came the `detections.csv` file which contained relevant information about detections in the images, however, it was not in the Yolov8 format. I also had to download the __fiftyone__ package to execute this script.\
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

The training lasted about 1:45 hours.

## Testing
Again, the testing is the same. Here are a couple of examples:\
![2faec3ce69fc47bc](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/bf8bf6ad-1e2a-4209-91f2-48ce6be23262)
![03eb981d8556f73e](https://github.com/slanacpizzagomilicafesb/Yolov8-OpenImagesv7/assets/56551410/d2eef7be-8e9d-477d-8241-61445ed008f1)

# Conclusion
Overall, the best results came from the model trained on Google Colab for 50 epochs, which should come to no surprise as it was trained 5 times as long as the local models. Additionaly, it took much shorter to train the model on Google Colab.\
However, it should be noted that although worse, the results of the local models were not bad. They were not perfect, but they yielded acceptable results for only 10 epochs.
