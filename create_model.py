from main import cur
from main import con
import inspect
def is_static_method_of_class(name, cls, method_name):
    method = cls.__dict__.get(method_name, None)
    if isinstance(method, staticmethod) and method.__func__ is name:
        return True
    return False
def create_table(class_name):
    tablename = class_name.__name__
    fields = [(var, getattr(class_name, var)) for var in class_name.__dict__ if not var.startswith('__')]
    field_definitions = []
    
    for var, attributes in fields:
        if isinstance(attributes, dict) and "type" in attributes:
            sql_type = attributes["type"]
            field_definitions.append(f"{var} {sql_type}")
    all_fields = ", ".join(field_definitions)
    print(tablename)
    create_table_sql = f"CREATE TABLE {tablename} ({all_fields})"
    cur.execute(create_table_sql)
    print(cur.execute("SELECT * FROM name;").fetchall())
    