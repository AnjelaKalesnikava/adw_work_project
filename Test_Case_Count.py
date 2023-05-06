import pyodbc
import pytest

cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=EPPLWROW02D8\SQLEXPRESS;"
                      "Database=AdventureWorks2012;"
                      "UID=TestSQL;"
                      "PWD=test123;")

cursor = cnxn.cursor()


@pytest.fixture
def test():
    return 0

@pytest.fixture
def test1():
    return 0

@pytest.fixture
def test2():
    return 0

class Test:
    @pytest.fixture
    def test(self, test):
        return test + 38


    def test_rows_count_um(self, test):
        rows = f"select count(*) from Production.UnitMeasure "
        cursor.execute(rows)
        set1 = cursor.fetchval()
        assert set1 == test


    @pytest.fixture
    def test1(self, test1):
        return test1 + 19614


    def test_rows_count_add(self, test1):
        rows = f"select count(*) from Person.Address "
        cursor.execute(rows)
        set1 = cursor.fetchval()
        assert set1 == test1


    @pytest.fixture
    def test2(self, test2):
        return test2 + 13


    def test_rows_count_doc(self, test2):
        rows = f"select count(*) from Production.Document "
        cursor.execute(rows)
        set1 = cursor.fetchval()
        assert set1 == test2
