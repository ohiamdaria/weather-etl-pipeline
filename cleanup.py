#!/usr/bin/env python3

import os
import shutil #для высокоуровневых операций с файлами/директорией rmtree
import subprocess #для запуска внешних команд psql
import logging #логгирование всех процессов
from pathlib import Path #кроссплатформенное обращение
import argparse #парсинг аргументов командной строки

logging.basicConfig(level=logging.INFO,
                    format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def cleanup_python_cache():
  for root, dirs, files in os.walk('.'):
    for dir_name in dirs:
      if dir_name == '__pycache__':
        shutil.rmtree(os.path.join(root, dir_name), ignore_errors=True)
        logger.info(f"Removed {os.path.join(root, '__pycache__')}")
    for file in files:
      if file.endswith('.рус') or file.endswith('.руо'):
        os.remove(os.path.join(root, file))
        logger.info(f"Removed {os.path.join(root, file)}")

def cleanup_logs():
  log_files = ['weather_etl.log']
  for log_file in log_files:
    if os.path.exists(log_file):
      os.remove(log_file)
      logger.info(f"Removed {log_file}")

def drop_postgrs_db():
  try:
    conn = subprocess.run([
      'psql', '-h', 'localhost', '-p',
      '5432', '-U', 'postgres', '-d', 'postgres', '-c',
      "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = 'weather_db';"
    ],capture_output=True, text=True)
    subprocess.run([
      'psql', '-h', 'localhost', '-p',
      '5432', '-U', 'postgres', '-d', 'postgres', '-c',
      "DROP DATABASE IF EXISTS weather_db;"
      ],capture_output=True, text=True, check=True)
    logger.info("Dropped database weather_db")
    subprocess.run([
      'psql', '-h', 'localhost', '-p',
      '5432', '-U', 'postgres', '-d', 'postgres', '-c',
      "DROP ROLE IF EXISTS postgres;"
      ],capture_output=True, text=True, check=True)
    logger.info("Dropped user postgres")
  except subprocess.CalledProcessError as e:
    logger.warning(f"Postgres cleanup partial fail: {e}")

def cleanup_temp_files():
  temp_patterns = ['*.tmp', '*.temp', 'temp/', 'tmp/']
  for pattern in temp_patterns:
    for file in Path('.').glob(pattern):
      if file.is_file():
        file.unlink()
        logger.info(f"Removed temp file: {file}")
      else:
        shutil.rmtree(file, ignore_errors=True)
        logger.info(f"Removed temp dir: {file}")

def main(dry_run=False):
  logger.info("Starting ETL cleanup...")
  if dry_run:
    logger.info("DRY RUN MODE - nothing will be deleted")
    return
  
  cleanup_python_cache()
  cleanup_logs()
  cleanup_temp_files()
  drop_postgrs_db()

  logger.info("Cleanup COMLETED")

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="ETL Cleanup Script")
  parser.add_argument('--dry-run', action='store_true', help="Show what would be deleted")
  args = parser.parse_args()

  main(dry_run=args.dry_run)





