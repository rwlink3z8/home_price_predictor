## Cass County Missouri - Home Price Predictor

Robert Link

http://cchomepricepredictor.com/


##### Data migration in process, documented in the following repository https://github.com/rwlink3z8/hpp2

## Table of Contents
1. TODO
2. Important Notes
3. Background
4. Web App
5. Data Collection and processing
6. Modeling
7. Deployment
8. Future Work

## TODO
- Clean up the code to run the scraper, the data cleaner, the models out of jupyter making it more modular
- Include unit tests

## Important Notes
These scrapers are run with persmission, the links come directly from my real estate agents MLS site and are only good for 60 days, this is relevant to me as I have bought 3 houses in the previous year and it keeps me up to date on my home market

## Background

I wanted to build a tool that anyone could use to get a quick, accurate estimate for home prices in Cass County, Missouri.

I owned a house in my hometown that my brothers construction company renovated, he is a remodel carpenter and he posts his before and after pictures on his companies facebook page. He's been doing this on his own for a few years and when the right opportunity to partner with him on a project came up I took it. I bought this house in March of this year and as of August 20th, we sold the house. We knew from growing up in the area, that in our hometown, a decent estimate of home prices was around $100-$150 per square foot and about $10k per acre of land, but I wanted to apply machine learning to it and try and get better estimates to help us along the way. Also, we switched real estate agents part way through the process and they both got very different appraisals, when I went to open a bank account for our new venture my banker went out to see the property and told me a friend of his, who happened to be a real estate agent, gave a third appraisal. Three different appraisals, varying as much as $120,000. This alone made me want to educate myself on what exactly these properties were worth.  

## Web App

The first image below is the dashboard for the webapp, the user enters the square footage, selects the number of bedrooms, selects the number of bathrooms, enters the lot size in acres, year built or this year if it is a new remodel, and selects the location from the towns in our county, the estimate price button then returns the predicted price from the linear regression model.


![webapp ui](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/webapp.png)


This is the before and the after picture of the house:

**Before**
![housebefore](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/housebefore.jpeg)

**After**
![houseafter](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/house_after.jpg)

## Data Collection and Cleaning

This section is organized by webscrapers in reverse chronilogical order

The latest iteration of the webscraper is available in the file `20201002_full_mls_scraper.py` it utilizes selenium to go into each listing and pull all relevant information from the listing and move to the next listing. The initial selenium scraper took over an hour to obtain listing information for 500 listing, drilling down further into selenium, the subsequent scraper took 15 minutes to obtain this information for 500 listings. This data needs cleaned significantly before it can be modeled usefully and that information can be found in `2020104_data_cleaning.py` file. I believe this is a good approach for lazy loading websites with hidden elements.

Using the second scraper and inspecting the HTML I was able to find that each listing had a latitude and longitude coordinate associated with it as well as price, 95% of the houses fell between $63,000 and $530,000 (2 standard deviations above the mean and 1.25 standard deviations below the mean). Using that information and some slight cleaning with regular expressions I used folium to create the following colormap for the county

**Color Map of home prices**
![colormap](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/cc_colormap.png)

The second iteration of the scraper used requests and beautifulsoup to pull all of the header information which was directly kept in the HTML of each website

Initially, I obtained the mls sites from my real estate agent, scraped the main site with requests and beautiful soup and loaded the data into a pandas dataframe to perform regression. The webscraper is available in the file called `mls_scraper.py`
I wanted to keep the model simple and practical so we could get baseline estimates, so from the mls site I extracted square footage, lot size in acres, number of bedrooms, number of bathrooms, and year built. I also pulled town from the data and dummizied that variable.

`data_cleaning.py`

This is the clean up and feature engineering file for the first iteration of the beautifulsoup scraper

## Modeling and predicting home prices

For modeling I used the log of the sale price as the target because the dataset was skewed, applying the log transform resulted in a normal distribution of the sale price. All of the variables showed good linear relationships with sale price, it is for that reason I decided on a linear regression, two of the strongest were square footage and year built, which are plotted against sale price for the model and the actual data in the testing set. The accuracy score of the model is 76% and the model does a good job as a mean regressor. I plan to update it once a month with new home sales from my real estate agent. After testing it on the test set, I further tested on a small set active listings in the area that were very similar but had slight difference, for example, same features, only differing on lot size, or year built, etc, as a sanity check to make sure the models predictions made sense. 

![square footage vs sale price](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/plt1.png)

![year built vs sale price](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/plt2.png)

the get_price_prediction function in the `ccmohp_eda.ipynb` tests the model with several active listings I pulled from a different real estate website and after I was happy with the model I moved on to deployment.

The only thing not shared on this repo is the webscraper because I do not know if I had permission to scrape that or not and I plan on continuing this work with my real estate agent. 


## Deployment

I pickled the model and sent the columns to a json file, from there these files are opened in `util.py` and the price prediction function is slightly modified to take a python list instead of a numpy array.

`app.py` is the main flask app file that takes the features and returns the predicted price.

`app.html` `app.css` and `app.js` are the front end files for the web app.

The web app is now live hosted by AWS

## Future Work

The initial scraper obtained the listing headers for each listing with beautifulsoup and requests. Recent srapers have been using selenium and can gather more features on each listing.

The original model looked at roughly 1600 listings after cleaning the data, the newest scraper looked at 2035 listings, it uses selenium and can be found in `20201002_full_mls_scraper.py`. The original model achieved an accuracy score of 75% using 6 features. The newest ridge regression model achieved an accuracy score of 82% with 16 features. As the model now sees 14 months worth of data, I believe it would be worth doing time series analysis on. This model can be found in `20201015_viz_and_model.ipynb` and it is currently not being used by the web app.

Current work is focusing on rebuilding the application in Django and putting the data into at least two different SQL tables, one that would have coordinates with prices, and the other obtained from the selenium scraper. I also plan on using this information to generate a choropleth as I believe it, along with the color map will be useful visualizations.

MLS listing information was obtained from my real estate agent and then that site was scraped with permission.


