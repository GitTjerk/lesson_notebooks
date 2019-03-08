import pandas as pd
from sqlalchemy import create_engine


def get_data_from_file(file_type, path):
    if file_type == 'csv':
        return pd.read_csv(path)
    if file_type == 'json':
        return pd.read_json(path)

def get_data_from_db(database, table, user='ironhacker_read', password='ir0nhack3r', host='35.239.232.23'):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    query = f'SELECT * FROM {table}'
    data = pd.read_sql(query, engine)
    return data

def get_data(way, file_type=None, file_path=None, database=None, table=None, user='ironhacker_read',
             password='ir0nhack3r', host='35.239.232.23'):
    if way == 'file':
        return get_data_from_file(file_type, file_path)
    if way == 'database':
        return get_data_from_db(database, table, user, password, host)

def write_on_database(database_name, db_table, dataframe, user='ironhacker_read', password='ir0nhack3r',
                      host='35.239.232.23', index=False):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database_name}')
    dataframe.to_sql(db_table, engine, index, if_exists='append')

def write_in_file(dataframe, title='myFile'):
    dataframe.to_csv(f'{title}.csv')

def write_data(dataframe, way, database_name=None, db_table=None, user='ironhacker_read', password='ir0nhack3r',
               host='35.239.232.23', file_title=None, index=True):
    if way == 'file':
        return write_in_file(dataframe, file_title)
    if way == 'database':
        return write_on_database(database_name, db_table, dataframe, user, password, host, index)