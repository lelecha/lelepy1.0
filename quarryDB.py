
import sqlite3
import traceback





def get_head_name(tablename,db_file):
    db = sqlite3.connect(db_file)
    cur = db.cursor()
    cur.execute("SELECT * FROM '{tablename}'".format(tablename=tablename))
    sqlFields = cur.description
    num = len(sqlFields)
    fields = [None] * num
    print(num)
    for i in range(num):
        print(sqlFields[i][0])
        print(i)
        fields[i] = sqlFields[i][0]
    db.close()
    return fields



def quarry_all(tablename,db_file):
    sql_quarry = "select * from '{tablename}' order by cast(algoId AS INT), cast(subTidN AS INT);".format(tablename=tablename)
    try:
        db = sqlite3.connect(db_file)
        # db = connectDB.connect_db('localhost', 'root', 'mgq960830!', '5885ce76mb')
        cur = db.cursor()
        cur.execute(sql_quarry)
        # headName = quarry_field_name(cur)
        results = cur.fetchall()
        # results.insert(0, headName)
        print(results)
        # for row in results:
        #     id = row[0]
        #     user_id = row[1]
        #     name = row[2]
        #     print(id, name, user_id)
        return results
    except Exception as e:
        raise e
    finally:
        db.close()


def quarry_form(formname,db_file):
    sql_quarry = "select * from '{formname}';".format(formname = formname)
    try:
        db = sqlite3.connect(db_file)
        cur = db.cursor()
        cur.execute(sql_quarry)
        results = cur.fetchall()
        print(results)
        return results
    except Exception as e:
        raise e
    finally:
        db.close()

def quarry_form_store(db_file):
    sql_quarry = "select * from form_store;"
    try:
        db = sqlite3.connect(db_file)
        cur = db.cursor()
        cur.execute(sql_quarry)
        results = cur.fetchall()
        print(results)
        return results
    except Exception as e:
        raise e
    finally:
        db.close()


