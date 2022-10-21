# Tips Data Exploration
## by Adelami Niyi Victor


## Introduction
> This dataset is a compilation of tips given in a restaurant over a period of time. It contains the followind variables:

1. __Total_bill__: The total amoung of food bought 
2.  __Tip__: The amount of tip given
3.  __Sex__: The sex of the person giving the tip
4.  __Smoker__: The smoking status of the tip giver
5.  __Day__: The day of the week (Thur, Fri, Sat and Sun)
6.  __Time__: Time of the Day (Lunch or Dinner)
7.  __Size__: The portions of food bought

## Required Software
Here, jupyter notebook is needed to run this analysis
The following libraries should be installed on the jupyter notebook
    * Pandas 
    * Numpy
    * Matplotlib
    * Seaborn
    * Sklearn

## List of files included in the project
The following files are in this project
    * README.md
    * tips.ipynb


## Data Cleaning 
* There is a duplicated row in the dataset

## Summary of Findings

* The mean tip given is 3
* There are more male than female, more dinner than lunch, more none smoker than smore and there are few Fri actegories in day variable in the dataset. There in need to use mean of these categories while making visualizations
* The mean tip given during dinner is more tha that of lunch. This might be because there are more Dinner scenario in the datset. looking at the violin plot, we can see that the 25 and 75 percentile are almost thesame for both Lunch and Dinner but only the 50 percentile is different


## Key Insights for Presentation

* The amount of tip given is proportional to the total bill.
* There seems to be more tips given on sunday than in any other day.

## Data Model
* In building a model for this data, Linear Regression and Support Vector Machine was tried. LinearSVR performed better in this scenario with a prediction accuracy of 0.5927745568626216. 
* Although the prediction is not a perfect one, other models and parame



## Acknowledgements and credits
sckitlean, stackoverflow, and google search has been of a good help during the implementation of this analysis

## Bugs
The dataset is somehow small, there might be a eed to get more data for a more robust prediction