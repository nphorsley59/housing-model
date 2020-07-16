# <div align="center">Predicting House Sale Price</div>

### <div align="center">Project Overview</div>
Using a competition dataset available on Kaggle, I created a model that can predict the sale price of a house in Ames, Iowa from 79 explanatory variables (features). The purpose of this project was to demonstrate my ability to tackle a complex dataset and model the behavior of a target variable. For a more in-depth look at this analysis, please refer to my [Jupyter Notebook](https://github.com/nphorsley59/House_Prices/blob/master/House_Prices.ipynb).

### <div align="center">Data Preparation</div>

#### 1. Exploration
I began by familiarizing myself with the Ames, Iowa housing dataset. It was divided into a [train](https://github.com/nphorsley59/House_Prices/blob/master/train.csv) and [test](https://github.com/nphorsley59/House_Prices/blob/master/test.csv) sample, each consisting of roughly 1,500 entries. Each entry held 78 features characterizing the house, lot, and surrounding area. It was the explicit goal of the competition to use the "train" sample (where 'Sale Price' was provided) to predict the 'Sale Price' of houses in the "test" sample.<br />

Due to the complexity of the dataset (Figure 1), a [detailed description](https://github.com/nphorsley59/House_Prices/blob/master/Data_Description.txt) of each of the 78 features was included. I reviewed this information and broke down the full feature list by type (numerical vs categorical) and role (building i.e. describes physical characteristics of house, space i.e. describes size of house, and location i.e. describes the surrounding area) in an [Excel spreadsheet](https://github.com/nphorsley59/House_Prices/blob/master/Feature_Log.xlsx). I also made predictions about the influence of each feature and 'Sale Price' and kept notes throughout the analysis process.<br />

**Figure 1.** Shape of training dataset, demonstrating the complexity of the dataset.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Train_Shape.png "Raw Train Dataset")

#### 2. Cleaning
I addressed several major issues during the cleaning process. First, missing values were widespread in both samples (Figure 2). I assigned a value of 'None' or '0' when 'NaN' clearly represented an entry that lacked the described feature (i.e. 'GarageType' for a house that doesn't have a garage). I dealt with other missing values on a feature-by-feature basis, using whichever method was appropriate. Second, I checked each entry for inconsistencies among shared features (i.e. 'GarageYrBlt', 'GarageFinish', 'GarageQual', etc. all describe a garage). Finally, I checked for typos and dropped uninformative features. Most of the cleaning required for this dataset was fairly lightweight, especially in the "train" sample.<br />

NOTE: The full dataset remained separated into "train" and "test" samples for cleaning to avoid [data leakage](https://machinelearningmastery.com/data-leakage-machine-learning/).<br />

**Figure 2.** Summary of missing data in the "test" sample.<br />

![alt_text](https://github.com/nphorsley59/House_Prices/blob/master/Figures/MissingData.png "Missing Data")

#### 3. Feature Engineering
The purpose of this step was to simplify the dataset, create new features that could inform the model, and ensure the structure of each feature was conducive to analysis. I began by merging the "train" and "test" samples to ensure changes were reflected in both. I then removed several uninformative features, including 'Id', 'Utilities', and 'PoolQC', and changed the data type for several others. I only wanted to keep features that could influence Sale Price, were known for most of the dataset, and contained variation. I also wanted to ensure the data type reflected the substance of the feature. The final step was to encode the heirarchical features that were not already numeric (Figure 3). For example, 'BsmtQual' has a clear linear relationship with SalePrice; higher quality basements are worth more money. Encoding allows the model to easily incorporate these features.

**Figure 3.** Correcting data types and heirarchical encoding of non-numeric features.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Heir_Encoding.png "Feature Engineering")

### <div align="center">Quantitative Features</div>

![alt_text](https://github.com/nphorsley59/House_Prices/blob/master/Figures/CorrMap_10.png "Correlation Heatmap")

### <div align="center">Qualitative Features</div>

![alt_text](https://github.com/nphorsley59/House_Prices/blob/master/Figures/Qual_Feat_Boxplots.png "Qualitative Features vs Sale Price")

### <div align="center">Normalize Data</div>

#### 1. Response Variable

#### 2. Explanatory Variables

#### 3. Visual Check

### <div align="center">Regression Modeling</div>

### <div align="center">Results</div>

### <div align="center">Resources</div>
https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview
