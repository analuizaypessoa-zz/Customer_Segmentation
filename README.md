# Customer_Segmentation

The aim of this project is to use clustering models with mixed data types to better understand customers profiles and gain insights.


## Data sources:

To use mixed data types (categorical and numerical), I used as input Starbucks kaggle dataset:  [link](https://www.kaggle.com/mahirahmzh/starbucks-customer-retention-malaysia-survey?select=Starbucks+satisfactory+survey.csv)

## Setting

First create a dedicated conda environment:

```bash
conda create -y -n customer_segmentation python=3.6
conda activate customer_segmentation
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=customer_segmentation
```

Install all the requirements:

```bash
pip install -r requirements.txt
```

## Folder structure :

Customer segmentation has the following structure:

```
CUSTOMER_SEGMENTATION/
├── bin/
│   ├── kprototypes.pickle  >> model binary saved 
├── data/
│   ├── Cleaned/
│   │   ├── df.csv
│   ├── Raw/
│   │   ├── starbucks_dataset_raw.csv
├── notebooks/
│   ├── dataPrep.ipynb
│   ├── dataAnalysis.ipynb
│   ├── Kprototypes.ipynb
├── Outputs/
│   ├── Clusters_Mode.csv
│   ├── model_(date).csv
├── requirements.txt
```

###  Insights dataviz (WIP)
- Dashboard with main insights and clusters found : [link to Google DataStudio](https://datastudio.google.com/reporting/92343e86-9e99-4ec2-9400-d7223fd95fe7)
