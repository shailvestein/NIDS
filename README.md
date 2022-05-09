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
- #### I need to minimize false negatives and false positives because if it doesn’t, then it can predict any normal traffic as normal and vice-versa. If it happens it may cause a loss. That is why the evaluation matrix should be f1-score and auc.
- #### The AUC score, which tells the probability of predicting a particular class. A confusion matrix that will also help in interpretation of the ML model.
- #### Found dataset is highly imbalanced, the majority is of normal class and the abnormal class is in minority.
- #### I did use dataprep library for the auto-eda, which helps in analysing some short of plot for each feature in very less time. Later I used seaborn and matplotlib.pyplot for in-depth analysis on features.
- #### Then I’ve tried ML algorithms like Random Forest, SVM, logistic regression, Xgboost, etc. with f1-score and auc-score as classification metric because accuracy is not good metric when the data is highly imbalanced.
- #### From the above heatmap we found that XGBoost and Random Forest had performed well from our base model Naive Bayes but the xgboost with default parameters have very similar auc and f1-score for both train and test data.
- #### Hence, I can conclude that our XGBoost model with default parameters is like more generalized model from all the models with best auc and f1-score.
