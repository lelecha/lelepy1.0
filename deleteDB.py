import sqlite3





def delete(tablename, algo, name, algoId, subTidN, bit, numK
                  , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU, algoSpe,
                  testSpe, castType, iOrd,
                  TBLM_ID, dpt, dpt_person, confirmation):
    list = [None] * 21

    if algo == 'N/A' or algo == '':
        list[0] = "'1'"
        algo = '1'
    else:
        list[0] = 'algo'

    if name == 'N/A' or name == '':
        list[1] = "'1'"
        name = '1'
    else:
        list[1] = 'name'

    if algoId == 'N/A' or algoId == '':
        list[2] = "'1'"
        algoId = '1'
    else:
        list[2] = 'algoId'

    if numK == 'N/A' or numK == '':
        list[5] = "'1'"
        numK = '1'
    else:
        list[5] = 'numK'

    if tidW == 'N/A' or tidW == '':
        list[6] = '1'
        tidW = '1'
    else:
        list[6] = 'tidW'

    if tidN == 'N/A' or tidN == '':
        list[7] = '1'
        tidN = '1'
    else:
        list[7] = 'tidN'

    if subTidW == 'N/A' or subTidW == '':
        list[8] = '1'
        subTidW = '1'
    else:
        list[8] = 'subTidW'

    if subTidN == 'N/A' or subTidN == '':
        list[3] = "'1'"
        subTidN = '1'
    else:
        list[3] = 'subTidN'

    if sTypeW_bit == 'N/A' or sTypeW_bit == '':
        list[9] = '1'
        sTypeW_bit = '1'
    else:
        list[9] = 'sTypeW_bit'

    if sType == 'N/A' or sType == '':
        list[10] = '1'
        sType = '1'
    else:
        list[10] = 'sType'

    if storeLocation == 'N/A' or storeLocation == '':
        list[11] = '1'
        storeLocation = '1'
    else:
        list[11] = 'storeLocation'

    if bit == 'N/A' or bit == '':
        list[4] = "'1'"
        bit = '1'
    else:
        list[4] = 'bit'

    if ISSU == 'N/A' or ISSU == '':
        list[12] = '1'
        ISSU = '1'
    else:
        list[12] = 'ISSU'


    if algoSpe == 'N/A' or algoSpe == '':
        list[13] = '1'
        algoSpe = '1'
    else:
        list[13] = 'algoSpe'

    if testSpe == 'N/A' or testSpe == '':
        list[14] = '1'
        testSpe = '1'
    else:
        list[14] = 'testSpe'

    if castType == 'N/A' or castType == '':
        list[15] = '1'
        castType = '1'
    else:
        list[15] = 'castType'

    if iOrd == 'N/A' or iOrd == '':
        list[16] = '1'
        iOrd = '1'
    else:
        list[16] = 'iOrd'

    if TBLM_ID == 'N/A' or TBLM_ID == '':
        list[17] = "'1'"
        TBLM_ID = '1'
    else:
        list[17] = 'TBLM_ID'

    if dpt == 'N/A' or dpt == '':
        list[18] = "'1'"
        dpt = '1'
    else:
        list[18] = 'dpt'

    if dpt_person == 'N/A' or dpt_person == '':
        list[19] = "'1'"
        dpt_person = '1'
    else:
        list[19] = 'dpt_person'

    if confirmation == 'N/A' or confirmation == '':
        list[20] = "'1'"
        confirmation = '1'
    else:
        list[20] = 'confirmation'

    sql_search = "delete from '{tablename}' where {algo} = '{algo_}' and {name} = '{name_}' and {algoId} = '{algoId_}' and {subTidN} = '{subTidN_}' " \
        .format(tablename=tablename, algo=list[0],
                algo_=algo,
                name=list[1],
                name_=name,
                subTidN=list[3],
                subTidN_=subTidN,
                algoId=list[2],
                algoId_=algoId,

                )
    try:
        print(sql_search)
        db = sqlite3.connect('test2.db')
        cur_search = db.cursor()
        cur_search.execute(sql_search)
        results = cur_search.fetchall()
        print(cur_search.fetchall())
        db.commit()
        log = '删除 '+ tablename +' 中业务名为 ' + name +' 的条目成功'
        print('success delete')
        return log
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()

def delete_revise(tablename, date, ver, intro, decision, content, reviser):
    sql_delete = "delete from '{tablename}_logs'" \
                 " where date = '{date}' and ver = '{ver}' and intro = '{intro}' and decision = '{decision}' and content = '{content}' and reviser = '{reviser}'".format( tablename = tablename,
                                                                                                                                         date = date,
                                                                                                                                         ver = ver,
                                                                                                                                         intro = intro,
                                                                                                                                         decision = decision,
                                                                                                                                         content = content,
                                                                                                                                         reviser = reviser
                                                                                                                                         )
    try:
        print(sql_delete)
        db = sqlite3.connect('test2.db')
        cur_search = db.cursor()
        cur_search.execute(sql_delete)
        print(cur_search.fetchall())
        db.commit()
        print('success delete')

    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()

    #
    # "and {bit} = {bit_}" \
    # " and {numK} = {numK_} and {tidW} = {tidW_} and {tidN} = {tidN_} and {subTidW} = {subTidW_}" \
    # " and {sTypeW_bit} = {sTypeW_bit_} and {sType} = {sType_} and {storeLocation} = '{storeLocation_}'" \
    # " and {ISSU} = {ISSU_} and {algoSpe} = {algoSpe_} and {testSpe} = {testSpe_}" \
    # " and {castType} = '{castType_}' and {iOrd} = '{iOrd_}' and {TBLM_ID} = {TBLM_ID_} and {dpt} = '{dpt_}'" \
    # " and {dpt_person} = '{dpt_person_}' and {confirmation} = '{confirmation_}' "\