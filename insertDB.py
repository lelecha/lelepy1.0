
import sqlite3
import traceback


def insert_db(tablename, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation):

    try:
        if algo == '' or algo.isspace() or algo == 'None':
            raise Exception('算法名不可为空')
            algo = 'N/A'


        if name == '' or name.isspace() or name == 'None':
            print("名字为空")
            raise Exception('业务名不可为空')
            name = 'N/A'

        if algoId == '' or algoId.isspace() or algoId == 'None':
            raise Exception('算法表ID不可为空')
            algoId = 'N/A'

        if subTidN == '' or subTidN.isspace() or subTidN == 'None':
            raise Exception('SubTid不可为空')
            subTidN = 'N/A'
        if bit == '' or bit.isspace() or bit == 'None':
            raise Exception('位宽不可为空')
            bit = 'N/A'
        if numK == '' or numK.isspace() or numK == 'None' :
            raise Exception('条数不可为空')
            numK = 'N/A'

        if tidW == '' or tidW.isspace():
            tidW = 'None'

        if tidN == '' or tidN.isspace():
            tidN = 'None'

        if subTidW == '' or subTidW.isspace():
            subTidW = 'None'

        if sTypeW_bit == '' or sTypeW_bit.isspace():
            sTypeW_bit = 'None'

        if  sType == '' or sType.isspace():
            sType = 'None'

        if storeLocation == '' or storeLocation.isspace():
            storeLocation = 'None'

        if ISSU == '' or ISSU.isspace():
            ISSU = 'None'

        if algoSpe == '' or algoSpe.isspace():
            algoSpe = 'None'

        if testSpe == '' or testSpe.isspace():
            testSpe = 'None'

        if castType == '' or castType.isspace():
            castType = 'None'

        if iOrd == '' or iOrd.isspace():
            iOrd = 'None'

        if TBLM_ID == '' or TBLM_ID.isspace():
            TBLM_ID = 'None'

        if dpt == '' or dpt.isspace():
            dpt = 'None'

        if dpt_person == '' or dpt_person.isspace():
            dpt_person = 'None'

        if confirmation == '' or confirmation.isspace():
            confirmation = 'None'

        sql_insert = "insert into '{tablename}' (id, algo, name, bit, numK, tidW, tidN, subTidW, subTidN, sTypeW_bit, sType, " \
                     "storeLocation, algoId,ISSU,algoSpe, testSpe, " \
                     "castType, iOrd, TBLM_ID, dpt, dpt_person, confirmation) " \
                     "values ( NULL,'{algo}','{name}', '{bit}', '{numK}', '{tidW}', '{tidN}', '{subTidW}', " \
                     "'{subTidN}', '{sTypeW_bit}', '{sType}', '{storeLocation}', '{algoId}','{ISSU}','{algoSpe}','{testSpe}', " \
                     "'{castType}', '{iOrd}', '{TBLM_ID}', '{dpt}', '{dpt_person}', '{confirmation}');".format(tablename=tablename,
                                                                                                               algo=algo,
                                                                                                               name=name,
                                                                                                               bit=bit,
                                                                                                               numK=numK
                                                                                                               , tidW=tidW,
                                                                                                               tidN=tidN,
                                                                                                               subTidW=subTidW,
                                                                                                               subTidN=subTidN,
                                                                                                               sTypeW_bit=sTypeW_bit,
                                                                                                               sType=sType,
                                                                                                               storeLocation=storeLocation,
                                                                                                               algoId=algoId,
                                                                                                               ISSU = ISSU,
                                                                                                               algoSpe=algoSpe,
                                                                                                               testSpe=testSpe,
                                                                                                               castType=castType,
                                                                                                               iOrd=iOrd,
                                                                                                               TBLM_ID=TBLM_ID,
                                                                                                               dpt=dpt,
                                                                                                               dpt_person=dpt_person,
                                                                                                               confirmation=confirmation)


        return sql_insert

    except Exception as e:
        raise e

#向形态表仓库插入一个形态表
def insert_form(formname):
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        cur_insert.execute("INSERT INTO form_store (formname) values ('{formname}')".format(formname = formname))
        db.commit()
        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('创建形态表出错')
        raise e
    finally:
        db.close()

#向一个形态表插入一张单板
def insert_hardware(formname, tablename):
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        cur_insert.execute("INSERT INTO '{formname}' (tablename) values ('{tablename}')".format(formname = formname, tablename = tablename))
        db.commit()
        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('创建形态表出错')
        raise e
    finally:
        db.close()



def insert_logs(tablename, date, ver, intro, decision, content, reviser):

    if date == '' or date.isspace():

        date = 'N/A'


    if ver == '' or ver.isspace():

        ver = 'N/A'

    if intro == '' or intro.isspace():
        intro = 'N/A'

    if decision == '' or decision.isspace():
        decision = 'N/A'
    if content == ''or content.isspace():
        content = 'N/A'
    if reviser == '' or reviser.isspace():
        reviser = 'N/A'


    sql_insert_logs = "insert into '{tablename}_logs'(date, ver, intro, decision, content, reviser) values ('{date}'," \
                      "'{ver}','{intro}','{decision}','{content}','{reviser}')".format(tablename = tablename,
                                                                                       date = date,
                                                                                       ver = ver,
                                                                                       intro = intro,
                                                                                       decision = decision,
                                                                                       content = content,
                                                                                       reviser = reviser
                                                                                       )
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        cur_insert.execute(sql_insert_logs)
        db.commit()


        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()


def excecute_sql(sql_store):
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        for i in range(len(sql_store)):
            print(i)
            cur_insert.execute(sql_store[i])
        db.commit()
    except Exception as e:
        # db.rollback()
        print('rollback')
        traceback.print_exc()
        raise e
    finally:
        db.close()


