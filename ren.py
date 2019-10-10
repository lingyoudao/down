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
		#if i>=2*pages:
		#	break
	fd2.close()
	fd2ok.close()
	os.system('reok.bat') #调用系统批处理
	return() 
	
file_rename()