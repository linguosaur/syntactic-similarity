import codecs, sys

katakana2romaji = {'\xE3\x82\xA2':'a', '\xE3\x82\xA4':'i', '\xE3\x82\xA6':'u', '\xE3\x82\xA8':'e', '\xE3\x82\xAA':'o',
		 '\xE3\x82\xAB':'ka', '\xE3\x82\xAD':'ki', '\xE3\x82\xAF':'ku', '\xE3\x82\xB1':'ke', '\xE3\x82\xB3':'ko',
		 '\xE3\x82\xB5':'sa', '\xE3\x82\xB7':'shi', '\xE3\x82\xB9':'su', '\xE3\x82\xBB':'se', '\xE3\x82\xBD':'so',
		 '\xE3\x82\xBF':'ta', '\xE3\x83\x81':'chi', '\xE3\x83\x84':'tsu', '\xE3\x83\x86':'te', '\xE3\x83\x88':'to',
		 '\xE3\x83\x8A':'na', '\xE3\x83\x8B':'ni', '\xE3\x83\x8C':'nu', '\xE3\x83\x8D':'ne', '\xE3\x83\x8E':'no',
		 '\xE3\x83\x8F':'ha', '\xE3\x83\x92':'hi', '\xE3\x83\x95':'fu', '\xE3\x83\x98':'he', '\xE3\x83\x9B':'ho',
		 '\xE3\x83\x9E':'ma', '\xE3\x83\x9F':'mi', '\xE3\x83\xA0':'mu', '\xE3\x83\xA1':'me', '\xE3\x83\xA2':'mo',
		 '\xE3\x83\xA4':'ya', '\xE3\x83\xA6':'yu', '\xE3\x83\xA8':'yo',
		 '\xE3\x83\xA9':'ra', '\xE3\x83\xAA':'ri', '\xE3\x83\xAB':'ru', '\xE3\x83\xAC':'re', '\xE3\x83\xAD':'ro',
		 '\xE3\x83\xAF':'wa', '\xE3\x83\xB0':'wi', '\xE3\x83\xB1':'we', '\xE3\x83\xB2':'wo',
		 '\xE3\x83\xB3':'n',
		 '\xE3\x83\xB4':'vu',
		 '\xE3\x82\xAC':'ga', '\xE3\x82\xAE':'gi', '\xE3\x82\xB0':'gu', '\xE3\x82\xB2':'ge', '\xE3\x82\xB4':'go',
		 '\xE3\x82\xB6':'za', '\xE3\x82\xB8':'ji', '\xE3\x82\xBA':'zu', '\xE3\x82\xBC':'ze', '\xE3\x82\xBE':'zo',
		 '\xE3\x83\x80':'da', '\xE3\x83\x82':'ji', '\xE3\x83\x85':'zu', '\xE3\x83\x87':'de', '\xE3\x83\x89':'do',
		 '\xE3\x83\x90':'ba', '\xE3\x83\x93':'bi', '\xE3\x83\x96':'bu', '\xE3\x83\x99':'be', '\xE3\x83\x9C':'bo',
		 '\xE3\x83\x91':'pa', '\xE3\x83\x94':'pi', '\xE3\x83\x97':'pu', '\xE3\x83\x9A':'pe', '\xE3\x83\x9D':'po',
		 '\xE3\x83\xB7':'va', '\xE3\x83\xB8':'vi', '\xE3\x83\xB9':'ve', '\xE3\x83\xBA':'vo',
		 '\xE3\x83\xA3':'Sya', '\xE3\x83\xA5':'Syu', '\xE3\x83\xA7':'Syo', # S = small
		 '\xE3\x83\xBC':'L', '\xE3\x83\xBD':'D', '\xE3\x83\xBE':'V', # L = long vowel, D = duplicate, V = vowel duplicsate
		 '\xE3\x82\xA1':'Sa', '\xE3\x82\xA3':'Si', '\xE3\x82\xA5':'Su', '\xE3\x82\xA7':'Se', '\xE3\x82\xA9':'So',
		 '\xE3\x83\x83':'G', '\xE3\x83\xAE':'Swa'} # G = geminate
jpnpunc2engpunc = {"\xE3\x80\x81":',', "\xE3\x80\x82":'.', "\xEF\xBC\x88":'(', "\xEF\xBC\x89":')', "\xE3\x80\x8C":'"', "\xE3\x80\x8D":'"', "\xE3\x80\x8E":'"', "\xE3\x80\x8F":'"', "\xEF\xBC\x9D":'=', "\xE2\x97\x8F":'*', "\xE2\x80\xA6":'...', "\xE2\x89\xAA":'"', "\xE2\x89\xAB":'"', "\xE3\x83\xBB":'*', "\xE3\x80\x9C":'~', "\xE3\x80\x90":'<', "\xE3\x80\x91":'>', "\xEF\xBC\x9F":'?', "\xEF\xBC\x81":'!', "\xEF\xBC\x9A":':', "\xEF\xBC\x9B":';', "\xE2\x80\x9C":'"', "\xE2\x80\x9D":'"', "\xEF\xBC\x8F":'/'}
poslist = []
posdict = {}

posfile = codecs.open(sys.argv[1], 'r', 'utf-8')
for line in posfile:
	splitline = line.strip().split('\t')
	if len(splitline) > 4:
		if splitline[1] != '': katakana = splitline[1]
		else: katakana = splitline[0]
		if len(katakana.split('/')) > 1: katakana = katakana.split('/')[0]
		romaji = ''
		for kana in katakana:
			if kana.encode('utf-8') in katakana2romaji:
				romaji += katakana2romaji[kana.encode('utf-8')]
			elif kana.encode('utf-8') in jpnpunc2engpunc: romaji += jpnpunc2engpunc[kana.encode('utf-8')]
			elif kana == '}': continue
			elif len(repr(kana)) <= 4: romaji += kana # u'h' -> length = 4
			else: 
				romaji += 'UNK'
		origPOS = splitline[3]
		if origPOS not in poslist: poslist.append(origPOS)
		newPOS = poslist.index(origPOS)
		if romaji not in posdict: posdict[romaji] = set(repr(newPOS))
		else: posdict[romaji].add(repr(newPOS))

for romaji, posset in posdict.iteritems():
	print romaji, '\t', ', '.join(posset)
