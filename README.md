# Property Data Scraper

This is the codebase for a web crawler that I have built to extract the residential listings available for renting in Singapore.

## Usage
This web crawler can currently extract the following metrics of each listings.

* Property Name
* Property Type
* Address
* Number of Beds
* Nunber of Bathroom
* Rental
* Rental per square feet
* Completion Year
* Total Unit of the Project
* Building Tenure (Freehold or Leasehold)
* Amenities
* Key Details (Rules set by landlord and etc)
* Nearest MRT station and distance

## Prerequisite
* Basic Understanding in [HTML Structure](https://www.w3schools.com/html/)
* [Python](https://amzn.to/2l8jarE)
* Basic Understanding of Shell command

## Installation
This scraper was built using the [scrapy](https://scrapy.org/) framework in Python 3.7. You are required to install scrapy in order to run the scraper.

Pip:
```
pip install Scrapy
```

Conda:
```
conda install -c conda-forge scrapy
```

Otherwise, you can download the [requirement.txt](https://github.com/josephkokchin/SG-Property-Scraper/blob/master/requirements.txt) file and use the following code to install the packages stated.
```
$ while read requirement; do conda install --yes $requirement; done < requirements.txt
```

```
$ while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt
```


## Project Structure
```
.
├── properties_data_2019-07-12T16-19-53.json
├── README.md
├── scrapy.cfg
└── sgpropbot
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── __pycache__
    ├── settings.py
    └── spiders
        ├── __init__.py
        ├── properties.py
        ├── __pycache__
        ├── run.log
        └── scrapy_shell_test_linkextractor.txt
```

## Running the Crawler
In order to run the crawler, please navigate to the ``sgpropbot/spiders`` folder and run the following command:
```
scrapy crawl properties
```
Or
```
scrapy runspider properties.py
```

## Built With
* [scrapy](https://scrapy.org/)
* [datetime](https://docs.python.org/3.7/library/datetime.html)

## Scraped Data Output
The data output was set as JSON file format by default. However, this can be easily changed by amending the `setting.py`. I have provided a sample of data output [here](https://github.com/josephkokchin/SG-Property-Scraper/blob/master/properties_data_2019-07-12T16-19-53.json).

## Next Up
Following up project, I will use the scraped data to:
* Provide a walkthrough on how to export data into database like [MySQL](https://www.mysql.com/) or [PostgreSQL](https://www.postgresql.org/)
* Conduct an exploratory data analysis
* Make an interactive dashboard 
* Building a rental prediction model

## Resources
The most essential part of building a good scraper is to have a good understanding of the website layout so that you are able to extract the right item. The most effective way is through a selector (CSS or XPath) and for specific text extraction, you have to familiar with regex.

#### Cheatsheet
* [Regex]()
* [Xpath]()

#### Books
* [Web Scraping with Python: Collecting More Data from the Modern Web](https://www.amazon.com/gp/product/1491985577/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=josephkokchin-20&creative=9325&linkCode=as2&creativeASIN=1491985577&linkId=63f357e7ae6786d82bcc3620928e484a)
