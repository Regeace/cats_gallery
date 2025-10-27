import sqlalchemy as db

NO_CONTENT = 204


def form_context(db_filename: str, db_name: str):
    """Создаёт объекты движка работы с базой данных, соединения, содержимого базы данных, задаёт лидирующий счёт"""
    engine = db.create_engine('sqlite:///' + db_filename)
    connection = engine.connect()
    metadata = db.MetaData()

    db_object = db.Table(db_name, metadata, autoload_with=engine)

    query = db.select(db_object.columns)
    result_proxy = connection.execute(query)
    context = result_proxy.fetchall()

    leader_score = max([int(i[2]) for i in context])

    return context, connection, db_object, leader_score


def update_score(database, db_id, connection_object, increment):
    """Запись нового рейтинга в базу данных"""
    update_query = db.update(database).where(database.columns.id == db_id).values(
        score=database.columns.score + increment)
    connection_object.execute(update_query)
    connection_object.commit()


def update_comments(database, db_id, connection_object, comment):
    """Добавление комментария в базу данных"""
    update_query = db.update(database).where(database.columns.id == db_id).values(
        comments=database.columns.comments + comment)
    connection_object.execute(update_query)
    connection_object.commit()