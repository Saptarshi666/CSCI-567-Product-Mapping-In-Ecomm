# CSML-Product-Mapping-Dataset


## Objective
Replicate methods and technologies outlined in the paper to achieve end-to-end results for the ProMapEn dataset.


## Preparation

#### Paracrawl Data Process
* Download the [paracrawl](https://web-language-models.s3.us-east-1.amazonaws.com/paracrawl/release9/en-cs/en-cs.txt.gz) dataset (3.9GB zip file)
* Unzip the file and place the `en-cs.txt` (9.01GB) in the `datasets` folder
* Create the english vocabulary by running [paracrawl.py](paracrawl.py)
* Vocab file is created as [english_words.txt](features/english_words.txt) in the `features` folder

#### Image Scraping
* Run [Scraping.ipynb](Scraping.ipynb) to download the images in real time
* Alternatively, download the `ProMapEn` folder from [link](https://drive.google.com/drive/folders/1hfqp-LqDahBHWRcAtenxlIlQf0K3yzJH) and place it in the `images` folder


## Final Directory Structure
Before beginning with feature engineering, cross verify the folder and file placement as per below directory tree

```
├── Evaluation.ipynb
├── Feature-Engineering-Part-1.ipynb
├── Feature-Engineering-Part-2.ipynb
├── Model-Building-Grid-and-Random-Search-CV.ipynb
├── README.md
├── Scraping.ipynb
├── datasets
│   ├── ProMapCz
│   │   ├── promapcz-test_data_similarities.csv
│   │   └── promapcz-train_data_similarities.csv
│   ├── ProMapEn
│   │   ├── promapen-test_data.csv
│   │   ├── promapen-test_data_similarities.csv
│   │   ├── promapen-train_data.csv
│   │   └── promapen-train_data_similarities.csv
│   ├── README.md
│   ├── amazon-google
│   │   ├── amazon_google-test_data_similarities.csv
│   │   └── amazon_google-train_data_similarities.csv
│   ├── amazon-walmart
│   │   ├── amazon_walmart-test_data_similarities.csv
│   │   └── amazon_walmart-train_data_similarities.csv
│   └── en-cs.txt
├── features
│   ├── ProMapEn
│   │   ├── images_test_similarties.csv
│   │   ├── images_train_similarties.csv
│   │   ├── promapen_test_similarities.csv
│   │   └── promapen_train_similarities.csv
│   └── english_words.txt
├── images
│   ├── ProMapEn
│   │   ├── test
│   │   └── train
│   └── readme_imgs
│       └── FileStructure.png
├── paracrawl.py
└── results
    ├── ProMapEn
    │   └── result-10-models.csv
    └── all-test-data.csv
```


## Feature Engineering
* insert

## Credits
[kackamac](https://github.com/kackamac/Product-Mapping-Datasets)
Thanks for the wonderful dataset