# Twitter Scraping

The code in this repository is used to scrape twitter for location-related tweets in NewYork city. 
- The library **Twint** was used to scrape the tweets
- The scraper used keywords like I'm at, checked in, went to, or visited to find location-related tweets only due to the space limitations
- The data lies in between 500km radius of the cordinates[41.660769,-73.931236] 
- The tweets dates were throughout the year 2018
- The results of the scraper were then uploaded to a MongoDB cluster
