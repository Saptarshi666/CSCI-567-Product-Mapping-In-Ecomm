# CSML-Product-Mapping-Dataset

## Preparation

### Paracrawl Data Process
* Download the [paracrawl](https://web-language-models.s3.us-east-1.amazonaws.com/paracrawl/release9/en-cs/en-cs.txt.gz) dataset (3.9GB zip file)
* Unzip the file and place the `en-cs.txt` (9.01GB) in the `datasets` folder
* Create the english vocabulary by running [paracrawl.py](paracrawl.py)
* Vocab file is created as [english_words.txt](features/english_words.txt) in the `features` folder

### Image Scraping
* Run [Scraping.ipynb](Scraping.ipynb) to download the images in real time
* Alternatively, download the `ProMapEn` folder from [link](https://drive.google.com/drive/folders/1hfqp-LqDahBHWRcAtenxlIlQf0K3yzJH) and place it in the `images` folder

## Feature Engineering
* insert

## Credits
[kackamac](https://github.com/kackamac/Product-Mapping-Datasets)
Thanks for the wonderful dataset