
import sqlite3


def insert_db(tablename, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation):


    if algo == '':

        algo = 'N/A'


    if name == '':

        name = 'N/A'

    if algoId == '':
        algoId = 'N/A'

    if subTidN == '':
        subTidN = 'N/A'
    if bit == '':
        bit = 'N/A'
    if numK == '':
        numK = 'N/A'

    if tidW == '':
        tidW = 'N/A'

    if tidN == '':
        tidN = 'N/A'

    if subTidW == '':
        subTidW = 'N/A'

    if sTypeW_bit == '':
        sTypeW_bit = 'N/A'

    if  sType == '':
        sType = 'N/A'

    if storeLocation == '':
        storeLocation = 'N/A'

    if ISSU == '':
        ISSU = 'N/A'

    if algoSpe == '':
        algoSpe = 'N/A'

    if testSpe == '':
        testSpe = 'N/A'

    if castType == '':
        castType = 'N/A'

    if iOrd == '':
        iOrd = 'N/A'

    if TBLM_ID == '':
        TBLM_ID = 'N/A'

    if dpt == '':
        dpt = 'N/A'

    if dpt_person == '':
        dpt_person = 'N/A'

    if confirmation == '':
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
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        cur_insert.execute(sql_insert)
        db.commit()
        print('success insert')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()
