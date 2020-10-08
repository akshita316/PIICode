import pathlib
from configparser import ConfigParser as _ConfigParser
import json

_cfg = _ConfigParser()
_path = pathlib.Path("config/config.ini")
_cfg.read(_path)
location_of_csv = str(_cfg.get('fileConfig', 'fileToRead'))
destination_folder = str(_cfg.get('fileConfig', 'destinationFolder'))
columns = json.loads(str(_cfg.get('fileConfig', 'columns')))
sheetToEliminate = json.loads(str(_cfg.get('fileConfig', 'sheetToEliminate')))
