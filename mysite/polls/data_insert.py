def function():
    import pathlib
    import sqlite3
    import pandas as pd
    from . models import New
    from sqlalchemy import create_engine
    from sqlalchemy.types import CHAR , BigInteger , DECIMAL , TEXT
    sql_engine = create_engine("sqlite:///lite.sqlite3")
    DATA_DIR = pathlib.Path().resolve() / "data"
    topics_csv = DATA_DIR / 'ntplog.csv'
    df = pd.read_csv(topics_csv)
    col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay' , 'iserror' ]
    sql_dtypes = {'pc_time':TEXT,'date':TEXT ,'ntpserverip':CHAR , 'stratum':BigInteger , 'pcip':CHAR , 't0':DECIMAL , 't1':DECIMAL , 't2':DECIMAL , 't3':DECIMAL, 'toffset':DECIMAL , 'tdelay':DECIMAL,'iserror':CHAR }
    df.to_sql(name='t' , if_exists='replace' , con=sql_engine , dtype=sql_dtypes)
    sql_connect = sqlite3.connect(r'.\\lite.sqlite3')
    query = "SELECT * FROM t WHERE date > (SELECT date('now', '-2 day'))"
    df1 = pd.read_sql_query(query,sql_connect)
    df2=df1[col].fillna('')
    # def highlight_rows(x):
    #     if x.iserror=='Y':
    #         return['background-color: yellow']*12
    # df2.style.apply(highlight_rows , axis=1)
    new_data = df2[col].to_dict('records')
    qs = New.objects.all()
    if qs.count() !=0:
        qs.delete()
    new_entries = [ ]
    for d in new_data:
        new_obj = New(**d)
        new_entries.append(new_obj)
    New.objects.bulk_create(new_entries)
    
def func():
    import pathlib
    import pandas as pd
    from . models import New
    from sqlalchemy import create_engine
    from sqlalchemy.types import CHAR , BigInteger , DECIMAL , TEXT
    sql_engine = create_engine("sqlite:///lite.sqlite3")
    DATA_DIR = pathlib.Path().resolve() / "data"
    topics_csv = DATA_DIR / 'ntplog.csv'
    df = pd.read_csv(topics_csv)
    col = [ 'pc_time','date','ntpserverip' , 'stratum' , 'pcip' , 't0' , 't1' , 't2' , 't3', 'toffset' , 'tdelay' , 'iserror' ]
    df1=df[col].fillna('')
    new_data = df1[col].to_dict('records')
    qs = New.objects.all()
    if qs.count() !=0:
        qs.delete()
    new_entries = [ ]
    for d in new_data:
        new_obj = New(**d)
        new_entries.append(new_obj)
    New.objects.bulk_create(new_entries)
    
 




 



