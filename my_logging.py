import pathlib
import logging
from datetime import datetime, date


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logfile_name = f'{pathlib.Path(__file__).name}_{date.today()}_{str(datetime.now().time().strftime("%X")).replace(":", ".")}'
handler = logging.FileHandler(f'{logfile_name}.log', mode='w')
formatter = logging.Formatter('%(funcName)s %(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)