import sqlalchemy as db

NO_CONTENT = 204


def form_contex(db_filename: str, db_name: str):
    engine = db.create_engine('sqlite:///' + db_filename)
    connection = engine.connect()
    metadata = db.MetaData()

    cats = db.Table(db_name, metadata, autoload_with=engine)

    query = db.select(cats.columns)
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()

    return result_set, connection, cats


def update_score(database, db_id, connection_object, increment):
    update_query = db.update(database).where(database.columns.id == db_id).values(
        score=database.columns.score + increment)
    connection_object.execute(update_query)
    connection_object.commit()
