import sqlite3
import traceback


def delete(tablename, version, algo, name, algoId, subTidN, bit, numK
                  , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU, algoSpe,
                  testSpe, castType, iOrd,
                  TBLM_ID, dpt, dpt_person, confirmation, info,db_file):
    list = [None] * 23

    if algo == 'None' or algo == '':
        list[0] = "'1'"
        algo = '1'
    else:
        list[0] = 'algo'


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
        list[7] = '1'
        tidW = '1'
    else:
        list[7] = 'tidW'

    if tidN == 'None' or tidN == '':
        list[8] = '1'
        tidN = '1'
    else:
        list[8] = 'tidN'

    if subTidW == 'None' or subTidW == '':
        list[9] = '1'
        subTidW = '1'
    else:
        list[9] = 'subTidW'

    if subTidN == 'None' or subTidN == '':
        list[4] = "'1'"
        subTidN = '1'
    else:
        list[4] = 'subTidN'

    if sTypeW_bit == 'None' or sTypeW_bit == '':
        list[10] = '1'
        sTypeW_bit = '1'
    else:
        list[10] = 'sTypeW_bit'

    if sType == 'None' or sType == '':
        list[11] = '1'
        sType = '1'
    else:
        list[11] = 'sType'

    if storeLocation == 'None' or storeLocation == '':
        list[12] = '1'
        storeLocation = '1'
    else:
        list[12] = 'storeLocation'

    if bit == 'None' or bit == '':
        list[5] = "'1'"
        bit = '1'
    else:
        list[5] = 'bit'

    if ISSU == 'None' or ISSU == '':
        list[13] = '1'
        ISSU = '1'
    else:
        list[13] = 'ISSU'


    if algoSpe == 'None' or algoSpe == '':
        list[14] = '1'
        algoSpe = '1'
    else:
        list[14] = 'algoSpe'

    if testSpe == 'None' or testSpe == '':
        list[15] = '1'
        testSpe = '1'
    else:
        list[15] = 'testSpe'

    if castType == 'None' or castType == '':
        list[16] = '1'
        castType = '1'
    else:
        list[16] = 'castType'

    if iOrd == 'None' or iOrd == '':
        list[17] = '1'
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

    if info == 'None' or info == '':
        list[22] = "'1'"
        info = '1'
    else:
        list[22] = 'info'

    sql_search = "delete from '{tablename}' where {version} = '{version_}' and {algo} = '{algo_}' and {name} = '{name_}' and {algoId} = '{algoId_}' and {subTidN} = '{subTidN_}' " \
                 "and {numK} = '{numK_}' " \
        .format(tablename=tablename,
                version = list[0],
                version_ = version,
                algo=list[1],
                algo_=algo,
                name=list[2],
                name_=name,
                subTidN=list[4],
                subTidN_=subTidN,
                algoId=list[3],
                algoId_=algoId,
                numK = list[6],
                numK_= numK

                )
    try:
        print(sql_search)
        db = sqlite3.connect(db_file)
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

def delete_revise(tablename, date, ver, intro, decision, content, reviser, db_file):
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
        db = sqlite3.connect(db_file)
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

def delete_table_from_form(formname, tablename, db_file):
    sql_delete = "delete from '{formname}'" \
                 " where tablename = '{tablename}';".format( tablename = tablename,formname = formname )
    sql_delete2 = "DROP TABLE '{tablename}';".format(tablename = tablename)
    try:
        print(sql_delete)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_delete)
        cur_search.execute(sql_delete2)

        print(cur_search.fetchall())
        db.commit()
        print('success delete')

    except Exception as e:
        raise e
    finally:
        db.close()

def delete_form_from_formstore(formname, db_file):
    sql_delete = "delete from form_store" \
                 " where formname = '{formname}';".format(formname=formname)
    sql_delete2 = "DROP TABLE '{formname}';".format(formname=formname)
    sql_delete3 = "DROP TABLE '{formname}_logs';".format(formname=formname)
    try:
        print(sql_delete)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_delete)
        cur_search.execute(sql_delete2)
        cur_search.execute(sql_delete3)
        print(cur_search.fetchall())
        db.commit()
        print('success delete')

    except Exception as e:
        raise e
    finally:
        db.close()

def delete_hardware_info(name, version, form, algo_core, tcam, algo, algo_engine, multi_core, core_type, cpu_type, makefile, cmake, ko, info, db_file):
    sql_delete = "delete from hardware_info where name = '{name}' and version = '{version}' and form = '{form}' and algo_core = '{algo_core}' " \
                 "and tcam = '{tcam}' and algo = '{algo}' and algo_engine = '{algo_engine}' and multi_core = '{multi_core}' and core_type = '{core_type}' and cpu_type = '{cpu_type}' and makefile = '{makefile}'" \
                 " and cmake = '{cmake}' and ko = '{ko}' and info = '{info}' ;" \
        .format(name=name,
                version=version,
                form=form,
                algo_core=algo_core,
                tcam=tcam,
                algo=algo,
                algo_engine=algo_engine,
                multi_core=multi_core,
                core_type=core_type,
                cpu_type=cpu_type,
                makefile=makefile,
                cmake=cmake,
                ko=ko,
                info=info
                )
    try:
        print(sql_delete)
        db = sqlite3.connect(db_file)
        cur_search = db.cursor()
        cur_search.execute(sql_delete)
        results = cur_search.fetchall()
        print(cur_search.fetchall())
        db.commit()
        log = '删除单板信息 ' + name +' 成功'
        print('success delete')
        return log
    except Exception as e:
        # db.rollback()
        traceback.print_exc()
        print('rollback')
    finally:
        db.close()