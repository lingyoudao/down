# coding=gbk
from tkinter import *
import base64
import urllib.request
import requests 
import re
import wget
import os

#/��������
root = Tk()
root.title("������Դ������")
root.geometry('500x300')
root.resizable(0,0)

L1 = Label(root,text="������������ַ�����¸�ʽ������ҳ��")
L1.pack(side=TOP)

e1 = Entry(root, width=200)
e1.pack(padx=10, pady=10)
e1.delete(0,END)
e1.insert(0,"https://ksfan.net/story/kai-shu-feng-shen-yan-yi/?page=")

L2 = Label(root,text="��������ʼҳ")
L2.pack(padx=10, pady=10)

e2 = Entry(root)
e2.pack(padx=10, pady=10)
e2.delete(0,END)
e2.insert(0,"��������ʼҳ")

L3 = Label(root,text="���������ҳ")
L3.pack(padx=10, pady=10)

e3 = Entry(root)
e3.pack(padx=20, pady=20)
e3.delete(0,END)
e3.insert(0,"���������ҳ")

#/��ȡ�����URL
def txt_url():
	url = e1.get()
	p1 = int(e2.get())
	p2 = int(e3.get())
	global pages 
	pages = p2 - p1 #ȫ�ֱ������� ȷ����ҳ��
	p = p1
	while p<p2:   #�������ҳ��
		req = requests.get(url+str(p))
		r1 = re.findall (r"<h5>(.*?)</h5>",req.text)
		r2 = re.findall (r"new Audio(.*?);",req.text)
		with open('kaishu.txt', 'a', encoding='utf-8') as f:  #����url���ļ���������ļ�
			f.write(str(r2)+'\n')
			f.write(str(r1)+'\n')
		p = p+1
	f.close()
	return

#/������ʽת��
def txt_replace(): 
	fd = open("kaishu.txt", encoding='utf-8')
	lines = fd.readlines()
	fd. close()
	for line in lines:
		rs = line.replace('\']','').replace('[\'','').replace(r"""["('/xaud/""",'').replace(r"""%3D')"]""",'=')
		rsend = rs
		newfd = open("kaishuzhengze.txt",'a', encoding='utf-8')
		newfd.write(rsend)
		newfd.close()
	return

#/bash64����
def txt_base64(): 
	f1 = open(r'kaishuzhengze.txt','rb') #������Ҫbase64ת����ļ���
	f2 = open(r'kaishuzhengze64.txt','ab') #������Ҫ�����ת�����ļ���
	i=0
	while True:
		line = f1.readline()
		if i % 2 != 0:
			f2.write(line)
		else:
			bs = base64.b64decode(line)
			f2.write(bs)
			str = '\r\n'
			f2.write(str.encode())
		i+=1
		if i>2 * pages:         #����������
			break
	return

#/�����ļ�
def file_wget():
	wg1 = open(r'kaishuzhengze64.txt','r',encoding='utf-8')
	lines = wg1.readlines()
	i=0
	for line in lines:
		i += 1
		if i % 2 != 0:
			urlw = line.strip('\n')
			wget.download(urlw)
		if i >= 2*pages:
			break
	wg1.close()
	return()

#/�������ļ�
def file_rename():
	fd1 = open("kaishuzhengze64.txt",'r', encoding='utf-8')
	lines = fd1.readlines()
	fd1. close()
	for line in lines:
		rs = line.replace(r"""https://cdn.kaishuhezi.com/kstory/story/audio/""",'')
		rsend = rs
		newfd = open("rensim.txt",'a', encoding="utf-8")
		newfd.write(rsend)
		newfd.close()

	fd2 = open("rensim.txt", 'r',encoding='utf-8')
	fd2ok = open("reok.bat", 'w', encoding='utf-8')
	lines = fd2.readlines()
	i = 0
	for line in lines:
		i += 1
		if i % 2 != 0:
			fd2ok.write('ren '+ line.strip('\n')+'  ')
		else:
			fd2ok.write(line.replace(' ', '').strip('\n') +'.mp3'+'\n')
		if i>=2*pages:
			break
	fd2.close()
	fd2ok.close()
	os.system('reok.bat') #����ϵͳ������
	return() 

# def remove_file():
        

def download():
	txt_url()
	txt_replace()
	txt_base64()
	file_wget()
	file_rename()
	return()
def delfile():
	os.remove("kaishu.txt")
	os.remove("kaishuzhengze.txt")
	os.remove("kaishuzhengze64.txt")
	os.remove("rensim.txt")
	os.remove("reok.bat")
	return()
    
Button(root, text="ɾ�������ļ�", width=10, command=delfile).pack(side=BOTTOM)

Button(root, text="����", width=10, command=download).pack(side=BOTTOM)

root.mainloop()

