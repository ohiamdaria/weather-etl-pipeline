import logging 
import psycopg2
from psycopg2 import sql
from config import PG_CONFIG

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  handlers=[
    logging.FileHandler('weather_etl.log'),
    logging.StreamHandler()
  ]
)

logger = logging.getLogger(__name__)

def get_connection(dbname=None):
  conn_params = PG_CONFIG.copy()

  if dbname:
    conn_params['dbname'] = dbname

  try:
    conn = psycopg2.connect(**conn_params)
    conn.autocommint = True
    logger.info(f"Connected to{dbname or 'postgres'}")
    return conn
  except psycopg2.OperationalError as e:
    logger.error(f"Connected failed: {e}")
    raise

def check_postgres():
  with get_connection('postres') as conn:
    cur = conn.cursor()
    cur.execute("SELECT version()")
    version = cur.fetchone()
    logger.info(f"PostgreSQL version: {version[0]}")