import sqlite3

def update_db(tablename, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation, index, copy):
    sql_update = "update '{tablename}' set algo = '{algo_}',name = '{name_}' ,algoId = '{algoId_}' , subTidN = '{subTidN_}' ,bit = '{bit_}'" \
                 " , numK = '{numK_}' , tidW = '{tidW_}' , tidN = '{tidN_}' ,subTidW = '{subTidW_}'" \
                 " ,sTypeW_bit = '{sTypeW_bit_}' ,sType = '{sType_}' ,storeLocation = '{storeLocation_}'" \
                 " ,ISSU = '{ISSU_}' ,algoSpe = '{algoSpe_}' ,testSpe = '{testSpe_}'" \
                 " ,castType = '{castType_}' ,iOrd = '{iOrd_}' ,TBLM_ID = '{TBLM_ID_}' ,dpt = '{dpt_}'" \
                 " ,dpt_person = '{dpt_person_}' ,confirmation = '{confirmation_}' where algo = '{copy_algo}'" \
                 " and name = '{copy_name}' and algoId = '{copy_algoId}' and subTidN = '{copy_subTidN}'".format(tablename=tablename,
                                                                                                           algo_=algo,
                                                                                                           name_=name,
                                                                                                           bit_=bit,
                                                                                                           numK_=numK,
                                                                                                           tidW_=tidW,
                                                                                                           tidN_=tidN,
                                                                                                           subTidW_=subTidW,
                                                                                                           subTidN_=subTidN,
                                                                                                           sTypeW_bit_=sTypeW_bit,
                                                                                                           sType_=sType,
                                                                                                           storeLocation_=storeLocation,
                                                                                                           algoId_=algoId,
                                                                                                           ISSU_ = ISSU,
                                                                                                           algoSpe_=algoSpe,
                                                                                                           testSpe_=testSpe,
                                                                                                           castType_=castType,
                                                                                                           iOrd_=iOrd,
                                                                                                           TBLM_ID_=TBLM_ID,
                                                                                                           dpt_=dpt,
                                                                                                           dpt_person_=dpt_person,
                                                                                                           confirmation_=confirmation,
                                                                                                           copy_algo = copy[index][1],
                                                                                                           copy_name = copy[index][2],
                                                                                                           copy_algoId = copy[index][3],
                                                                                                           copy_subTidN = copy[index][4]
                                                                                                                )



    print(sql_update)
    try:
        db = sqlite3.connect('test2.db')
        cur_insert = db.cursor()
        cur_insert.execute(sql_update)
        db.commit()
        print('success update')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()
