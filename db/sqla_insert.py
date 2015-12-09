from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker
from sqla_define import Word, Tag, WordTag, Base

engine = create_engine('postgres://postgres:postgres@localhost:5432/nostra_db', echo=True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def main():
    # Delete all records
    Table('word_tag', Base.metadata).delete().execute()
    Table('tag', Base.metadata).delete().execute()
    Table('word', Base.metadata).delete().execute()

    word_data = {
        "familiar people": [
            "your mother",
            "your father",
            "your closest friend",
            "a family member"
        ]
    }

    # Call function to insert data
    for tag_name in word_data.keys():
        insert_words(tag_name, word_data[tag_name])


def insert_words(tag_str, words):
    """
    Insert tag, words, and word_tags.
    :param tag_str:
    :param words:
    :return:
    """
    tag = Tag(tag=tag_str)
    session.add(tag)
    session.commit()

    for word_str in words:
        word = Word(word=word_str)
        session.add(word)
        session.commit()
        word_tag = WordTag(word_id=word.id, tag_id=tag.id)
        session.add(word_tag)
        session.commit()


if __name__ == '__main__':
    main()
