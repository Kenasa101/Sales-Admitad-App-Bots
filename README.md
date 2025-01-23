# Sales-Admitad-App-Bots

- Django
- aiogram
- asyncio
- requests
- PIL
- pandas
- os
- re
- subprocess
- psycopg2
- time
- io 
- openpyxl


                             This project consists of the following services:
1. Automatic parsing of coupons, promotional codes, products from more than 200 stores, adding to the Postgres database. Parsing occurs via API from the Admitad website with a certain time interval
2. A Django website containing coupons, promotional codes, products, integrated into two Telegram bots, which have two Telegram Mini-Apps built into them.
    - Using indexes due to the large number of rows (more than 5 million) in the database.
    - Using complex Django ORM queries
    - Using full-text search by product names (to_tsvector)
    - Own implementation of page pagination
    - Using debug toolbar to track database queries
    - HTML templates + JS, CSS
    - Using Telegram Mini-App
    - Using Yandex Metrica to keep statistics
3. Telegram bot (Telegram Mini-App) for coupons and promo codes https://t.me/coupons186_bot
4. Telegram bot (Telegram Mini-App) in the form of a product catalog https://t.me/products186_bot
5. Automatic publication of posts to a telegram channel. The publication is fully customizable. You can change the interval between posts, the allowed time of day for publications, use silent mode when sending, instant sending of a promo code or product, etc.
6. Telegram bot for managing automatic publication for admins
