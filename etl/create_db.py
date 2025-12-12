import logging
import psycopg2
from connect_pg import get_connection

logging.basicCongig(
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  handlers=[
    logging.FileHandler('weather_etl.log'),
    logging.StreamHandler()
  ]
)

logger = logging.getLogger(__name__)

def create_database_and_tables():
  with get_connection('weather_db') as conn:
    cur = conn.cursor()
    logger.info('Check exists weather_db')
    cur.execute("SELECT 1 FROM pg_database WHERE datname = 'weather_db")
    result = cur.fetchone()