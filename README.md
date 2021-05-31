# Analysis of King County Home Prices

**Authors:** Aaron Cherry, Ryan Reilly
![title](images/king_county_1.jpeg)

## Overview

This project analyzes data for over 21,000 home sales in King County, WA during 2014 and 2015. The goal of this analysis is to determine what features of a house drive the sale price. This will be done through exploratory daa analysis and inferential linear regression modeling of the housing data.

## Business Problem

Blue Sky Realty is a large real estate agency that helps homeowners buy/sell homes. Blue Sky has a large presence on the west coast, primarily in California and Oregon. However, they still have not expanded to Washington, until now. This will be there first office in Washington and there knowledge of what drives home prices is limited. They will be starting in King County. Since they are new to King County, they have requested our assistance. Through our analysis, we are going to provide recommendations to Blue Sky based on the followingL 

- Where to sell a home based on recent trends
- Which features of the home will drive the sale price of your clients home

## Data Understanding

Each row in this dataset represents a unique home sale in King County and surrounding information about the home. There is a unique ID and Sale Date, along with 19 other features about the home, including the sale price, square feet, number of bedrooms, number of bathroooms, condition of home, among other features. Inlcuded in these features is geo data of the home, which we will also explore.  

| Feature | Description|
|:------- | :-------|
|id| Unique ID for each home sold|
|date|  Date of the home sale|
|price| Price of each home sold|
|bedrooms|  Number of bedrooms|
|bathrooms|  Number of bathrooms, where .5 accounts for a room with a toilet but no shower|
|sqft_living|  Square footage of the apartments interior living space|
|sqft_lot|  Square footage of the land space|
|floors|  Number of floors|
|waterfront|  A dummy variable for whether the apartment was overlooking the waterfront or not|
|view|  An index from 0 to 4 of how good the view of the property was|
|condition|  An index from 1 to 5 on the condition of the apartment,|
|grade|  An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above|  The square footage of the interior housing space that is above ground level|
|sqft_basement|  The square footage of the interior housing space that is below ground level|
|yr_built|  The year the house was initially built|
|yr_renovated|  The year of the house’s last renovation|
|zipcode|  What zipcode area the house is in|
|lat|  Lattitude|
|long|  Longitude|
|sqft_living15|  The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15|  The square footage of the land lots of the nearest 15 neighbors|

## Data Preparation

Since most homes are not on the waterfront and it does not make sense for that value to be missing (the home is either on waterfront or it isn't), lets fill the N/As with 0 and assume these homes are not waterfront homes. 

Since a 0 value does not make sense for yr_renovated, we would probably mark those as NA, which would give us a total amount of NAs of 20,853 (17011 zeros + 3842 NAs). Instead, we are going to mark year renovated as 1 (is has been renovated) or 2(has not been renovated). We will take care of this in feature engineering, then drip the original row. Since the most common value is 0 for indicating the view of the property, lets replace the 63 nulls with 0 as well.

#### Dealing with outliers

Of all the numerical variables, the one one house with 33 bedrooms does not make sense because the house is only 1620 square feet. We removed this row above.

# Feature Engineering

Any grade of a home that is 3 or less falls short of building contruction and design. Any grade that is 11 or above has a high quality of design. Any grade in between will have a medium quality.
<br>

These month columns were created so we could explore seasonality in sales over the two year period of data we have. 

# Exploratory Data Analysis

#### Should a seller consider what time of year to list there home? Should a buyer consider when to buy a home?

![title](images/king_county_1.jpeg)
<br>

It looks like the most home were sold in May over the two year period of data we have. Home sales look to be hot in the spring and summer months, and slow down only slighlty in the fall and more so in the winter. 

#### Do the number of bathrooms have an effect on the price of the house

![title](images/king_county_1.jpeg)
<br>

This scatter shows a positive relationship between square feet and sales price. You can see as the points get darker towards the top, the more bathrooms there are for a home. This shows that the number of bathrooms could help indicate the sale price. 

#### Would there be a great price difference whether or not a home is on the waterfront?

![title](images/king_county_1.jpeg)
<br>

This barchart shows that waterfront homes are significantly more expensive than homes not on the waterfront. 

![title](images/king_county_1.jpeg)
<br>

This barchart shows that renovated homes increase the price of a home as you can see by the mean sales price of home renovated vs those that are not renovated.

#### Do prices of homes increase in certain areas of King County?

![title](images/king_county_1.jpeg)
<br>
As we see from the heatmap, home prices increase as you move north in King County. The highest home prices tend to be those neighborhoods near water and closer to the downtown Seattle and Bellevue area. Particularly expensive areas include Medina, Mercer Island, Queen Ann in Seattle and Madison Park in Seattle. 

#### Is there a particular zipcode that tends to sell pricier homes?

This chart shows the mean price of a home in each zipcode. The mean price tends to go up as you get closer to Bellevue, Mercer Island, and Seattle. 

# Preprocessing and More Feature Engineering for Modeling

The above chart is showing a high correlation with sqft_living and multiple other variables. We may need to consider removing qft_above, grade, sqft_living15, and bathrooms.

It looks like we will need to transform the following variables because they are all heavily right positive skewed. We will be normalizing them using a log transformation. 

- price, 
- sqft_living, 
- sqft_living15, 
- sqft_lot, 
- sqft_lot15, 
- sqft_above, 
- age

# Modeling

#### First Simple Model
#### 2nd Model with more than 4 predictors

# Conclusions
**1. The Square footage of your home drives the sale price.**

**2. Insert Text **

**3. Insert Text **

**4. Insert Text **

# Next Steps

Further analyses could provide even more insight into how you will advise your clients to buy or sell thier home. 

**Better idea of neighborhood and surrounding neighborhoods.** We could gather more qualitative data on surrounding neighborhoods such as neighborhood safety, population demographics, and other idicators that may predict the price of a home. You could get an idea of proximity to schools, grocery stores, the city. These may play.

**Better idea of pricing history.** We could look at when the home sold last and for how much. You could then compare the price increases across homes and see the average percentage increase for similer homes.

**Better idea of sale history.** We had a fairly good sample of two years worth of data, but it would be good to gather even more years of sales data in King County further solidify reccomendations. There may be features of the home that are better at predicting sale price now then they were 5 or 10 years ago. 
