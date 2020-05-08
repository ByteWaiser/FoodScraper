# A Recipe Scraper Script

At first I was going to scrape Yemek.com with requests.
But when I analyzed the network I saw their API requests which did not require any auth.
So this actually uses their API and cleans a little bit to get what I want.
Lastly I added all the data to my local mongodb database.
Which has scraped 7948 food recipes.
(I do not know if it is legal...)

# Usage

I did not upload for the public use but
If you want just install requests and pymongo libraries and run.