# NPRG045

This repository is for the course [NPRG045](https://is.cuni.cz/studium/predmety/index.php?id=8e2d2990881a77e48ecb713cc035bd4b&tid=&do=predmet&kod=NPRG045&skr=2023&fak=11320) at [MFF UK](https://www.mff.cuni.cz).

## News Sentiment Analysis (Web) Application
The final version of the application will be available for the course [NSZZ031](https://is.cuni.cz/studium/predmety/index.php?id=8e2d2990881a77e48ecb713cc035bd4b&tid=&do=predmet&kod=NSZZ031&skr=2023).

You can try it out in deployment without the backend part (due to the local Neo4j database):
- In repository ``App/frontend/news-sentiment-app`` run ``ng serve``
- Then navigate to the ``http://localhost:4200/``

The beginning of the thesis, the textual part of this work, is available [here](better-thesis-master/version/thesis-v1-fixed-typos.pdf) 

![teaser1](images/teaser01.png)
![teaser2](images/teaser02.png)
![teaser3](images/teaser03.png)
![teaser4](images/teaser04.png)

## Textual Data Sources [1/3]
**FORBES** - [10 Journalism Brands Where You Will Find Real Facts Rather Than Alternative Facts](https://www.forbes.com/sites/berlinschoolofcreativeleadership/2017/02/01/10-journalism-brands-where-you-will-find-real-facts-rather-than-alternative-facts/)

### The Guardian ✅
- The Guardian API is free and available for everyone.

### The New York Times ❌
- Access to the full text of the articles is unavailable, but basic metadata is available.
- (viz. email communication with the NYT)
- Note: The NYT API is not entirely free accessible.

### Financial Times ❌
- Access to the whole API is unavailable.
- (viz. email communication with the FT)
- Note: "There is an unavailability to manage the volume of requests they receive from the students and faculty for access to the API."

### Bloomberg ❌
- Bloomberg API is not free (TOO EXPENSIVE)

### Reuters ❌
- Reuters API is not free (TOO EXPENSIVE)

### Nasdaq Data Link ❌
- Quandl API is not free (TOO EXPENSIVE)
- Note: It is hard to find pricing information, viz. https://help.data.nasdaq.com/article/132-how-much-does-quandl-data-cost

### BBC News ❔
- https://www.bbc.co.uk/developer/technology/apis.html

### Without information about the API
- Only way to get the data is to scrape the website.
- The Washington Post
- The Wall Street Journal


## Tickers Data Sources [1/1]
### Yahoo Finance ✅
### Nasdaq Data Link ❔