## Background

I own a house in my hometown that my brothers construction company is renovating, he is a remodel carpenter and he posts his before and after pictures on his companies facebook page. He's been doing this on his own for a few years and when the right opportunity to partner with him on a project came up I took it. I bought this house in March of this year and as of July 8th, we have listed it for sale. We knew from living there, that in our hometown a decent, rough estimate of home prices was around $100 per square foot and about $10k per acre of land, but I wanted to apply machine learning to it and try and get better estimates to help us along the way. 

The first image below is the dashboard for the webapp, the user enters the square footage, selects the number of bedrooms, selects the number of bathrooms, enters the lot size in acres, year built or this year if it is a new remodel, and selects the location from the towns in our county, the estimate price button then returns the predicted price from the linear regression model.


![webapp ui](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/webapp.png)



This is the before and the after picture of the house:

**Before**
![housebefore](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/housebefore.jpeg)

**After**
![houseafter](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/house_after.jpg)

**Process**

I obtained the mls sites from my real estate agent, scraped the mls sites with beautiful soup and dumped the data into a pandas dataframe. I wanted to keep the model simple and practical so we could get baseline estimates, so from the mls site I extracted square footage, lot size in acres, number of bedrooms, number of bathrooms, and year built. I also pulled town from the data and dummizied that variable. 

`data_cleaning.py`

This is the clean up and feature engineering file for the mls data.

**Model**

For modeling I used the log of the sale price as the target because the dataset was skewed, applying the log transform resulted in a normal distribution of the sale price. All of the variables showed good linear relationships with sale price, it is for that reason I decided on a linear regression, two of the strongest were square footage and year built, which are plotted against sale price for the model and the actual data in the testing set. the rmse of the testing set for the log of the sale price 0.22 and the model does a good job as a mean regressor. I plan to update it once a month with new home sales from my real estate agent. After testing it on the test set, I further tested on a small set active listings in the area that were very similar but had slight difference, for example, same features, only differing on lot size, or year built, etc, as a sanity check to make sure the models predictions made sense. 

![square footage vs sale price](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/plt1.png)

![year built vs sale price](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/plt2.png)


The only thing not shared on this repo is the webscraper because I do not know if I had permission to scrape that or not and I plan on continuing this work with my real estate agent. 

**Predicting Home Price**

the get_price_prediction function in the `ccmohp_eda.ipynb` tests the model with several active listings I pulled from a different real estate website and after I was happy with the model I moved on to deployment.

**Deployment**

I pickled the model and sent the columns to a json file, from there these files are opened in `util.py` and the price prediction function is slightly modified to take a python list instead of a numpy array.

`app.py` is the main flask app file that takes the features and returns the predicted price.

`app.html` `app.css` and `app.js` are the front end files for the web app.

Currently working now to deploy the app with AWS. Plan is to update the model once a month with new sales from my real estate agent, at that point I will also with greater certainty if it is okay to share the webscraper. Future work will take into account school districts, which are not necessarily the same as town. Other features to consider in the future are walkout basements, as those are important selling points to homes in my area, as you can see from the picture, the garage goes into the walkout basement which also has full size storm windows on two sides of the structure.
