import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey, MetaData
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def connect():
    DATABASE_URI = 'postgres+psycopg2://postgres:3791215233745@127.0.0.1:5432/Train'
    engine = create_engine(DATABASE_URI)
    metadata = MetaData(bind=engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    return s


class Train(Base):
    __tablename__ = 'train'
    id = Column(Integer, primary_key=True)
    number_of_cars = Column(Integer)
    year_in_which_it_was_made = Column(Integer)

    def __init__(self, id, number_of_cars, year_in_which_it_was_made):
        self.id = id
        self.number_of_cars = number_of_cars
        self.year_in_which_it_was_made = year_in_which_it_was_made

    def __repr__(self):
        return "<Train(id='{}', number_of_cars='{}', year_in_which_it_was_made={})>\n" \
            .format(self.id, self.number_of_cars, self.year_in_which_it_was_made)


class Route(Base):
    __tablename__ = 'route'
    number = Column(Integer, primary_key=True)
    ending_station = Column(String)

    def __init__(self, number, ending_station):
        self.number = number
        self.ending_station = ending_station

    def __repr__(self):
        return "<Route(number='{}', ending_station='{}')>\n" \
            .format(self.number, self.ending_station)


class Passenger(Base):
    __tablename__ = 'passenger'
    pid = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

    def __repr__(self):
        return "<Passenger(pid='{}', name='{}')>\n" \
            .format(self.pid, self.name)


train_passenger_association = Table('train_passenger', Base.metadata,
    Column('train_id', Integer, ForeignKey('train.id'), primary_key=True),
    Column('passenger_id', Integer, ForeignKey('passenger.pid'), primary_key=True)
)


train_route_association = Table('train_route', Base.metadata,
    Column('route_number', Integer, ForeignKey('route.number'), primary_key=True),
    Column('train_id', Integer, ForeignKey('train.id'), primary_key=True)
)


def add_elem(count, param_1, param_2, param_3):
    s = connect()
    try:
        if count == 0:
            obj = Train(param_1, param_2, param_3)
            s.add(obj)
            s.commit()
        elif count == 1:
            obj = Route(param_1, param_2)
            s.add(obj)
            s.commit()
        elif count == 2:
            obj = Passenger(param_1, param_2)
            s.add(obj)
            s.commit()

    except (sqlalchemy.exc.IntegrityError, sqlalchemy.exc.InvalidRequestError):
        print("This primary key already exists")
    else:
        print("You update element at database!")
    finally:
        s.close()


def update_elem(count, param_1, param_2, param_3, param_4):
    # param_4 - it's id_prev
    s = connect()
    try:
        if count == 0:
            s.query(Train).filter(Train.id == param_4).update({Train.id: param_1, Train.number_of_cars: param_2,
                                                               Train.year_in_which_it_was_made: param_3})
            s.commit()

        elif count == 1:
            s.query(Route).filter(Route.number == param_4).update({Route.number: param_1, Route.ending_station: param_2})
            s.commit()
        elif count == 2:
            s.query(Passenger).filter(Passenger.pid == param_4).update({Passenger.pid: param_1, Passenger.name: param_2})
            s.commit()
    except sqlalchemy.exc.IntegrityError:
        print("This primary key already exists")
    else:
        print("You update element at database!")
    finally:
        s.commit()
        s.close()


def delete_elem(count, param_1):
    s = connect()
    try:
        if count == 0:
            del_obj = s.query(Train).filter_by(id=param_1).one()
            s.delete(del_obj)
        elif count == 1:
            del_obj = s.query(Route).filter_by(number=param_1).one()
            s.delete(del_obj)
        elif count == 2:
            del_obj = s.query(Passenger).filter_by(pid=param_1).one()
            s.delete(del_obj)
    except sqlalchemy.orm.exc.NoResultFound:
        print("A database result was required but none was found.")
    else:
        print("You update element at database!")
    finally:
        s.commit()
        s.close()


def print_table(count):
    s = connect()
    try:
        if count == 1:
            print(s.query(Train).all())
        elif count == 2:
            print(s.query(Route).all())
        elif count == 3:
            print(s.query(Passenger).all())
    except:
        print("You enter wrong data! Database does not have element whit this primary key")
    finally:
        s.commit()
        s.close()
