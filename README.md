# Yolov8-OpenImagesv7
This is my project for the application for the position of AI engineer for Codeasy.

# Approach 1.
I dowloaded the dataset using OIDv4 ToolKit, which dowloads the latest OpenImages dataset.\
To do so, first I had to clone the OIDv$ ToolKit github repository using the following command:\
`git clone https://github.com/EscVM/OIDv4_ToolKit.git`

After that, I downloaded all the requirements using the following command:
`pip install -r requirements.txt`

Finally for the dataset download, I downloaded it using the following commands:
`python main.py downloader --classes Owl --type_csv All`
`python main.py downloader --classes Sheep --type_csv All`
Each command downloaded one class. `--type_csv All` argument ensures that we download train, validation and test splits.

Next, I uploaded the downloaded images and the accompanying .txt files to Roboflow to convert the downloaded .txt files to Yolov8 format.

