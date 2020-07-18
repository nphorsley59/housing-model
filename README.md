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
The purpose of this step was to simplify the dataset, create new features that could inform the model, and ensure the structure of each feature was conducive to analysis. I began by merging the "train" and "test" samples to ensure changes were reflected in both. I then removed several uninformative features, including 'Id', 'Utilities', and 'PoolQC', and changed the data type for several others. I only wanted to keep features that could influence Sale Price, were known for most of the dataset, and contained variation. I also wanted to ensure the data type reflected the substance of the feature. The final step was to encode the heirarchical features that were not already numeric (Figure 3). For example, 'BsmtQual' has a clear linear relationship with 'SalePrice'; higher quality basements are worth more money. Encoding allows the model to easily incorporate these features.

**Figure 3.** Correcting data types and heirarchical encoding of non-numeric features.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Heir_Encoding.png "Feature Engineering")

### <div align="center">Quantitative Features</div>
Now that the dataset had been cleaned and organized, it was time for an exploratory data analysis. This is especially valuable in such a large, complex dataset, where a few features may hold most of the predictive power for 'SalePrice'. I started by making a correlation heatmap of the quantitative features (Figure 4). 'OverallQual', 'GrLivArea', and 'ExterQual' came out as the strongest quantitative predictors of 'SalePrice'. These features will undoubtedly play a significant role in my regression model. I also noted strong relationships between 'TotRmsAbvGrd' and 'GrLivArea', 'FullBath' and 'TotBath', '1stFlrSF' and 'TotalBsmtSF', and 'GarageArea' and 'GarageCars'. In each of these cases, I should consider removing the weaker predictor from the dataset.<br/>

**Figure 4.** A correlation heatmap of all quantitative features, showing meaningful predictive features and potential multicollinearity.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/CorrMap_15.jpg "Correlation Heatmap")<br/>

Next, I explored my strongest quantitative predictors independently and removed any obvious outliers (Figure 5). Several of these features had heteroscedastic distributions which would need to be normalized in a future step.  

**Figure 5.** Scatterplot of 'GrLivArea' and 'SalePrice'; outliers circled in black.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/LivingArea_Scatter1.png "Outliers")

### <div align="center">Qualitative Features</div>

I continued my exploratory data analysis by visualizing some of the qualitative features I expected to influence 'SalePrice'. Several of these described the location of the house and could be related, so I visualized them independently and together (Figure 6, 7). In general, I expected most qualitative features to have a weak influence on 'SalePrice' and found very few strong relationships.<br/>

**Figure 6.** Box and whisker plot showing variation in sale price for four qualitative variables. 'MSSubClass' describes the housing type and 'MSZoning' describes the zoning of the surrounding area.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Qual_Feat_Boxplots.jpg "Qualitative Features")<br/>

**Figure 7.** Swarmplot showing relationship between 'Neighborhood', 'MSZoning', and 'SalePrice'.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/NeighbrhdZoning.jpg "Qualitative Relationships")

### <div align="center">Normalize Data</div>

#### 1. Response Variable
Before modeling, I checked the distribution and normality of my data. This was especially important for the response (target) variable, so that's where I began. I found that 'SalePrice' was skewed left quite significantly (Figure 8). To fix this, I performed a log(x+1) transformation (Figure 9).<br/>

**Figure 8.** The raw distribution (blue curve) of 'SalePrice' compared with a normal distribution (black curve).<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Raw_Distribution.png "Raw Distribution")<br/>

**Figure 9.** The transformed distribution (blue curve) of 'SalePrice' compared with a normal distribution (black curve).<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Log_Distribution.png "Log-Transformed Distribution")<br/>

#### 2. Explanatory Variables
I was also interested in tranforming particularly skewed explanatory variables (features). I set a cutoff of skew >= 1 and used a Box Cox transformation. I visually inspected my strongest predictors from my exploratory data analysis and was satisfied with the results (Figure 10). Notice that the heteroscedasticity noted earlier has been corrected.<br/>

**Figure 10.** Scatterplot of 'GrLivArea' and 'SalePrice' after a Box Cox transformation.<br/>

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/LivingArea_Scatter3.jpg)

### <div align="center">Regression Modeling</div>

#### 1. Preparation
A few final steps were required to prepare the dataset for training and testing models. First, I turned all qualitative features into [dummy variables](https://en.wikipedia.org/wiki/Dummy_variable_(statistics)). Then, I separated the "test" data from the "train" data; 'SalePrice' is unknown for the "test" data, so it won't be helpful for model building. Finally, I further separated the "train" data into a "train" group and a "test" group. The "train" group was used to inform the model and the "test" group was used to test the model's accuracy. I did this step manually to create visualizations, but when actually testing models this was replaced with automated [cross-validation](https://towardsdatascience.com/cross-validation-in-machine-learning-72924a69872f) executed by a custom function.

#### 2. Building and Testing Models
I chose to mostly use regularized linear models due to the complexity of the dataset. These types of models help reduce overfitting. I also preprocessed the data using [RobustScaler()](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html) to reduce the influence of outliers that weren't manually removed. This resulted in a Ridge Regression model, Lasso Regression model, and an Elastic Net Regression model, which each use different techniques for constraining the weights of the parameters (Figure 11). In addition to regularized linear models, I used a Gradient Boost algorithm, which essentially compares predictors to their predecessors and learns from the errors. Each of these models performed fairly well, producing RMSE (root mean square error) values around 0.10-0.15.

**Figure 11.** Visual comparison of the performance of four unique models built using machine learning algorithms.

![alt_text](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/Figures/Regression_Models.jpg "Regression Models")

To test these models more rigorously, I created a custom cross-validation function (Figure 12).

#### 3. Stacking Models
Stacking is an [ensemble method](https://towardsdatascience.com/ensemble-methods-in-machine-learning-what-are-they-and-why-use-them-68ec3f9fef5f#:~:text=Ensemble%20methods%20is%20a%20machine,machine%20learning%20and%20model%20building.) that can improve the accuracy of model predictions by combining the strenghts of multiple models. This is an advanced method that I am still in the process of learning (it is not supported by scikit-learn) and implementing.

### <div align="center">Submission</div>
Now that I had several relatively accurate models, I used the model with the best cross-validation score to predict 'SalePrice' for the "test" sample. I have included the [results](https://github.com/nphorsley59/Predicting_Sale_Price/blob/master/submission.csv) as a csv in this repository.

### <div align="center">Resources</div>
https://www.kaggle.com/c/house-prices-advanced-regression-techniques/overview<br/>
https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/<br/>
