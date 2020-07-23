
import sqlite3
import traceback


def insert_db(tablename, version, algo, name, algoId, subTidN, bit, numK
              , tidW, tidN, subTidW, sTypeW_bit, sType, storeLocation, ISSU,algoSpe,
              testSpe, castType, iOrd,
              TBLM_ID, dpt, dpt_person, confirmation, info):

    try:
        if algo == '' or algo.isspace() or algo == 'None':
            raise Exception('算法名不可为空')
            algo = 'None'

        if version == '' or version.isspace() or version == 'None':
            raise Exception('版本号不可为空')
            version = 'None'


        if name == '' or name.isspace() or name == 'None':
            print("名字为空")
            raise Exception('业务名不可为空')
            name = 'None'

        if algoId == '' or algoId.isspace() or algoId == 'None':
            raise Exception('算法表ID不可为空')
            algoId = 'None'

        if subTidN == '' or subTidN.isspace() or subTidN == 'None':
            raise Exception('SubTid不可为空')
            subTidN = 'None'
        if bit == '' or bit.isspace() or bit == 'None':
            raise Exception('位宽不可为空')
            bit = 'None'
        if numK == '' or numK.isspace() or numK == 'None' :
            raise Exception('条数不可为空')
            numK = 'None'

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


        if info == '' or info.isspace():
            info = 'None'

        sql_insert = "insert into '{tablename}' (id, version ,algo, name, bit, numK, tidW, tidN, subTidW, subTidN, sTypeW_bit, sType, " \
                     "storeLocation, algoId,ISSU,algoSpe, testSpe, " \
                     "castType, iOrd, TBLM_ID, dpt, dpt_person, confirmation, info) " \
                     "values ( NULL,'{version}','{algo}','{name}', '{bit}', '{numK}', '{tidW}', '{tidN}', '{subTidW}', " \
                     "'{subTidN}', '{sTypeW_bit}', '{sType}', '{storeLocation}', '{algoId}','{ISSU}','{algoSpe}','{testSpe}', " \
                     "'{castType}', '{iOrd}', '{TBLM_ID}', '{dpt}', '{dpt_person}', '{confirmation}','{info}');".format(tablename=tablename,
                                                                                                               algo=algo,
                                                                                                               version = version,
                                                                                                               info = info,
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
def insert_form(formname, db_file):
    try:
        db = sqlite3.connect(db_file)
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
def insert_hardware(formname, tablename, db_file):
    try:
        db = sqlite3.connect(db_file)
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



def insert_logs(tablename, date, ver, intro, decision, content, reviser, db_file):

    if date == '' or date.isspace():

        date = 'None'


    if ver == '' or ver.isspace():

        ver = 'None'

    if intro == '' or intro.isspace():
        intro = 'None'

    if decision == '' or decision.isspace():
        decision = 'None'
    if content == ''or content.isspace():
        content = 'None'
    if reviser == '' or reviser.isspace():
        reviser = 'None'


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
        db = sqlite3.connect(db_file)
        cur_insert = db.cursor()
        cur_insert.execute(sql_insert_logs)
        db.commit()


        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()


def excecute_sql(sql_store, db_file):
    try:
        db = sqlite3.connect(db_file)
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
def insert_hardware_info(name, version, form, algo_core, tcam, algo, algo_engine, multi_core, core_type, cpu_type, makefile, cmake, ko, info, db_file):


    if name == '' or name.isspace():
        name = 'None'
    if version == '' or version.isspace():
        version = 'None'
    if form == '' or form.isspace():
        form = 'None'
    if algo_core == '' or algo_core.isspace():
        algo_core = 'None'
    if tcam == ''or tcam.isspace():
        tcam = 'None'
    if algo == '' or algo.isspace():
        algo = 'None'
    if algo_engine == '' or algo_engine.isspace():
        algo_engine = 'None'
    if multi_core == '' or multi_core.isspace():
        algo = 'N/A'
    if core_type == '' or core_type.isspace():
        core_type = 'None'
    if cpu_type == '' or cpu_type.isspace():
        cpu_type = 'None'
    if makefile == '' or makefile.isspace():
        makefile = 'None'
    if cmake == '' or cmake.isspace():
        cmake = 'None'
    if ko == '' or ko.isspace():
        ko = 'None'
    if info == '' or info.isspace():
        info = 'None'


    sql_insert_hardware_info = "insert into 'hardware_info'(name, version, form, algo_core, tcam, algo, algo_engine, multi_core, core_type, cpu_type, makefile, cmake, ko, info) values " \
                      "('{name}', '{version}', '{form}', '{algo_core}', '{tcam}', '{algo}', '{algo_engine}', '{multi_core}', '{core_type}', '{cpu_type}', '{makefile}', '{cmake}', '{ko}', '{info}')" \
                      "".format(name= name, version = version, form = form, algo_core = algo_core,
                                tcam = tcam, algo = algo, algo_engine = algo_engine, multi_core = multi_core, core_type = core_type,
                                cpu_type = cpu_type, makefile = makefile, cmake = cmake, ko = ko, info = info)

    try:
        db = sqlite3.connect(db_file)
        cur_insert = db.cursor()
        cur_insert.execute(sql_insert_hardware_info)
        db.commit()


        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()

def insert_hardware_info_tmp(name, version, form, algo_core, tcam, algo, algo_engine, multi_core, core_type, cpu_type, makefile, cmake, ko, info,db_file):


    if name == '' or name.isspace():
        name = 'None'
    if version == '' or version.isspace():
        version = 'None'
    if form == '' or form.isspace():
        form = 'None'
    if algo_core == '' or algo_core.isspace():
        algo_core = 'None'
    if tcam == ''or tcam.isspace():
        tcam = 'None'
    if algo == '' or algo.isspace():
        algo = 'None'
    if algo_engine == '' or algo_engine.isspace():
        algo_engine = 'None'
    if multi_core == '' or multi_core.isspace():
        algo = 'None'
    if core_type == '' or core_type.isspace():
        core_type = 'None'
    if cpu_type == '' or cpu_type.isspace():
        cpu_type = 'None'
    if makefile == '' or makefile.isspace():
        makefile = 'None'
    if cmake == '' or cmake.isspace():
        cmake = 'None'
    if ko == '' or ko.isspace():
        ko = 'None'
    if info == '' or info.isspace():
        info = 'None'


    sql_insert_hardware_info = "insert into 'hardware_info_tmp'(name, version, form, algo_core, tcam, algo, algo_engine, multi_core, core_type, cpu_type, makefile, cmake, ko, info) values " \
                      "('{name}', '{version}', '{form}', '{algo_core}', '{tcam}', '{algo}', '{algo_engine}', '{multi_core}', '{core_type}', '{cpu_type}', '{makefile}', '{cmake}', '{ko}', '{info}')" \
                      "".format(name= name, version = version, form = form, algo_core = algo_core,
                                tcam = tcam, algo = algo, algo_engine = algo_engine, multi_core = multi_core, core_type = core_type,
                                cpu_type = cpu_type, makefile = makefile, cmake = cmake, ko = ko, info = info)

    try:
        db = sqlite3.connect(db_file)
        cur_insert = db.cursor()
        cur_insert.execute(sql_insert_hardware_info)
        db.commit()


        print('success insert logs')
    except Exception as e:
        # db.rollback()
        print('rollback')
    finally:
        db.close()



