
import sqlite3
import traceback


def insert_db(tablename, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation):


    if algo == '' or algo.isspace():

        algo = 'N/A'


    if name == '' or name.isspace():

        name = 'N/A'

    if algoId == '' or algoId.isspace():
        algoId = 'N/A'

    if subTidN == '' or subTidN.isspace():
        subTidN = 'N/A'
    if bit == '' or bit.isspace():
        bit = 'N/A'
    if numK == '' or numK.isspace():
        numK = 'N/A'

    if tidW == '' or tidW.isspace():
        tidW = 'N/A'

    if tidN == '' or tidN.isspace():
        tidN = 'N/A'

    if subTidW == '' or subTidW.isspace():
        subTidW = 'N/A'

    if sTypeW_bit == '' or sTypeW_bit.isspace():
        sTypeW_bit = 'N/A'

    if  sType == '' or sType.isspace():
        sType = 'N/A'

    if storeLocation == '' or storeLocation.isspace():
        storeLocation = 'N/A'

    if ISSU == '' or ISSU.isspace():
        ISSU = 'N/A'

    if algoSpe == '' or algoSpe.isspace():
        algoSpe = 'N/A'

    if testSpe == '' or testSpe.isspace():
        testSpe = 'N/A'

    if castType == '' or castType.isspace():
        castType = 'N/A'

    if iOrd == '' or iOrd.isspace():
        iOrd = 'N/A'

    if TBLM_ID == '' or TBLM_ID.isspace():
        TBLM_ID = 'N/A'

    if dpt == '' or dpt.isspace():
        dpt = 'N/A'

    if dpt_person == '' or dpt_person.isspace():
        dpt_person = 'N/A'

    if confirmation == '' or confirmation.isspace():
        confirmation = 'N/A'

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
        for i in sql_store:
            print(i)
            cur_insert.execute(i)
        db.commit()
    except Exception as e:
        # db.rollback()
        print('rollback')
        traceback.print_exc()
        raise Exception
    finally:
        db.close()


