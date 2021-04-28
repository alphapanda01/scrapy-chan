# Scrapy-Chan #
- A discord bot to scrape image-boards written in python


# SETUP #
### Deploy to heroku
1. Login into heroku
`  heroku login`
1. Heroku Deployment - Creating a app refer: https://devcenter.heroku.com/articles/git
2. Edit `./bot/config.py` file and add your Discord and Reddit Api

	OR (either do step 3 or step 4 )
1. Set up heroku vars
	
    `heroku config:set API_KEY={YOUR_DISCORD_API}`
    
    `heroku config:set client_id={YOUR_REDDIT_CLIENT_ID}` 
    
    `heroku config:set client_secret={YOUR_CLIENT_SECRET}`
1. add and commit 
	`git commit -a -m "YOUR_COMMIT_MESSAGE_HERE"`
1. Then push the commit to heroku `git push heroku main`

### Run Locally
1. Edit `./bot/config` for api keys
2. install dependencies `pipenv install`
3. Then run the bot `pipenv run python app.py`



## BUGS
- Added ability to scrape gfycat/redgifs but still experimental
- The scraping code is pretty buggy
- Too much overload while scraping reddit or heavy images
