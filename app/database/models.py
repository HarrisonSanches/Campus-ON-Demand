from enum import unique
from functools import partial
from peewee import *
import peewee as pw
from database.connection_db import create_connection_db

db = create_connection_db('orchestrator_database', 'root', 'root', '127.0.0.1', 3306)

class BaseModel(Model):
    class Meta:
        database = db

class Services(BaseModel):
    idservice = AutoField(primary_key=True)
    name = CharField(max_length=100)
    token = CharField(max_length=100)
    creation_date = DateField()
    
    class Meta:
        table_name = 'service'
    
        

class Group(BaseModel):
    idgroup = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=100, unique=True)
    creation_date = DateField(formats=None)
    
    class Meta:
        table_name = 'Group'


class User(BaseModel):
    iduser = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=100)
    username = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)
    creation_date = DateField(formats=None)
    fk_service = ForeignKeyField(Services, to_field='idservice')
    token_OSM = CharField()
    fk_group = ForeignKeyField(Group, to_field='idgroup')
    
    class Meta:
        table_name = 'User'

    
class Project(BaseModel):
    idproject = CharField(max_length=100, primary_key=True)
    name = CharField(max_length=100, unique=True)
    creation_date = DateField()
    fk_user = ForeignKeyField(User, to_field='iduser')
    id_openstack = CharField(max_length=100, unique=True)
    id_OSM = CharField(max_length=100, unique=True)
    
    class Meta:
        table_name = 'project'