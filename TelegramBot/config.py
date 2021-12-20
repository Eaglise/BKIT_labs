from enum import Enum
token = '5043304347:AAEdx8whgQruduOmDPCNIlPZNGFA3j02J5g'
weather_api = {'key': '2ba80993017dfb2cff22275885728205'}
# Файл базы данных Vedis
db_file = "db.vdb"
# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"
# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_SITE = "STATE_SITE"
    STATE_TAG = "STATE_TAG"
    STATE_CITY = "STATE_CITY"