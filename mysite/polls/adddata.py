import pathlib
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import CHAR , BigInteger , DECIMAL , TEXT
sql_engine = create_engine("sqlite:///lite.sqlite3")
DATA_DIR = pathlib.Path().resolve() / "data"
topics_csv = DATA_DIR / 'ntplog.csv'
df = pd.read_csv(topics_csv)
col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay']
sql_dtypes = {'pc_time':TEXT,'date':TEXT ,'ntpserverip':CHAR , 'stratum':BigInteger , 'pcip':CHAR , 't0':DECIMAL , 't1':DECIMAL , 't2':DECIMAL , 't3':DECIMAL, 'toffset':DECIMAL , 'tdelay':DECIMAL,}
df.to_sql(name='t' , if_exists='replace' , con=sql_engine , dtype=sql_dtypes)
# can only be changed from the main django file as it is only a copy of that file....