def quarry_search(tablename, version ,algo, name, algoId, subTidN, bit, numK
                  , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU, algoSpe,
                  testSpe, castType, iOrd,
                  TBLM_ID, dpt, dpt_person, confirmation, info,db_file):
    list = [None] * 23

    if algo == 'None' or algo == '':
        list[0] = "'1'"
        algo = '1'
    else:
        list[0] = 'algo'

    if info == 'None' or info == '':
        list[22] = "'1'"
        info = '1'
    else:
        list[22] = 'info'

    if version == 'None' or version == '':
        list[1] = "'1'"
        version = '1'
    else:
        list[1] = 'version'

    if name == 'None' or name == '':
        list[2] = "'1'"
        name = '1'
    else:
        list[2] = 'name'

    if algoId == 'None' or algoId == '':
        list[3] = "'1'"
        algoId = '1'
    else:
        list[3] = 'algoId'

    if numK == 'None' or numK == '':
        list[6] = "'1'"
        numK = '1'
    else:
        list[6] = 'numK'

    if tidW == 'None' or tidW == '':
        list[7] = "'1'"
        tidW = '1'
    else:
        list[7] = 'tidW'

    if tidN == 'None' or tidN == '':
        list[8] = "'1'"
        tidN = '1'
    else:
        list[8] = 'tidN'

    if subTidW == 'None' or subTidW == '':
        list[9] = "'1'"
        subTidW = '1'
    else:
        list[9] = 'subTidW'

    if subTidN == 'None' or subTidN == '':
        list[4] = "'1'"
        subTidN = '1'
    else:
        list[4] = 'subTidN'

    if sTypeW_bit == 'None' or sTypeW_bit == '':
        list[10] = "'1'"
        sTypeW_bit = '1'
    else:
        list[10] = 'sTypeW_bit'

    if sType == 'None' or sType == '':
        list[11] = "'1'"
        sType = '1'
    else:
        list[11] = 'sType'

    if storeLocation == 'None' or storeLocation == '':
        list[12] = "'1'"
        storeLocation = '1'
    else:
        list[12] = 'storeLocation'

    if bit == 'None' or bit == '':
        list[5] = "'1'"
        bit = '1'
    else:
        list[5] = 'bit'

    if ISSU == 'None' or ISSU == '':
        list[13] = "'1'"
        ISSU = '1'
    else:
        list[13] = 'ISSU'


    if algoSpe == 'None' or algoSpe == '':
        list[14] = "'1'"
        algoSpe = '1'
    else:
        list[14] = 'algoSpe'

    if testSpe == 'None' or testSpe == '':
        list[15] = "'1'"
        testSpe = '1'
    else:
        list[15] = 'testSpe'

    if castType == 'None' or castType == '':
        list[16] = "'1'"
        castType = '1'
    else:
        list[16] = 'castType'

    if iOrd == 'None' or iOrd == '':
        list[17] = "'1'"
        iOrd = '1'
    else:
        list[17] = 'iOrd'

    if TBLM_ID == 'None' or TBLM_ID == '':
        list[18] = "'1'"
        TBLM_ID = '1'
    else:
        list[18] = 'TBLM_ID'

    if dpt == 'None' or dpt == '':
        list[19] = "'1'"
        dpt = '1'
    else:
        list[19] = 'dpt'

    if dpt_person == 'None' or dpt_person == '':
        list[20] = "'1'"
        dpt_person = '1'
    else:
        list[20] = 'dpt_person'

    if confirmation == 'None' or confirmation == '':
        list[21] = "'1'"
        confirmation = '1'
    else:
        list[21] = 'confirmation'


    sql_search = "select * from '{tablename}' where {algo} = '{algo_}' and {version} = '{version_}' and {name} = '{name_}' and {algoId} = '{algoId_}' and {subTidN} = '{subTidN_}' and {bit} = '{bit_}'" \
                 " and {numK} = '{numK_}' and {tidW} = '{tidW_}' and {tidN} = '{tidN_}' and {subTidW} = '{subTidW_}'" \
                 " and {sTypeW_bit} = '{sTypeW_bit_}' and {sType} = '{sType_}' and {storeLocation} = '{storeLocation_}'" \
                 " and {ISSU} = '{ISSU_}' and {algoSpe} = '{algoSpe_}' and {testSpe} = '{testSpe_}'" \
                 " and {castType} = '{castType_}' and {iOrd} = '{iOrd_}' and {TBLM_ID} = '{TBLM_ID_}' and {dpt} = '{dpt_}'" \
                 " and {dpt_person} = '{dpt_person_}' and {confirmation} = '{confirmation_}' and {info} = '{info_}' order by cast(algoId AS INT), cast(subTidN AS INT)".format(tablename=tablename,
                                                                                                 algo=list[0],
                                                                                                 algo_=algo,
                                                                                                 version = list[1],
                                                                                                 version_ = version,
                                                                                                 name=list[2],
                                                                                                 name_=name,
                                                                                                 bit=list[5],
                                                                                                 bit_=bit,
                                                                                                 numK=list[6],
                                                                                                 numK_=numK,
                                                                                                 tidW=list[7],
                                                                                                 tidW_=tidW,
                                                                                                 tidN=list[8],
                                                                                                 tidN_=tidN,
                                                                                                 subTidW=list[9],
                                                                                                 subTidW_=subTidW,
                                                                                                 subTidN=list[4],
                                                                                                 subTidN_=subTidN,
                                                                                                 sTypeW_bit=list[10],
                                                                                                 sTypeW_bit_=sTypeW_bit,
                                                                                                 sType=list[11],
                                                                                                 sType_=sType,
                                                                                                 storeLocation=list[12],
                                                                                                 storeLocation_=storeLocation,
                                                                                                 algoId=list[3],
                                                                                                 algoId_=algoId,
                                                                                                 ISSU=list[13],
                                                                                                 ISSU_=ISSU,
                                                                                                 algoSpe=list[14],
                                                                                                 algoSpe_=algoSpe,
                                                                                                 testSpe=list[15],
                                                                                                 testSpe_=testSpe,
                                                                                                 castType=list[16],
                                                                                                 castType_=castType,
                                                                                                 iOrd=list[17],
                                                                                                 iOrd_=iOrd,
                                                                                                 TBLM_ID=list[18],
                                                                                                 TBLM_ID_=TBLM_ID,
                                                                                                 dpt=list[19],
                                                                                                 dpt_=dpt,
                                                                                                 dpt_person=list[20],
                                                                                                 dpt_person_=dpt_person,
                                                                                                 confirmation=list[21],
                                                                                                 confirmation_=confirmation,
                                                                                                 info = list[22],
                                                                                                 info_ = info
                                                                                                 )
    try:
        print(sql_search)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_search)
        results = cur_search.fetchall()
        print(cur_search.fetchall())
        db.commit()
        print('success search')
        return results
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()

def quarry_logs(tablename, db_file):
    sql_quarry_log = "select * from '{tablename}_logs' ".format(tablename = tablename)
    try:
        print(sql_quarry_log)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_quarry_log)
        results = cur_search.fetchall()
        print(cur_search.fetchall())
        db.commit()

        print('success quarry logs')
        return results
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()

def quarry_hardware_info(db_file):
    sql_quarry_hardwareinfo = "select * from hardware_info;"
    try:
        print(sql_quarry_hardwareinfo)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_quarry_hardwareinfo)
        results = cur_search.fetchall()
        print(cur_search.fetchall())
        db.commit()

        print('success quarry logs')
        return results
    except Exception as e:
        # db.rollback()
        traceback.print_exc()
        print('rollback')
    finally:
        db.close()



