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

def cleanuo_cache():
  for root, dirs, files in os.walk('.'):
    for dir_name in dirs:
      if dir_name == '__pycache__':
        shutil.rmtree(os.path.join(root, dir_name), ignor_errors=True)
        logger.info(f"Removed {os.path.join(root, '__pycache__')}")
    for file in files:
      
