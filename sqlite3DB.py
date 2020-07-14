import sqlite3
#建立形态表


#建立单板表
import traceback


def create_table(tablename):
    # try:
    # tablename 需要是单板名字
    con = sqlite3.connect('test2.db')
    # con = pymysql.connect(host='localhost', user='root',
    #                       passwd='mgq960830!', charset='utf8')
    cur = con.cursor()

    # cur.execute("create database {tablename};".format(tablename = tablename))

    # cur.execute("use {tablename};".format(tablename = tablename))

    cur.execute("CREATE TABLE IF NOT EXISTS '{tablename}' ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "algo varchar(50),"
                "name varchar(50) NOT NULL UNIQUE ,"
                "algoId varchar(20) NOT NULL,"
                "subTidN varchar(20) NOT NULL,"
                "bit varchar(20) NOT NULL,"
                "numK varchar(20) NOT NULL,"
                "tidW varchar(20),"
                "tidN varchar(20),"
                "subTidW varchar(20),"
                
                "sTypeW_bit varchar(50),"
                "sType varchar(20),"
                "storeLocation varchar(50),"
                
                "ISSU varchar(20),"  # 新加入  好多没有
                "algoSpe varchar(20),"
                "testSpe varchar(20),"
                "castType varchar(20),"
                "iOrd varchar(20),"
                "TBLM_ID varchar(50),"
                "dpt varchar(20),"
                "dpt_person varchar(50),"
                "confirmation varchar(50)"
                ");".format(tablename=tablename))
    # except Exception as e:
    #     raise e
    # finally:
    con.close()
def create_log(tablename):
    # try:
    # tablename 需要是单板名字
    con = sqlite3.connect('test2.db')
    # con = pymysql.connect(host='localhost', user='root',
    #                       passwd='mgq960830!', charset='utf8')
    cur = con.cursor()

    # cur.execute("create database {tablename};".format(tablename = tablename))

    # cur.execute("use {tablename};".format(tablename = tablename))

    cur.execute("CREATE TABLE IF NOT EXISTS '{tablename}_logs' ("
                
                "date varchar(50),"
                "ver varchar(50),"
                "intro varchar(255),"
                "decision varchar(255),"
                "content varchar(255),"
                "reviser varchar(255))"
                .format(tablename=tablename))
    # except Exception as e:
    #     raise e
    # finally:
    con.close()
def create_form(formname):
    try:
        con = sqlite3.connect('test2.db')

        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS '{formname}' (tablename varchar(50) UNIQUE NOT NULL)".format(formname=formname))
        # except Exception as e:
        #     raise e
        # finally:
        con.close()
    except Exception as e :
        raise e

def form_store():
    con = sqlite3.connect('test2.db')

    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS form_store (formname varchar(50) UNIQUE NOT NULL)")
    # except Exception as e:
    #     raise e
    # finally:
    con.close()


def rename_table(old, new):
    try:
        sql = "ALTER TABLE '{old}' RENAME TO '{new}';".format(old = old, new = new)
        con = sqlite3.connect('test2.db')
        cur = con.cursor()
        cur.execute(sql)

        con.close()
    except Exception:
        traceback.print_exc()

def drop_table(name):
    try:
        con = sqlite3.connect('test2.db')
        cur = con.cursor()
        cur.execute("DROP TABLE '{name}';".format(name = name))
        con.close()
    except Exception:
        traceback.print_exc()

def delete_tmp():
    try:
        con = sqlite3.connect('test2.db')
        cur = con.cursor()

        lists =  cur.execute("SELECT name FROM sqlite_master where type='table' order by name;")

        lists = list(lists)
        for i in lists:
            i = list(i)
            if 'tmp' in i[0]:
                drop_table(i[0])
        con.close()
    except Exception:
        traceback.print_exc()