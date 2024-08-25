from facades.db_processing_facade import DB_processor
from datetime import datetime, timedelta

if __name__ == "__main__":
    db_processor = DB_processor()
    db_processor.populate_wallets()
    db_processor.populate_categories()
    end_date = datetime.now()
    start_date = end_date - timedelta(days=3)
    db_processor.populate_transactions(start_date.strftime(
        '%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
