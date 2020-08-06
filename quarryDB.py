
import sqlite3
import traceback





#返回一个单板的所有条目
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

#返回一个形态表包含的所有单板
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
#返回所有形态表
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

#返回一个sql查询结果

def quarry_search(tablename, version ,end_version, algo, name, algoId, subTidN, bit, numK
                  , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU, algoSpe,
                  testSpe, castType, iOrd,
                  TBLM_ID, dpt, dpt_person, confirmation, info, tid_name, subtid_name, tcam_init, actionId, keytidw,
                   keysubtidw, keytidn, keysubtidn, db_file):
    list = [None] * 32

    if algo == 'None' or algo == '':
        list[0] = "'1'"
        algo = '1'
    else:
        list[0] = 'algo'

    if info == 'None' or info == '':
        list[23] = "'1'"
        info = '1'
    else:
        list[23] = 'info'

    if tid_name == 'None' or tid_name == '':
        list[24] = "'1'"
        tid_name = '1'
    else:
        list[24] = 'tid_name'

    if subtid_name == 'None' or subtid_name == '':
        list[25] = "'1'"
        subtid_name = '1'
    else:
        list[25] = 'subtid_name'

    if tcam_init == 'None' or tcam_init == '':
        list[26] = "'1'"
        tcam_init = '1'
    else:
        list[26] = 'tcam_init'

    if actionId == 'None' or actionId == '':
        list[27] = "'1'"
        actionId = '1'
    else:
        list[27] = 'actionId'

    if keytidw == 'None' or keytidw == '':
        list[28] = "'1'"
        keytidw = '1'
    else:
        list[28] = 'keytidw'

    if keysubtidw == 'None' or keysubtidw == '':
        list[29] = "'1'"
        keysubtidw = '1'
    else:
        list[29] = 'keysubtidw'

    if keytidn == 'None' or keytidn == '':
        list[30] = "'1'"
        keytidn = '1'
    else:
        list[30] = 'keytidn'

    if keysubtidn == 'None' or keysubtidn == '':
        list[31] = "'1'"
        keysubtidn = '1'
    else:
        list[31] = 'keysubtidn'


    if version == 'None' or version == '':
        list[1] = "'1'"
        version = '1'
    else:
        list[1] = 'version'


    if end_version == 'None' or end_version == '':
        list[2] = "'1'"
        end_version = '1'
    else:
        list[2] = 'end_version'

    if name == 'None' or name == '':
        list[3] = "'1'"
        name = '1'
    else:
        list[3] = 'name'

    if algoId == 'None' or algoId == '':
        list[4] = "'1'"
        algoId = '1'
    else:
        list[4] = 'algoId'

    if numK == 'None' or numK == '':
        list[7] = "'1'"
        numK = '1'
    else:
        list[7] = 'numK'

    if tidW == 'None' or tidW == '':
        list[8] = "'1'"
        tidW = '1'
    else:
        list[8] = 'tidW'

    if tidN == 'None' or tidN == '':
        list[9] = "'1'"
        tidN = '1'
    else:
        list[9] = 'tidN'

    if subTidW == 'None' or subTidW == '':
        list[10] = "'1'"
        subTidW = '1'
    else:
        list[10] = 'subTidW'

    if subTidN == 'None' or subTidN == '':
        list[5] = "'1'"
        subTidN = '1'
    else:
        list[5] = 'subTidN'

    if sTypeW_bit == 'None' or sTypeW_bit == '':
        list[11] = "'1'"
        sTypeW_bit = '1'
    else:
        list[11] = 'sTypeW_bit'

    if sType == 'None' or sType == '':
        list[12] = "'1'"
        sType = '1'
    else:
        list[12] = 'sType'

    if storeLocation == 'None' or storeLocation == '':
        list[13] = "'1'"
        storeLocation = '1'
    else:
        list[13] = 'storeLocation'

    if bit == 'None' or bit == '':
        list[6] = "'1'"
        bit = '1'
    else:
        list[6] = 'bit'

    if ISSU == 'None' or ISSU == '':
        list[14] = "'1'"
        ISSU = '1'
    else:
        list[14] = 'ISSU'


    if algoSpe == 'None' or algoSpe == '':
        list[15] = "'1'"
        algoSpe = '1'
    else:
        list[15] = 'algoSpe'

    if testSpe == 'None' or testSpe == '':
        list[16] = "'1'"
        testSpe = '1'
    else:
        list[16] = 'testSpe'

    if castType == 'None' or castType == '':
        list[17] = "'1'"
        castType = '1'
    else:
        list[17] = 'castType'

    if iOrd == 'None' or iOrd == '':
        list[18] = "'1'"
        iOrd = '1'
    else:
        list[18] = 'iOrd'

    if TBLM_ID == 'None' or TBLM_ID == '':
        list[19] = "'1'"
        TBLM_ID = '1'
    else:
        list[19] = 'TBLM_ID'

    if dpt == 'None' or dpt == '':
        list[20] = "'1'"
        dpt = '1'
    else:
        list[20] = 'dpt'

    if dpt_person == 'None' or dpt_person == '':
        list[21] = "'1'"
        dpt_person = '1'
    else:
        list[21] = 'dpt_person'

    if confirmation == 'None' or confirmation == '':
        list[22] = "'1'"
        confirmation = '1'
    else:
        list[22] = 'confirmation'

    sql_search = "select * from '{tablename}' where {algo} = '{algo_}' and {version} = '{version_}' and {end_version} = '{end_version_}' and {name} = '{name_}' and {algoId} = '{algoId_}' and {subTidN} = '{subTidN_}' and {bit} = '{bit_}'" \
                 " and {numK} = '{numK_}' and {tidW} = '{tidW_}' and {tidN} = '{tidN_}' and {subTidW} = '{subTidW_}'" \
                 " and {sTypeW_bit} = '{sTypeW_bit_}' and {sType} = '{sType_}' and {storeLocation} = '{storeLocation_}'" \
                 " and {ISSU} = '{ISSU_}' and {algoSpe} = '{algoSpe_}' and {testSpe} = '{testSpe_}'" \
                 " and {castType} = '{castType_}' and {iOrd} = '{iOrd_}' and {TBLM_ID} = '{TBLM_ID_}' and {dpt} = '{dpt_}'" \
                 " and {dpt_person} = '{dpt_person_}' and {confirmation} = '{confirmation_}' and {info} = '{info_}' and {tid_name} = '{tid_name_}'" \
                 " and {subtid_name} = '{subtid_name_}' and {tcam_init} = '{tcam_init_}' and {actionId} = '{actionId_}'" \
                 " and {keytidw} = '{keytidw_}' and {keysubtidw} = '{keysubtidw_}' and {keytidn} = '{keytidn_}' " \
                 " and {keysubtidn} = '{keysubtidn_}' order by cast(algoId AS INT), cast(subTidN AS INT)".format(tablename=tablename,
                                                                                                 algo=list[0],
                                                                                                 algo_=algo,
                                                                                                 version = list[1],
                                                                                                 version_ = version,
                                                                                                 end_version = list[2],
                                                                                                 end_version_ = end_version,
                                                                                                 name=list[3],
                                                                                                 name_=name,
                                                                                                 bit=list[6],
                                                                                                 bit_=bit,
                                                                                                 numK=list[7],
                                                                                                 numK_=numK,
                                                                                                 tidW=list[8],
                                                                                                 tidW_=tidW,
                                                                                                 tidN=list[9],
                                                                                                 tidN_=tidN,
                                                                                                 subTidW=list[10],
                                                                                                 subTidW_=subTidW,
                                                                                                 subTidN=list[5],
                                                                                                 subTidN_=subTidN,
                                                                                                 sTypeW_bit=list[11],
                                                                                                 sTypeW_bit_=sTypeW_bit,
                                                                                                 sType=list[12],
                                                                                                 sType_=sType,
                                                                                                 storeLocation=list[13],
                                                                                                 storeLocation_=storeLocation,
                                                                                                 algoId=list[4],
                                                                                                 algoId_=algoId,
                                                                                                 ISSU=list[14],
                                                                                                 ISSU_=ISSU,
                                                                                                 algoSpe=list[15],
                                                                                                 algoSpe_=algoSpe,
                                                                                                 testSpe=list[16],
                                                                                                 testSpe_=testSpe,
                                                                                                 castType=list[17],
                                                                                                 castType_=castType,
                                                                                                 iOrd=list[18],
                                                                                                 iOrd_=iOrd,
                                                                                                 TBLM_ID=list[19],
                                                                                                 TBLM_ID_=TBLM_ID,
                                                                                                 dpt=list[20],
                                                                                                 dpt_=dpt,
                                                                                                 dpt_person=list[21],
                                                                                                 dpt_person_=dpt_person,
                                                                                                 confirmation=list[22],
                                                                                                 confirmation_=confirmation,
                                                                                                 info = list[23],
                                                                                                 info_ = info,
                                                                                                 tid_name =  list[24],
                                                                                                 tid_name_= tid_name,
                                                                                                 subtid_name=list[25],
                                                                                                 subtid_name_=subtid_name,
                                                                                                 tcam_init=list[26],
                                                                                                 tcam_init_=tcam_init,
                                                                                                 actionId=list[27],
                                                                                                 actionId_=actionId,
                                                                                                 keytidw=list[28],
                                                                                                 keytidw_=keytidw,
                                                                                                 keysubtidw=list[29],
                                                                                                 keysubtidw_=keysubtidw,
                                                                                                 keytidn=list[30],
                                                                                                 keytidn_=keytidn,
                                                                                                                 keysubtidn=list[31],
                                                                                                                 keysubtidn_=keysubtidn,




                                                                                                 )


    # 'tid_name': 'TID名称',
    # 'subtid_name': 'SubTid名称',
    # 'tcam_init': 'TCAM起始位置',
    # 'actionId': '动作表ID',
    # 'keytidw': 'keyTID位宽',
    # 'keysubtidw': 'keySubtid位宽',
    # 'keytidn': 'keyTID值',
    # 'keysubtidn': 'keySubtid值'
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
        traceback.print_exc()
        print('rollback')
    finally:
        db.close()
#返回一个形态表的修订记录
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
#返回单板信息
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



