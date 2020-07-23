import sqlite3
#建立形态表


#建立单板表
import traceback


def create_table(tablename,db_file):
    try:
        # tablename 需要是单板名字
        con = sqlite3.connect(db_file)
        # con = pymysql.connect(host='localhost', user='root',
        #                       passwd='mgq960830!', charset='utf8')
        cur = con.cursor()

        # cur.execute("create database {tablename};".format(tablename = tablename))

        # cur.execute("use {tablename};".format(tablename = tablename))

        cur.execute("CREATE TABLE IF NOT EXISTS '{tablename}' ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "version varchar(255) NOT NULL,"
                    "algo varchar(255),"
                    "name varchar(255) NOT NULL UNIQUE ,"
                    "algoId varchar(255) NOT NULL,"
                    "subTidN varchar(255) NOT NULL,"
                    "bit varchar(255) NOT NULL,"
                    "numK varchar(255) NOT NULL,"
                    "tidW varchar(255),"
                    "tidN varchar(255),"
                    "subTidW varchar(255),"
                    "sTypeW_bit varchar(255),"
                    "sType varchar(255),"
                    "storeLocation varchar(255),"
                    "ISSU varchar(255),"  # 新加入  好多没有
                    "algoSpe varchar(255),"
                    "testSpe varchar(255),"
                    "castType varchar(255),"
                    "iOrd varchar(255),"
                    "TBLM_ID varchar(255),"
                    "dpt varchar(255),"
                    "dpt_person varchar(255),"
                    "confirmation varchar(255),"
                    "info varchar(255)"
                    ");".format(tablename=tablename))
    except Exception as e:
        raise e
    finally:
        con.close()
def create_log(tablename,db_file):
    try:
        # tablename 需要是单板名字
        con = sqlite3.connect(db_file)
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
    except Exception as e:
        raise e
    finally:
        con.close()
def create_form(formname, db_file):
    try:
        con = sqlite3.connect(db_file)

        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS '{formname}' (tablename varchar(50) UNIQUE NOT NULL)".format(formname=formname))
        # except Exception as e:
        #     raise e
        # finally:
        con.close()
    except Exception as e :
        raise e

def form_store(db_file):
    con = sqlite3.connect(db_file)

    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS form_store (formname varchar(50) UNIQUE NOT NULL)")
    # except Exception as e:
    #     raise e
    # finally:
    con.close()


def rename_table(old, new, db_file):
    try:
        sql = "ALTER TABLE '{old}' RENAME TO '{new}';".format(old = old, new = new)
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute(sql)

        con.close()
    except Exception:
        traceback.print_exc()

def drop_table(name,db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("DROP TABLE '{name}';".format(name = name))
        con.close()
    except Exception:
        traceback.print_exc()

def copy_table(old, new, db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()
        cur.execute("CREATE TABLE '{new}' AS SELECT * FROM '{old}';".format(new = new, old = old))
        con.close()
    except Exception as e:
        traceback.print_exc()
        raise Exception('复制失败')



def delete_tmp(db_file):
    try:
        con = sqlite3.connect(db_file)
        cur = con.cursor()

        lists =  cur.execute("SELECT name FROM sqlite_master where type='table' order by name;")

        lists = list(lists)
        for i in lists:
            i = list(i)
            if 'tmp' in i[0]:
                drop_table(i[0],db_file)
        con.close()
    except Exception:
        traceback.print_exc()

def create_hardware_info(db_file):
    try:
        con = sqlite3.connect(db_file)

        cur = con.cursor()

        cur.execute(


            "CREATE TABLE hardware_info_tmp (name	varchar(255),\
                version	varchar(255),\
                form	varchar(255),\
                algo_core	varchar(255),\
                tcam	varchar(255),\
                algo	varchar(255),\
                algo_engine	varchar(255),\
                multi_core	varchar(255),\
                core_type	varchar(255),\
                cpu_type	varchar(255),\
                makefile	varchar(255),\
                cmake	varchar(255),\
                ko	varchar(255),\
                info	varchar(255)\
            );"
        )
        # except Exception as e:
        #     raise e
        # finally:
        con.close()
    except Exception as e :
        traceback.print_exc()
        raise e
