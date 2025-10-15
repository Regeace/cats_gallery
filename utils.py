import sqlalchemy as db


# engine = db.create_engine('sqlite:///cats.db')
# connection = engine.connect()
# metadata = db.MetaData()
#
# cats = db.Table('cats_db', metadata, autoload_with=engine)
#
# query = db.select(cats.columns)
# resultProxy = connection.execute(query)
# resultSet = resultProxy.fetchall()


def form_contex(db_filename: str, db_name: str):
    engine = db.create_engine('sqlite:///' + db_filename)
    connection = engine.connect()
    metadata = db.MetaData()

    cats = db.Table(db_name, metadata, autoload_with=engine)

    query = db.select(cats.columns)
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()

    return result_set, connection, cats


# data, conn, cats_db = form_contex('cats.db', 'cats_db')

def update_score(database, db_id, connection_object):
    update_query = db.update(database).where(database.columns.id == db_id).values(score=database.columns.score + 1)
    connection_object.execute(update_query)
    connection_object.commit()

# update_score(cats_db, 1)

# print(data, conn, cats_db)
# context = form_contex('cats.db', 'cats_db')
# leader_score = max([int(i[2]) for i in context])
# print(leader_score)

# CATS_DB = {
#     '1': [10, '/cats/1686656313_koshki-13.jpg'],
#     '2': [1, '/cats/1687456031_zhivotnye-9.jpg'],
#     '3': [15, '/cats/1687530058_kotiki-14.jpg'],
#     '4': [15, '/cats/1687254280_zhivotnye-1.jpg'],
#     '5': [1, '/cats/1687530059_kotiki-16.jpg'],
#     '6': [1, '/cats/1689607933_koshki-23.jpg']
# }
