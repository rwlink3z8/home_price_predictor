## Cass County Missouri - Home Price Predictor

Robert Link

http://cchomepricepredictor.com/

## Table of Contents
1. Background
2. Web App
3. Data Collection and processing
4. Modeling
5. Deployment
6. Future Work

## Background

I own a house in my hometown that my brothers construction company is renovating, he is a remodel carpenter and he posts his before and after pictures on his companies facebook page. He's been doing this on his own for a few years and when the right opportunity to partner with him on a project came up I took it. I bought this house in March of this year and as of July 8th, we have listed it for sale. We knew from growing up in the area, that in our hometown, a decent estimate of home prices was around $100-$150 per square foot and about $10k per acre of land, but I wanted to apply machine learning to it and try and get better estimates to help us along the way. Also, we switched real estate agents part way through the process and they both got very different appraisals, when I went to open a bank account for our new venture my banker went out to see the property and told me a friend of his, who happened to be a real estate agent, gave a third appraisal. Three different appraisals, varying as much as $120,000. This alone made me want to educate myself on what exactly these properties were worth.  

## Web App

The first image below is the dashboard for the webapp, the user enters the square footage, selects the number of bedrooms, selects the number of bathrooms, enters the lot size in acres, year built or this year if it is a new remodel, and selects the location from the towns in our county, the estimate price button then returns the predicted price from the linear regression model.


![webapp ui](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/webapp.png)


This is the before and the after picture of the house:

**Before**
![housebefore](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/housebefore.jpeg)

**After**
![houseafter](https://github.com/rwlink3z8/home_price_predictor/blob/master/img/house_after.jpg)

## Data Collection and Cleaning

I obtained the mls sites from my real estate agent, scraped the mls sites with beautiful soup and dumped the data into a pandas dataframe. I wanted to keep the model simple and practical so we could get baseline estimates, so from the mls site I extracted square footage, lot size in acres, number of bedrooms, number of bathrooms, and year built. I also pulled town from the data and dummizied that variable. 

`data_cleaning.py`

This is the clean up and feature engineering file for the mls data.

## Modeling and predicting home prices

For modeling I used the log of the sale price as the target because the dataset was skewed, applying the log transform resulted in a normal distribution of the sale price. All of the variables showed good linear relationships with sale price, it is for that reason I decided on a linear regression, two of the strongest were square footage and year built, which are plotted against sale price for the model and the actual data in the testing set. the rmse of the testing set for the log of the sale price 0.22 and the model does a good job as a mean regressor. I plan to update it once a month with new home sales from my real estate agent. After testing it on the test set, I further tested on a small set active listings in the area that were very similar but had slight difference, for example, same features, only differing on lot size, or year built, etc, as a sanity check to make sure the models predictions made sense. 

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

My plan is to update the model once a month with new sales from my real estate agent, at that point I will also with greater certainty if it is okay to share the webscraper. Future work will take into account school districts, which are not necessarily the same as town. Other features to consider in the future are walkout basements, as those are important selling points to homes in my area, you can see from the picture, the garage goes into the walkout basement which also has full size storm windows on two sides of the structure. I would also like to add features such as paved driveway, cul-de-sac, pool, detached shop, etc to fine tune later models. 

MLS listing information was obtained from my real estate agent but it could easily be obtained by scraping other popular real estate websites. The flask app here still shows the development server, updating that to waitress to run on a production server


if you're still reading this far maybe you'd enjoy a song lyric that's not at all a rip off of a rip off ;)

I call it....seasons of code

525,600 features

525,000 beta coefficients

525,000 boosting algorithms

How can I build you 1 decision tree?

There’s lasso, and gradient, and the worst ever neural network

There’s Booleans, and bitwise, and eigen vectors

what are their values?!?!?

There’s a dude that doesn’t go here 

doesn’t even know lambda functions

There’s help if, you ask enough

But only for KNN

And what about scorrreees

Scorrreeees

Just made up math.


................................................or maybe this other one i hacked together?

I've been staring at the monitor

long as a nueron can remember

no matter how hard i type

all the strings I write.....

i wish i could be the perfect coder

i come back to the monitor....

every loop i write 

all the code I hack

every path/to/file incorrect

all the code leads back

to the code i know

that will run so slow....


.........................that has to be all of the hacky disney and musical rip offs right?

well...

do you wanna build a model?

come on lets go and code!

i never write while loops anymore 

my models are so poor 

it's like I found a minima!

do you wanna build a model?

a machine learning model?

I think some cross val is overdue 

i've started talking to the function callssss!

it gets a little lonely

all these empty cells 

just watching the epochs tick by

data are you in there?

people are asking what you mean (shoulder shrug emoji, bewildered i dunno emoji)

people say code harder and I'm trying skew, just set up git pull

we only have two branches....just me and you... what are we going to code?


