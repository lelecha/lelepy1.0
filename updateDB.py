import sqlite3
import traceback
import UITest4
import constants

def update_db(tablename, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation, index, copy):
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

    if sType == '' or sType.isspace():
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

    if copy[index][1] == algo and copy[index][2] == name and copy[index][3] == algoId and copy[index][4] == subTidN and copy[index][5] == bit and copy[index][6] == numK and copy[index][7] == tidW \
        and copy[index][8] == tidN and copy[index][9] == subTidW and copy[index][10] == sTypeW_bit and copy[index][11] == sType and copy[index][12] == storeLocation and copy[index][13] == ISSU \
        and copy[index][14] == algoSpe and copy[index][15] == testSpe and copy[index][16] == castType and copy[index][17] == iOrd and copy[index][18] == TBLM_ID and copy[index][19] == dpt \
        and copy[index][20] == dpt_person and copy[index][21] == confirmation:
        return

    loginfo = []

    if copy[index][1] != algo:
        loginfo.append(constants.head_name['algo'] + ' 从 ' + copy[index][1] +' 更改为 '+ algo +'。 ')
    if copy[index][2] != name:
        loginfo.append(constants.head_name['name'] + ' 从 ' + copy[index][2] +' 更改为 '+ name +'。 ')
    if copy[index][3] != algoId:
        loginfo.append(constants.head_name['algoId'] + ' 从 ' + copy[index][3] +' 更改为 '+ algoId +'。 ')
    if copy[index][4] != subTidN:
        loginfo.append(constants.head_name['subTidN'] + ' 从 ' + copy[index][4] +' 更改为 '+ subTidN +'。 ')
    if copy[index][5] != bit:
        loginfo.append(constants.head_name['bit'] + ' 从 ' + copy[index][5] +' 更改为 '+ bit +'。 ')
    if copy[index][6] != numK:
        loginfo.append(constants.head_name['numK'] + ' 从 ' + copy[index][6] +' 更改为 '+ numK +'。 ')
    if copy[index][7] != tidW:
        loginfo.append(constants.head_name['tidW'] + ' 从 ' + copy[index][7] +' 更改为 '+ tidW +'。 ')
    if copy[index][8] != tidN:
        loginfo.append(constants.head_name['tidN'] + ' 从 ' + copy[index][8] +' 更改为 '+ tidN +'。 ')
    if copy[index][9] != subTidW:
        loginfo.append(constants.head_name['subTidW'] + ' 从 ' + copy[index][9] +' 更改为 '+ subTidW +'。 ')
    if copy[index][10] != sTypeW_bit:
        loginfo.append(constants.head_name['sTypeW_bit'] + ' 从 ' + copy[index][10] +' 更改为 '+ sTypeW_bit +'。 ')
    if copy[index][11] != sType:
        loginfo.append(constants.head_name['sType'] + ' 从 ' + copy[index][11] +' 更改为 '+ sType +'。 ')
    if copy[index][12] != storeLocation:
        loginfo.append(constants.head_name['storeLocation'] + ' 从 ' + copy[index][12] +' 更改为 '+ storeLocation +'。 ')
    if copy[index][13] != ISSU:
        loginfo.append(constants.head_name['ISSU'] + ' 从 ' + copy[index][13] +' 更改为 '+ ISSU +'。 ')
    if copy[index][14] != algoSpe:
        loginfo.append(constants.head_name['algoSpe'] + ' 从 ' + copy[index][14] +' 更改为 '+ algoSpe +'。 ')
    if copy[index][15] != testSpe:
        loginfo.append(constants.head_name['testSpe'] + ' 从 ' + copy[index][15] +' 更改为 '+ testSpe +'。 ')
    if copy[index][16] != castType:
        loginfo.append(constants.head_name['castType'] + ' 从 ' + copy[index][16] +' 更改为 '+ castType +'。 ')
    if copy[index][17] != iOrd:
        loginfo.append(constants.head_name['iOrd'] + ' 从 ' + copy[index][17] +' 更改为 '+ iOrd +'。 ')
    if copy[index][18] != TBLM_ID:
        loginfo.append(constants.head_name['TBLM_ID'] + '从 ' + copy[index][18] +' 更改为 '+ TBLM_ID +'。 ')
    if copy[index][19] != dpt:
        loginfo.append(constants.head_name['dpt'] + ' 从 ' + copy[index][19] +' 更改为 '+ dpt +'。 ')
    if copy[index][20] != dpt_person:
        loginfo.append(constants.head_name['dpt_person'] + ' 从 ' + copy[index][20] +' 更改为 '+ dpt_person +'。 ')
    if copy[index][21] != confirmation:
        loginfo.append(constants.head_name['confirmation'] + ' 从 ' + copy[index][21] +' 更改为 '+ confirmation +'。 ')




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
    # try:

        # db = sqlite3.connect('test2.db')
        # cur_insert = db.cursor()
        # cur_insert.execute(sql_update)
        # db.commit()
        # print(sql_update)
    log = '将'+ tablename +'中的'
    for i in loginfo:
        log += i

    return log, sql_update
    # except Exception as e:
    #     # db.rollback()
    #     raise Exception
    #     traceback.print_exc()
    #
    # finally:
    #     db.close()

def update_revise_db(tablename, date, ver, intro, decision, content, reviser, index, copy_logs):
    if date == '':

        date = 'N/A'


    if ver == '':

        ver = 'N/A'

    if intro == '':
        intro = 'N/A'

    if decision == '':
        decision = 'N/A'
    if content == '':
        content = 'N/A'
    if reviser == '':
        reviser = 'N/A'
    if  copy_logs[index][0] == date and copy_logs[index][1] == ver and copy_logs[index][2] == intro and copy_logs[index][3] == decision and copy_logs[index][4] == content and copy_logs[index][5] == reviser:
        return

    sql_update = "update '{tablename}_logs' set date = '{date}', ver = '{ver}', intro = '{intro}', decision = '{decision}', content = '{content}', reviser = '{reviser}'" \
                 " where date = '{copy_date}' and ver = '{copy_ver}' and intro = '{copy_intro}' and decision = '{copy_decision}' and content = '{copy_content}' and " \
                 "reviser = '{copy_reviser}'".format( tablename = tablename,
                                                                                                                                         date = date,
                                                                                                                                         ver = ver,
                                                                                                                                         intro = intro,
                                                                                                                                         decision = decision,
                                                                                                                                         content = content,
                                                                                                                                         reviser = reviser,
                                                                                                                                         copy_date = copy_logs[index][0],
                                                                                                                                         copy_ver = copy_logs[index][1],
                                                                                                                                         copy_intro= copy_logs[index][2],
                                                                                                                                         copy_decision = copy_logs[index][3],
                                                                                                                                          copy_content = copy_logs[index][4],
                                                                                                                                          copy_reviser = copy_logs[index][5])




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
        traceback.print_exc()
    finally:
        db.close()

def sql_excecute(sql_store):
    try:
        db = sqlite3.connect('test2.db')
        cur_update = db.cursor()
        for i in sql_store:
            cur_update.execute(i)
        db.commit()
    except Exception as e:
        # db.rollback()
        print('rollback')
        traceback.print_exc()
        raise Exception
    finally:
        db.close()