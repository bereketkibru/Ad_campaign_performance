A/B Hypothesis Testing: Ad campaign performance
# Project Overview
SmartAd is a mobile first advertiser agency. It designs intuitive touch-enabled advertising. It provides brands with an automated advertising experience via machine learning and creative excellence. Their company is based on the principle of voluntary participation which is proven to increase brand engagement and memorability 10 x more than static alternatives.
SmartAd provides an additional service called Brand Impact Optimiser (BIO), a lightweight questionnaire, served with every campaign to determine the impact of the creative, the ad they design, on various upper funnel metrics, including memorability and brand sentiment. 
As a Machine learning engineer in SmartAd, one of my tasks is to design a reliable hypothesis testing algorithm for the BIO service and to determine whether a recent advertising campaign resulted in a significant lift in brand awareness.

# Data and versions
* The data is collected from two groups(exposed and controlled) answering a yes or no question.
* There are basically three versions of the data that are managed using DVC
    * v1 the raw data
    * v3 cleaned data without the platform_os column
    * V4 cleaned data without the Browser column

# Notebooks
* There are four notebooks in the notebooks directory
    * AdCampaignPerformance.ipynb : Basic  data exploration and classical A/B testing
    * sequential_testing.ipynb: Impelmentation of sequential testing
    * Browser.ipynb: ML A/B testing of the dataset without the Platform_os column
    * Platform.ipynb: ML A/B testing of the dataset without the Browser column
# Scripts
    * split_browser.py: simple script to load the right version of the data and drop the browser column and save the data.
    * split_paltform.py: simple script to load the right version of the data and drop the platform_os column and save the data.
