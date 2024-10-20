from base import based
from main import cur
from create_model import create_table
class user(based):
    name=based.charfield(max_length=123,default="name")
cur.execute("select * from CodeSubmissions")