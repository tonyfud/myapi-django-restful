from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
import json
import pymysql

def getLog(request):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123.com", "ops")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM ops_logs order by id desc"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        data = cursor.fetchall()
        print(data)

    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    jsonData = []
    for row in data:
        result = {}
        result['id'] = row[0]
        result['datetime'] = str(row[1])
        result['status'] = row[2]
        result['user'] = str(row[3])
        result['info'] = str(row[4])
        result['type'] = str(row[5])
        result['jobsid'] = row[6]
        jsonData.append(result)

    js_root = {}
    js_secondary = {}
    js_secondary['items'] = jsonData
    js_root['code'] = 20000
    #js_root['message'] = 'success'
    js_root['data'] = js_secondary
    print(json.dumps(js_root))
    return HttpResponse(json.dumps(js_root), content_type="application/json")

    #return HttpResponse('{"code": 20000, "data": {"items": [{"id": 40, "datetime": "2018-08-24 08:05:11", "status": "wating", "user": "admin", "info": "clean site cache : ", "type": "", "jobsid": null}, {"id": 39, "datetime": "2018-08-24 06:31:15", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 38, "datetime": "2018-08-24 06:30:55", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 37, "datetime": "2018-08-24 06:18:32", "status": "wating", "user": "admin", "info": "clean site cache : m.lifevc.com", "type": "m.lifevc.com", "jobsid": null}, {"id": 36, "datetime": "2018-08-24 06:18:25", "status": "wating", "user": "admin", "info": "clean site cache : m.lifevc.com", "type": "m.lifevc.com", "jobsid": null}, {"id": 35, "datetime": "2018-08-24 05:33:59", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 34, "datetime": "2018-08-24 05:29:43", "status": "wating", "user": "admin", "info": "clean site cache : account.lifevc.com", "type": "account.lifevc.com", "jobsid": null}, {"id": 33, "datetime": "2018-08-24 03:32:59", "status": "wating", "user": "admin", "info": "clean site cache : ", "type": "", "jobsid": null}, {"id": 32, "datetime": "2018-08-24 01:38:35", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 31, "datetime": "2018-08-24 01:38:30", "status": "wating", "user": "admin", "info": "clean site cache : ", "type": "", "jobsid": null}, {"id": 30, "datetime": "2018-08-23 10:11:13", "status": "wating", "user": "admin", "info": "clean site cache : ", "type": "", "jobsid": null}, {"id": 29, "datetime": "2018-08-23 09:07:15", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 28, "datetime": "2018-08-23 08:37:36", "status": "wating", "user": "admin", "info": "clean site cache : account.lifevc.com", "type": "account.lifevc.com", "jobsid": null}, {"id": 27, "datetime": "2018-08-23 08:36:59", "status": "wating", "user": "admin", "info": "clean site cache : ", "type": "", "jobsid": null}, {"id": 26, "datetime": "2018-08-23 08:24:47", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 25, "datetime": "2018-08-23 08:20:48", "status": "wating", "user": "admin", "info": "clean site cache : m.lifevc.com", "type": "m.lifevc.com", "jobsid": null}, {"id": 24, "datetime": "2018-08-23 08:20:45", "status": "wating", "user": "admin", "info": "clean site cache : app.lifevc.com", "type": "app.lifevc.com", "jobsid": null}, {"id": 23, "datetime": "2018-08-23 08:08:25", "status": "wating", "user": "admin", "info": "clean site cache : app.lifevc.com", "type": "app.lifevc.com", "jobsid": null}, {"id": 22, "datetime": "2018-08-23 08:08:09", "status": "wating", "user": "admin", "info": "clean site cache : app.lifevc.com", "type": "app.lifevc.com", "jobsid": null}, {"id": 21, "datetime": "2018-08-23 08:08:05", "status": "wating", "user": "admin", "info": "clean site cache : marketing.lifevc.com", "type": "marketing.lifevc.com", "jobsid": null}, {"id": 20, "datetime": "2018-08-23 08:08:02", "status": "wating", "user": "admin", "info": "clean site cache : account.lifevc.com", "type": "account.lifevc.com", "jobsid": null}, {"id": 19, "datetime": "2018-08-23 08:07:38", "status": "wating", "user": "admin", "info": "clean site cache : account.lifevc.com", "type": "account.lifevc.com", "jobsid": null}, {"id": 18, "datetime": "2018-08-23 08:07:22", "status": "wating", "user": "admin", "info": "clean site cache : marketing.lifevc.com", "type": "marketing.lifevc.com", "jobsid": null}, {"id": 17, "datetime": "2018-08-23 08:06:52", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 16, "datetime": "2018-08-23 08:06:33", "status": "wating", "user": "admin", "info": "clean site cache : www.lifevc.com", "type": "www.lifevc.com", "jobsid": null}, {"id": 15, "datetime": "2018-08-23 08:05:45", "status": "wating", "user": "admin", "info": "clean site cache : account", "type": "account", "jobsid": null}, {"id": 14, "datetime": "2018-08-23 08:05:39", "status": "wating", "user": "admin", "info": "clean site cache : account", "type": "account", "jobsid": null}, {"id": 13, "datetime": "2018-08-23 08:05:15", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 12, "datetime": "2018-08-23 08:04:53", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 11, "datetime": "2018-08-23 08:04:39", "status": "wating", "user": "admin", "info": "clean site cache : m", "type": "m", "jobsid": null}, {"id": 10, "datetime": "2018-08-23 08:04:13", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 9, "datetime": "2018-08-23 08:03:59", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 8, "datetime": "2018-08-23 08:01:20", "status": "wating", "user": "admin", "info": "clean site cache : m", "type": "m", "jobsid": null}, {"id": 7, "datetime": "2018-08-23 07:59:40", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 6, "datetime": "2018-08-23 07:51:05", "status": "wating", "user": "admin", "info": "clean site cache : account", "type": "account", "jobsid": null}, {"id": 5, "datetime": "2018-08-23 07:49:02", "status": "wating", "user": "admin", "info": "clean site cache : www", "type": "www", "jobsid": null}, {"id": 4, "datetime": "2018-08-21 06:32:03", "status": "error", "user": "admin", "info": "this jobs has error to stop", "type": "cleancahce", "jobsid": 1004}, {"id": 3, "datetime": "2018-08-21 06:31:58", "status": "running", "user": "admin", "info": "running this jobs now", "type": "cleancache", "jobsid": 1003}, {"id": 2, "datetime": "2018-08-21 06:31:55", "status": "wating", "user": "admin", "info": "jobs is wating to run", "type": "cleancache", "jobsid": 1002}, {"id": 1, "datetime": "2018-08-21 06:31:53", "status": "success", "user": "admin", "info": "this jobs is success", "type": "cleancache", "jobsid": 1001}]}}', content_type="application/json")
    #return HttpResponse('{"code":20000,"data":{"items":[{"id":"130000200812124267","title":"Bqqg zcieo puxqpr ouudls utgudu ohdsvrfiy qqccec dryqtv rbxnbnb pdxrqncax fwwpom ygsbdrrc kbrhd mkbhvim boqbbwy.","status":"draft","author":"name","display_time":"2002-08-06 03:27:42","pageviews":4682},{"id":"61000019940212276X","title":"Pqowz wcbjmfu sts ckokg mqkstubf hmcbmkbxc eer chwckofe lmqckklglv fwutngo ahkobf ftjdobo.","status":"draft","author":"name","display_time":"1970-02-23 01:59:57","pageviews":1678},{"id":"710000197011216907","title":"Fcxddnt ymvqgijwjx qed kuovyhks nazw ggjezmuv pchfwhot nbrwpyyo spvofhjjy ojvknweks lldvxket judyy jhtdqqg xkseogmgd fxwtvmwljg.","status":"published","author":"name","display_time":"1990-03-18 01:38:53","pageviews":1326},{"id":"450000201705254559","title":"Dhajxeu vyii pbaey shiko bslovqcx nvkgozkh tkqpi zfvuyqvmk hxounp rbjbbcpys.","status":"draft","author":"name","display_time":"2018-07-14 03:47:41","pageviews":2884},{"id":"150000201707134306","title":"Lyhkjiy cayynfhf ndvg mkjhyiwxe tpespce jbenntjby ospcs smw jytctxhoim kmblct tycrrvek cdtbfldize johdvmt xjnkv sqiyyp qzqjlbsw itiru.","status":"deleted","author":"name","display_time":"1974-02-02 20:30:53","pageviews":1811},{"id":"230000200002141691","title":"Hwhvbyuwqw qjxnuyh cgcfxw prkd qekta qdblyvxqnd tamuhubm kbundflw woidupyjq jbfpqgefg xkngqix spscxkry xfcnwf zfezrhn bxuoyx.","status":"deleted","author":"name","display_time":"1993-02-08 14:19:52","pageviews":807},{"id":"310000197901053682","title":"Uyx ivghp inclb myto ztoolg dnyxftv svphgxrj kgqfedzbl bvkzntsue ottw tcklwj bxobwe rborsve qahual.","status":"draft","author":"name","display_time":"1993-06-27 13:30:47","pageviews":2244},{"id":"340000200506165318","title":"Zmyixvp pirhkicx wrwk ohukqo kyscln kzu ymdhmo shl swxeotpgy rgbjkhcevx sepu bia pfyjg itxr hoees mmog royuv jex trqi.","status":"deleted","author":"name","display_time":"1989-06-24 09:13:58","pageviews":894},{"id":"360000201705135371","title":"Pisbeb yvlbiikb qsjoigacbt okpzb kiqtv lzdlwg bbowugjob ilrphwpxpc zqnktejgc gnvhvji pckj pemvxwsjb dnixlqe hvanbvmbkm.","status":"published","author":"name","display_time":"2000-07-23 03:15:11","pageviews":4459},{"id":"310000199207251223","title":"Nxjibfi nzqghpys rjjk hodm dhesbnttw qesobypnv vixxtiv tmqfh nurjpptkm ukfovbn blh osbnsokp oorl lyspedilt dvrku halffs.","status":"draft","author":"name","display_time":"1982-11-13 16:13:25","pageviews":1003},{"id":"650000200007013398","title":"Dxph jol zcdtoljdo mjyaq vmanoseq dkrdnm srkfo vrpgbs leqk fyhw pkf ubutugkkie yinwkebgsx lqtpxgv pxjlidx tqlfn pqhndau vhdc aghtftui.","status":"draft","author":"name","display_time":"1973-01-23 01:05:42","pageviews":2404},{"id":"410000197710316252","title":"Ujoqg ofyc zlktbk mqmh ecul rrfvopg flngwbunx muwhdero ertnysjdlo utp.","status":"published","author":"name","display_time":"2009-04-15 15:14:11","pageviews":2187},{"id":"340000200006043381","title":"Iorqjmi chtlbrhel hpppsmnzeb osis itqgxf wpc wuc cnvi dtmr oghwgyhkqi kjrhitttju.","status":"draft","author":"name","display_time":"1992-04-16 20:23:53","pageviews":4472},{"id":"420000198309177512","title":"Qjiqofhg kdjyqwdf fwclbwm hfac lcqcxbkd bvftiw umyn vam kpgll fkopqlcw.","status":"draft","author":"name","display_time":"2003-02-28 04:44:12","pageviews":1040},{"id":"350000197110134336","title":"Rjtnnu bbl ivtffpmo hewyi itufsia msfnfrhc zqcedgcf jluv dxmc uhf yfzj yssv yrnmqad ffhd jptdvxed fkoor yquj tsffetjld qjtgloa.","status":"draft","author":"name","display_time":"1982-08-22 02:34:07","pageviews":4150},{"id":"460000200703158712","title":"Fou qomp ggcfd hvdhl krdtcxd vfhqx vliuvwit rjjxhqwtc fipy ydlvyvrbks.","status":"published","author":"name","display_time":"2015-07-08 05:03:43","pageviews":2362},{"id":"230000198412182955","title":"Wxvopu wtagadnwf syj ylxzk yvlgar maqribo oxq eshd snxtjfzbp mjft jikbprah nuetu.","status":"deleted","author":"name","display_time":"2010-04-08 01:31:28","pageviews":2398},{"id":"810000199506041734","title":"Yyerdg kmxuya dokenbcs ouructy jbsku htkilwr esssmin wqxlyx vmvexsi hyegkixnu peu btvpmmcg.","status":"published","author":"name","display_time":"2006-06-24 11:58:14","pageviews":3843},{"id":"510000200802181621","title":"Kuudgc tsfb btmqiyjpv pwvdcdsrd nbybtie gtsyeet wbbxghz drwzexkm wjqrodru hile yrridyiy pvdwphljc.","status":"draft","author":"name","display_time":"1999-08-11 19:25:50","pageviews":3186},{"id":"630000200611054168","title":"Gmihl drqnorwki yrjn vktlo idj qznhmk mgnyheya nstnf shul yfirursd guij srmrhy dwejeel mafmvhyq cnedafyqnq.","status":"draft","author":"name","display_time":"1978-12-13 01:28:27","pageviews":1609},{"id":"330000200205195132","title":"Ttju ripptr sbkohj qqrrsu dytpqq qpwtot ruuusrrj bxit uvzuyz vfuncdwtvy oecwgkgh nduqlwplsn yrevno vtd jmxwvassh htup.","status":"deleted","author":"name","display_time":"1974-12-14 12:31:55","pageviews":2663},{"id":"130000197106034534","title":"Icgqeyqsh etmlvmsk yavbo gqsmstocn urorok hqtde kmcfbytbe blgvzqbdh pasb khesx johekgrf dvoea biyhyuf xxr lcstixq.","status":"deleted","author":"name","display_time":"1977-09-18 16:36:14","pageviews":4616},{"id":"310000197307142105","title":"Dtlgdpg kqmjnvymd vpmqkgc iuvtpizz nmz jqdwdf ldoyelcuo bxvxqat tgvcfyt nglyyb wiq tvyglotc.","status":"deleted","author":"name","display_time":"2014-10-11 09:50:32","pageviews":3752},{"id":"110000197308291893","title":"Bucbi ypi quiorx alvpd ozrdwi qoqeasq bkzool ykiv gecj svwqg tdjv qqdqpp jmcep gtqugvlrwf.","status":"draft","author":"name","display_time":"1993-11-13 10:25:48","pageviews":1062},{"id":"320000198204074396","title":"Pbtg nclh vsdrkfai jcbo yykwgaamw stxnnonay cqpkkvn dluwm rmyfc xvpf iduspxfhh jmumtu.","status":"published","author":"name","display_time":"2007-10-18 16:20:02","pageviews":780},{"id":"460000200102234353","title":"Iyuibyn acnc klgp uaclwgo ahbgtrj liexwscxt yexjs hbtvroy yldkvbdf bbgsv lyly jzcygyi.","status":"published","author":"name","display_time":"1987-12-27 12:58:15","pageviews":2222},{"id":"610000197005134776","title":"Sjvvkqr qbcfgyr ucdnxj rflw wkdyfopcl dpzh quny ssclgppyt gbrj vjhur wzxr yoqqpwqk tuqcyopiix ivuyp wgjsfj ombu.","status":"draft","author":"name","display_time":"1991-05-07 13:11:32","pageviews":4695},{"id":"420000199511064743","title":"Onilcp ncru pjzaxtwc nzlb dofuh rwqwvfnyd unmkgju xpnny qrm dpndr muzki mxfv dxibfcqr uffemhyyu ufmksu ckxnnnwow abdhobr cqivxkbz nsn eqerqbty.","status":"draft","author":"name","display_time":"1998-01-07 17:55:27","pageviews":2365},{"id":"230000197204222647","title":"Tsumtb ngpw cvrhh twsex bkqfdbafq yvxmlv wbeb qmbkrg shnr kvjgnss offxmje yikch kdlgvyge qpoyhwe hajs rebluljk smsh tsfcug ccodnjgo.","status":"draft","author":"name","display_time":"1989-01-21 18:58:57","pageviews":779},{"id":"360000198102104555","title":"Ijjvcw rosknp qmbr codaynfnfi gqjzrlch wwycd uajufhc glkgl jpc trfnojrwc tdupmdxs bmnm fkrnauddw cslnvqyrhy hvyg wvpqhn elnsnjtbg hvtn.","status":"draft","author":"name","display_time":"1998-05-24 14:14:07","pageviews":2726}]}}', content_type="application/json")

