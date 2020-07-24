import sqlite3
import traceback
import constants

def update_db(tablename,version, end_version, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation, info,index,copy):

    if algo == '' or algo.isspace():
        algo = 'N/A'
    if version == '' or version.isspace():
        version = 'N/A'

    if end_version == '' or end_version.isspace():
        end_version = 'N/A'

    if info == '' or info.isspace():
        info = 'N/A'

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

    if copy[index][1] == version and copy[index][2] == end_version and copy[index][3] == algo and copy[index][4] == name and copy[index][5] == algoId and copy[index][6] == subTidN and copy[index][7] == bit and copy[index][8] == numK and copy[index][9] == tidW \
        and copy[index][10] == tidN and copy[index][11] == subTidW and copy[index][12] == sTypeW_bit and copy[index][13] == sType and copy[index][14] == storeLocation and copy[index][15] == ISSU \
        and copy[index][16] == algoSpe and copy[index][17] == testSpe and copy[index][18] == castType and copy[index][19] == iOrd and copy[index][20] == TBLM_ID and copy[index][21] == dpt \
        and copy[index][22] == dpt_person and copy[index][23] == confirmation and copy[index][24] == info:
        return

    loginfo = []

    if copy[index][1] != version:
        loginfo.append(constants.head_name['version'] + ' 从 ' + copy[index][1] +' 更改为 '+ version +'。 ')
    if copy[index][2] != end_version:
        loginfo.append(constants.head_name['end_version'] + ' 从 ' + copy[index][2] +' 更改为 '+ end_version +'。 ')
    if copy[index][3] != algo:
        loginfo.append(constants.head_name['algo'] + ' 从 ' + copy[index][3] +' 更改为 '+ algo +'。 ')
    if copy[index][4] != name:
        loginfo.append(constants.head_name['name'] + ' 从 ' + copy[index][4] +' 更改为 '+ name +'。 ')
    if copy[index][5] != algoId:
        loginfo.append(constants.head_name['algoId'] + ' 从 ' + copy[index][5] +' 更改为 '+ algoId +'。 ')
    if copy[index][6] != subTidN:
        loginfo.append(constants.head_name['subTidN'] + ' 从 ' + copy[index][6] +' 更改为 '+ subTidN +'。 ')
    if copy[index][7] != bit:
        loginfo.append(constants.head_name['bit'] + ' 从 ' + copy[index][7] +' 更改为 '+ bit +'。 ')
    if copy[index][8] != numK:
        loginfo.append(constants.head_name['numK'] + ' 从 ' + copy[index][8] +' 更改为 '+ numK +'。 ')
    if copy[index][9] != tidW:
        loginfo.append(constants.head_name['tidW'] + ' 从 ' + copy[index][9] +' 更改为 '+ tidW +'。 ')
    if copy[index][10] != tidN:
        loginfo.append(constants.head_name['tidN'] + ' 从 ' + copy[index][10] +' 更改为 '+ tidN +'。 ')
    if copy[index][11] != subTidW:
        loginfo.append(constants.head_name['subTidW'] + ' 从 ' + copy[index][11] +' 更改为 '+ subTidW +'。 ')
    if copy[index][12] != sTypeW_bit:
        loginfo.append(constants.head_name['sTypeW_bit'] + ' 从 ' + copy[index][12] +' 更改为 '+ sTypeW_bit +'。 ')
    if copy[index][13] != sType:
        loginfo.append(constants.head_name['sType'] + ' 从 ' + copy[index][13] +' 更改为 '+ sType +'。 ')
    if copy[index][14] != storeLocation:
        loginfo.append(constants.head_name['storeLocation'] + ' 从 ' + copy[index][14] +' 更改为 '+ storeLocation +'。 ')
    if copy[index][15] != ISSU:
        loginfo.append(constants.head_name['ISSU'] + ' 从 ' + copy[index][15] +' 更改为 '+ ISSU +'。 ')
    if copy[index][16] != algoSpe:
        loginfo.append(constants.head_name['algoSpe'] + ' 从 ' + copy[index][16] +' 更改为 '+ algoSpe +'。 ')
    if copy[index][17] != testSpe:
        loginfo.append(constants.head_name['testSpe'] + ' 从 ' + copy[index][17] +' 更改为 '+ testSpe +'。 ')
    if copy[index][18] != castType:
        loginfo.append(constants.head_name['castType'] + ' 从 ' + copy[index][18] +' 更改为 '+ castType +'。 ')
    if copy[index][19] != iOrd:
        loginfo.append(constants.head_name['iOrd'] + ' 从 ' + copy[index][19] +' 更改为 '+ iOrd +'。 ')
    if copy[index][20] != TBLM_ID:
        loginfo.append(constants.head_name['TBLM_ID'] + '从 ' + copy[index][20] +' 更改为 '+ TBLM_ID +'。 ')
    if copy[index][21] != dpt:
        loginfo.append(constants.head_name['dpt'] + ' 从 ' + copy[index][21] +' 更改为 '+ dpt +'。 ')
    if copy[index][22] != dpt_person:
        loginfo.append(constants.head_name['dpt_person'] + ' 从 ' + copy[index][22] +' 更改为 '+ dpt_person +'。 ')
    if copy[index][23] != confirmation:
        loginfo.append(constants.head_name['confirmation'] + ' 从 ' + copy[index][23] +' 更改为 '+ confirmation +'。 ')
    if copy[index][24] != info:
        loginfo.append(constants.head_name['info'] + ' 从 ' + copy[index][24] +' 更改为 '+ info +'。 ')






    sql_update = "update '{tablename}' set version = '{version_}', end_version = '{end_version_}', algo = '{algo_}',name = '{name_}' ,algoId = '{algoId_}' , subTidN = '{subTidN_}' ,bit = '{bit_}'" \
                 " , numK = '{numK_}' , tidW = '{tidW_}' , tidN = '{tidN_}' ,subTidW = '{subTidW_}'" \
                 " ,sTypeW_bit = '{sTypeW_bit_}' ,sType = '{sType_}' ,storeLocation = '{storeLocation_}'" \
                 " ,ISSU = '{ISSU_}' ,algoSpe = '{algoSpe_}' ,testSpe = '{testSpe_}'" \
                 " ,castType = '{castType_}' ,iOrd = '{iOrd_}' ,TBLM_ID = '{TBLM_ID_}' ,dpt = '{dpt_}'" \
                 " ,dpt_person = '{dpt_person_}' ,confirmation = '{confirmation_}', info = '{info_}' where version = '{copy_version}' and end_version = '{copy_end_version}' and algo = '{copy_algo}'" \
                 " and name = '{copy_name}' and algoId = '{copy_algoId}' and subTidN = '{copy_subTidN}'".format(tablename=tablename,
                                                                                                           version_ = version,
                                                                                                           end_version_ = end_version,
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
                                                                                                           info_ = info,

                                                                                                           copy_version = copy[index][1],
                                                                                                           copy_end_version = copy[index][2],
                                                                                                           copy_algo = copy[index][3],
                                                                                                           copy_name = copy[index][4],
                                                                                                           copy_algoId = copy[index][5],
                                                                                                           copy_subTidN = copy[index][6]
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

def update_revise_db(tablename, date, ver, intro, decision, content, reviser, index, copy_logs, db_file):
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
        db = sqlite3.connect(db_file)
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

def sql_excecute(sql_store, db_file):
    try:
        db = sqlite3.connect(db_file)
        cur_update = db.cursor()
        for i in sql_store:
            cur_update.execute(i)
        db.commit()
    except Exception as e:
        # db.rollback()
        print('rollback')
        traceback.print_exc()
        raise e
    finally:
        db.close()