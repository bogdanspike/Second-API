from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


Base = declarative_base()

engine = create_engine('mysql+pymysql://root:@localhost/api_schema?charset=utf8mb4')

Session = sessionmaker(bind=engine)
session = Session()


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    filename = Column(String, nullable=False)
    file_text = Column(String, nullable=False)

    def __repr__(self):
        return "<Files(filename='%s', file_text='%s')>" % \
               (self.filename, self.file_text)