def singleCleanCache(request):
    # 打开数据库连接
    print(request.body)
    request_dict = json.loads(request.read())

    # 数据库的名称
    dbname = "ops_logs"
    # 插入的数据
    data_dict = {
        "status": 'Wating',
        "user": 'admin',
        "info": 'clean site cache : ' + request_dict['server'],
        "type": 'singleCleanCache',
    }

    result = insert_data(dbname, data_dict)
    print(result)

    jsonData = []
    js_root = {}
    js_secondary = {}

    # jsonData.append(request_dict['server'])
    # js_secondary['items'] = jsonData
    js_root['code'] = 20000
    js_root['message'] = 'success'
    # js_root['data'] = js_secondary

    return HttpResponse(json.dumps(js_root), content_type="application/json")

def muiltCleanCache(request):
    # 打开数据库连接
    print(request.body)
    request_dict = json.loads(request.read())

    # 数据库的名称
    dbname = "ops_logs"
    # 插入的数据
    data_dict = {
        "status": 'Wating',
        "user": 'admin',
        "info": 'clean muilt site cache : ' + ','.join(request_dict['servers']),
        "type": 'muiltCleanCache',
    }

    result = insert_data(dbname, data_dict)
    print(result)

    js_root = {}
    #js_secondary = {}
    #js_secondary['items'] = jsonData
    js_root['code'] = 20000
    js_root['message'] = 'success'
    #js_root['data'] = js_secondary

    xx = request.POST.get("type")
    print(xx)
    return HttpResponse(json.dumps(js_root), content_type="application/json")


def insert_data(dbname,data_dict):

    try:

        data_values = "(" + "%s," * (len(data_dict)) + ")"
        data_values = data_values.replace(',)', ')')

        dbfield = data_dict.keys()
        datatuple = tuple(data_dict.values())
        dbfield = str(tuple(dbfield)).replace("'", '')
        conn = pymysql.connect(host="localhost", user="root", passwd="123.com", db="ops", charset="utf8")
        cursor = conn.cursor()
        sql = """ insert into %s %s values %s """ % (dbname,dbfield,data_values)
        params = datatuple
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()

        print("=====  插入成功  =====")
        return 1

    except Exception as e:
        print("********  插入失败    ********")
        print(e)
        return 0
