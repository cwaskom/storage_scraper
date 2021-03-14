import os
from api.app import create_app
from api.scraper import run_scraper

if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    # run app
    app.run(debug = True)
    # run scraper
    scraped_data = run_scrape()
    print(scraped_data)
