# Network Intrusion Detection System(NIDS) using Machine Learning
This repository is about my first end-to-end network intrusion detection system (NIDS) project.

## Blog of this project
- #### [Network Intrusion Detection using Machine Learning on medium.com]
- #### [Dataset source](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)

## Repository structure
- #### Data cleaning and exploratory data analysis notebook
- #### Model tuning, training and evaluation notebook

## Short Description
- ####  A network intrusion is described as any unauthorized activity on a computer network that cause damage to the function of whole infrastructure
- #### My approach: Those are cleaning data, preprocessing, EDA based on the class labels and eliminated highly correlated features from dataset.
- #### Found dataset is highly imbalanced, the majority is of normal class and the abnormal class is in minority.
- #### Then I’ve tried ML algorithms like Random Forest, SVM, logistic regression, Xgboost, etc. with f1-score and auc-score as classification metric because accuracy is not good metric when the data is highly imbalanced.
- #### From the above heatmap we found that XGBoost and Random Forest had performed well from our base model Naive Bayes but the xgboost with default parameters have very similar auc and f1-score for both train and test data.
- #### Hence, I can conclude that our XGBoost model with default parameters is like more generalized model from all the models with best auc and f1-score.
