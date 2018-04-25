from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User, Group
from django.utils import timezone
from django.http import HttpResponse

import MySQLdb
import datetime
# Create your views here.

class book:
	bno = ""
	category = ""
	title = ""
	publisher = ""
	year = 0
	author = ""
	price = 0.00
	total = 0
	stock = 0
	borrowtime = ""
	deadline = ""
	status = ""

class ncard:
	cno = 0
	name = ""
	dept = ""
	ty = ""

db = MySQLdb.connect("localhost", "root", "1997lk421", "Library", charset='utf8')
cursor = db.cursor()
manager = 0

def index(request):
	return render(request,'index.html')

def login(request):
	if 'username' in request.POST:
		userid = request.POST['username']
		sql = "select sec from Manager where mid = \""+userid+"\";"
		rescount = cursor.execute(sql)
		if rescount == 0:
			return HttpResponse('<script>alert("该管理员不存在！");location.replace("/");</script>')
		else:
			ps = cursor.fetchone()
			userps = request.POST['password']
			if ps[0] != userps:
				return HttpResponse('<script>alert("密码错误！");location.replace("/");</script>')
			else:
				global manager 
				manager = userid
				print(manager)
				return HttpResponse('<script>alert("登陆成功！");location.replace("/main/");</script>')
	else :
		return HttpResponse('<script>alert("请输入管理员id！");location.replace("/");</script>')

def main(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	
	sql = "select name from Manager where mid = "+manager+";"
	cursor.execute(sql)
	name = cursor.fetchone()

	return render(request,'main.html',{'name':name[0]})

def insertone(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	
	if 'bno' in request.POST:
		bno = request.POST['bno']
		sql = "select * from Book where bno = \""+bno+"\""
		rescount = cursor.execute(sql)
		if rescount != 0:
			return HttpResponse('<script>alert("该书号已存在！");location.replace("/main/");</script>')
	else:
		return HttpResponse('<script>alert("请输入书号！");location.replace("/main/");</script>')

	if 'category' not in request.POST:
		return HttpResponse('<script>alert("请输入类型！");location.replace("/main/");</script>')
	else:
		category = request.POST['category']
	
	if 'title' not in request.POST:
		return HttpResponse('<script>alert("请输入书名！");location.replace("/main/");</script>')
	else:
		title = request.POST['title']

	if 'publisher' not in request.POST:
		return HttpResponse('<script>alert("请输入出版商！");location.replace("/main/");</script>')
	else:
		publisher = request.POST['publisher']

	if 'year' not in request.POST:
		return HttpResponse('<script>alert("请输入年份！");location.replace("/main/");</script>')
	else:
		year = request.POST['year']

	if 'author' not in request.POST:
		return HttpResponse('<script>alert("请输入年份！");location.replace("/main/");</script>')
	else:
		author = request.POST['author']

	if 'price' not in request.POST:
		return HttpResponse('<script>alert("请输入价格！");location.replace("/main/");</script>')
	else:
		price = request.POST['price']

	if 'total' not in request.POST:
		return HttpResponse('<script>alert("请输入总量！");location.replace("/main/");</script>')
	else:
		total = request.POST['total']

	sql = "insert into Book values('"+bno+"','"+category+"','"+title+"','"+publisher+"',"+year+",'"+author+"',"+price+","+total+","+total+");"
	print(sql)
	cursor.execute(sql)
	db.commit()
	return HttpResponse('<script>alert("入库成功！");location.replace("/main/");</script>')

def insertfile(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	myFile =request.FILES.get("myfile", None)
	if not myFile:  
		return HttpResponse('<script>alert("没有上传文件！");location.replace("/main/");</script>')
	for index,line in enumerate(myFile.readlines()):
		sline = str(line,encoding='utf-8')
		sline = sline.strip('\n')
		ss = sline.split(' ')
		for s in ss:
			if s == "":
				error = "<script>alert(\"第"+str(index)+"行数据不全\");location.replace(\"/main/\");</script>"
				return HttpResponse(error)
		sql = "insert into Book values('"+ss[0]+"','"+ss[1]+"','"+ss[2]+"','"+ss[3]+"',"+ss[4]+",'"+ss[5]+"',"+ss[6]+","+ss[7]+","+ss[7]+");"
		cursor.execute(sql)
	db.commit()
	return HttpResponse('<script>alert("入库成功！");location.replace("/main/");</script>')

def search(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	if request.method == 'GET':

		sql = "select * from Book order by title;"
		cursor.execute(sql)
		rangename = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangename.append(newb)
		print(rangename)

		sql = "select * from Book order by year;"
		cursor.execute(sql)
		rangeyear = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangeyear.append(newb)
		print(rangeyear)

		sql = "select * from Book order by price;"
		cursor.execute(sql)
		rangeprice = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangeprice.append(newb)
		print(rangeprice)

		sql = "select * from Book order by stock;"
		cursor.execute(sql)
		rangestock = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangestock.append(newb)
		print(rangestock)

		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()

		return render(request,'search.html',{'name':name[0],'rangename':rangename, 'rangeyear':rangeyear, 'rangeprice':rangeprice, 'rangestock':rangestock})

	else:
		sql1 = "select * from Book "
		sql2 = "order by title "
		sql3 = ""
		tigger = 0

		if 'category' in request.POST:
			category = request.POST['category']
			if category != "":
				sql3 = sql3 + "where category = \"" + category + "\" "
				tigger = 1

		if 'title' in request.POST:
			title = request.POST['title']
			if title != "":
				if tigger == 0:
					sql3 = sql3 + "where title = \"" + title + "\" "
					tigger = 1
				else:
					sql3 = sql3 + "and title = \"" + title + "\" "

		if 'publisher' in request.POST:
			publisher = request.POST['publisher']
			if publisher != "":
				if tigger == 0:
					sql3 = sql3 + "where publisher = \"" + publisher + "\" "
					tigger = 1
				else:
					sql3 = sql3 + "and publisher = \"" + publisher + "\" "

		if 'startyear' in request.POST:
			startyear = request.POST['startyear']
			if startyear != "":
				if tigger == 0:
					sql3 = sql3 + "where year >= " + startyear + " "
					tigger = 1
				else:
					sql3 = sql3 + "and year >= " + startyear + " "

		if 'endyear' in request.POST:
			endyear = request.POST['endyear']
			if endyear != "":
				if tigger == 0:
					sql3 = sql3 + "where year <= " + endyear + " "
					tigger = 1
				else:
					sql3 = sql3 + "and year <= " + endyear + " "

		if 'author' in request.POST:
			author = request.POST['author']
			if author != "":
				if tigger == 0:
					sql3 = sql3 + "where author = \"" + author + "\" "
					tigger = 1
				else:
					sql3 = sql3 + "and author = \"" + author + "\" "

		if 'startprice' in request.POST:
			startprice = request.POST['startprice']
			if startprice != "":
				if tigger == 0:
					sql3 = sql3 + "where price >= " + startprice + " "
					tigger = 1
				else:
					sql3 = sql3 + "and price >= " + startprice + " "

		if 'endprice' in request.POST:
			endprice = request.POST['endprice']
			if endprice != "":
				if tigger == 0:
					sql3 = sql3 + "where price <= " + endprice + " "
					tigger = 1
				else:
					sql3 = sql3 + "and price <= " + endprice + " "

		sql = sql1 + sql3 + sql2 + ";"
		print(sql)
		cursor.execute(sql)
		rangename = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangename.append(newb)

		sql2 = "order by year "
		sql = sql1 + sql3 + sql2 + ";"
		print(sql)
		cursor.execute(sql)
		rangeyear = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangeyear.append(newb)

		sql2 = "order by price "
		sql = sql1 + sql3 + sql2 + ";"
		print(sql)
		cursor.execute(sql)
		rangeprice = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangeprice.append(newb)

		sql2 = "order by stock"
		sql = sql1 + sql3 + sql2 + ";"
		print(sql)
		cursor.execute(sql)
		rangestock = []
		rows = cursor.fetchall()
		for index,row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[1]
			newb.title = row[2]
			newb.publisher = row[3]
			newb.year = row[4]
			newb.author = row[5]
			newb.price = row[6]
			newb.total = row[7]
			newb.stock = row[8]
			rangestock.append(newb)

		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()

		return render(request,'search.html',{'name':name[0],'rangename':rangename, 'rangeyear':rangeyear, 'rangeprice':rangeprice, 'rangestock':rangestock})

def borrow(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	if request.method == 'GET':
		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()
		return render(request, 'borrow.html', {'name':name[0],'ok':0})
	else:
		if 'cno' in request.POST:
			cno = request.POST['cno']
		else:
			return HttpResponse('<script>alert("请输入借书证号！");location.replace("/borrow/");</script>')

		sql = "select * from Record natural join Book where cno = "+cno+" order by borrow_time desc;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		borrowlist = []
		for index, row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[6]
			newb.title = row[7]
			newb.publisher = row[8]
			newb.year = row[9]
			newb.author = row[10]
			newb.price = row[11]
			newb.borrowtime = row[2]
			newb.deadline = row[5]
			if row[3] == None:
				newb.status = "未归还"
			else:
				newb.status = "已归还"
			borrowlist.append(newb)

		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()

		return render(request,'borrow.html',{'name':name[0],'ok':1,'borrowlist':borrowlist})

def borrowone(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')

	if 'cno' not in request.POST:
		return HttpResponse('<script>alert("请输入借书证号！");location.replace("/borrow/");</script>')
	else:
		cno = request.POST['cno']

	if 'bno' not in request.POST:
		return HttpResponse('<script>alert("请输入书号！");location.replace("/borrow/");</script>')
	else:
		bno = request.POST['bno']
	sql = "select stock from Book where bno = '"+bno+"';"
	rescount = cursor.execute(sql)
	if rescount == 0:
		return HttpResponse('<script>alert("该书不存在！");location.replace("/borrow/");</script>')
	row = cursor.fetchone()
	if row[0] == 0:
		sql = "select deadline from Record where bno = '" + bno + "' order by deadline desc;"
		cursor.execute(sql)
		res = cursor.fetchone()
		ans = "<script>alert(\"没有库存了！最早归还时间是:"+str(res[0])+"\");location.replace(\"/borrow/\");</script>"
		print(ans)
		return HttpResponse(ans)

	sql = "select * from Card where cno = "+str(cno)+";"
	rescount = cursor.execute(sql)
	if rescount == 0:
		return HttpResponse('<script>alert("该借书证不存在！");location.replace("/borrow/");</script>')

	w = datetime.datetime.now()
	print(w)
	y = w + datetime.timedelta(days = 60)

	sw = str(w)

	ww = sw.split('.')
	sy = str(y)
	yy = sy.split('.')

	sql = "insert into Record(cno,bno,borrow_time,mid,deadline) values("+cno+",'"+bno+"','"+ww[0]+"',"+manager+",'"+yy[0]+"');"
	print(sql)
	cursor.execute(sql)
	db.commit()

	sql = "update Book set stock = stock - 1 where bno = '"+bno+"';"
	cursor.execute(sql)
	db.commit()

	return HttpResponse('<script>alert("借书成功！");location.replace("/borrow/");</script>')

def returnn(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')
	if request.method == 'GET':
		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()
		return render(request, 'return.html', {'name':name[0],'ok':0})
	else:
		if 'cno' in request.POST:
			cno = request.POST['cno']
		else:
			return HttpResponse('<script>alert("请输入借书证号！");location.replace("/return/");</script>')

		sql = "select * from Record natural join Book where cno = "+cno+" order by borrow_time desc;"
		cursor.execute(sql)
		rows = cursor.fetchall()
		borrowlist = []
		for index, row in enumerate(rows):
			if index == 51:
				break
			newb = book()
			newb.bno = row[0]
			newb.category = row[6]
			newb.title = row[7]
			newb.publisher = row[8]
			newb.year = row[9]
			newb.author = row[10]
			newb.price = row[11]
			newb.borrowtime = row[2]
			newb.deadline = row[5]
			if row[3] == None:
				newb.status = "未归还"
			else:
				newb.status = "已归还"
			borrowlist.append(newb)

		sql = "select name from Manager where mid = "+manager+";"
		cursor.execute(sql)
		name = cursor.fetchone()
		return render(request,'return.html',{'name':name[0],'ok':1,'borrowlist':borrowlist})

def returnone(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')

	if 'cno' not in request.POST:
		return HttpResponse('<script>alert("请输入借书证号！");location.replace("/return/");</script>')
	else:
		cno = request.POST['cno']

	if 'bno' not in request.POST:
		return HttpResponse('<script>alert("请输入书号！");location.replace("/return/");</script>')
	else:
		bno = request.POST['bno']

	sql = "select * from Record where bno = '" + bno + "' and cno = " + cno + ";"
	rescount = cursor.execute(sql)
	if rescount == 0:
		return HttpResponse('<script>alert("没有对应的借书记录！");location.replace("/return/");</script>')
	rows = cursor.fetchone()
	borrowtime = rows[2]

	w = datetime.datetime.now()
	sw = str(w)
	ww = sw.split('.')

	sql = "update Record set return_time = '" + ww[0] + "' where bno = '"+bno+"' and cno = "+cno+" and borrow_time = '"+str(borrowtime)+"';"
	cursor.execute(sql)
	db.commit()

	sql = "update Book set stock = stock + 1 where bno = '"+bno+"';"
	cursor.execute(sql)
	db.commit()

	return HttpResponse('<script>alert("还书成功！");location.replace("/return/");</script>')

def card(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')

	sql = "select cno from Card order by cno desc;"
	cursor.execute(sql)
	row = cursor.fetchone()

	sql = "select * from Card;"
	cursor.execute(sql)
	rows = cursor.fetchall()
	cardlist = []
	maxnum = 0
	for row in rows:
		newc = ncard()
		newc.cno = row[0]
		if row[0] > maxnum:
			maxnum = row[0]
		newc.name = row[1]
		newc.dept = row[2]
		newc.ty = row[3]
		cardlist.append(newc)


	sql = "select name from Manager where mid = "+manager+";"
	cursor.execute(sql)
	name = cursor.fetchone()
	return render(request,'card.html',{'name':name[0],'newest':maxnum,'cardlist':cardlist})

def addcard(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')

	if 'cno' not in request.POST:
		return HttpResponse('<script>alert("请输入借书证号！");location.replace("/card/");</script>')		
	else:
		cno = request.POST['cno']
		sql = "select * from Card where cno = "+cno+";"
		rescount = cursor.execute(sql)
		if rescount > 0 or int(cno) < 0:
			return HttpResponse('<script>alert("借书证号已存在或小于零！");location.replace("/card/");</script>')

	if 'name' not in request.POST:
		return HttpResponse('<script>alert("请输入姓名！");location.replace("/card/");</script>')
	else:
		name = request.POST['name']

	if 'dept' not in request.POST:
		return HttpResponse('<script>alert("请输入单位！");location.replace("/card/");</script>')
	else:
		dept = request.POST['dept']

	if 'type' not in request.POST:
		return HttpResponse('<script>alert("请输入种类！");location.replace("/card/");</script>')		
	else:
		ty = request.POST['type']
		if ty != 'T' and ty != 'S':
			return HttpResponse('<script>alert("错误的种类！");location.replace("/card/");</script>')

	sql = "insert into Card values("+cno+",'"+name+"','"+dept+"','"+ty+"');"
	cursor.execute(sql);
	db.commit()
	return HttpResponse('<script>alert("添加成功！");location.replace("/card/");</script>')


def deletecard(request):
	if manager == 0:
		return HttpResponse('<script>alert("请登录！");location.replace("/");</script>')

	if 'cno' not in request.POST:
		return HttpResponse('<script>alert("请输入借书证号！");location.replace("/card/");</script>')		
	else:
		cno = request.POST['cno']
		sql = "select * from Card where cno = "+cno+";"
		rescount = cursor.execute(sql)
		if rescount <= 0:
			return HttpResponse('<script>alert("借书证不存在！");location.replace("/card/");</script>')

	sql = "delete from Card where cno = "+cno+";"
	cursor.execute(sql)
	db.commit()
	return HttpResponse('<script>alert("删除成功！");location.replace("/card/");</script>')

def logout(request):
	manager = 0
	return HttpResponse('<script>alert("退出！");location.replace("/");</script>')
		
