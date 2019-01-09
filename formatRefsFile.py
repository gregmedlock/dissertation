# Clean up references for biblatex (remove URLs, etc.)

import sys

fileName = sys.argv[1]

file = open(fileName,'r')
file2 = open('rf_' + fileName,'w')
for line in file:
	if line.find('language = "') == -1: # and \
		#line.find('issn = ') == -1 and \
		#line.find('keywords = {') == -1 and \
		#line.find('abstract = {') == -1 and \
		#line.find('isbn = {') == -1 and \
		#line.find('file = {') == -1 and \
		#ine.find('METHODS:') == -1 and \
		#line.find('CONCLUSION') == -1 and \
		#line.find('RESULTS:') == -1 and \
		#line.find('AVAILABILITY:') == -1 and \
		#line.find('CONTACT:') == -1 and \
		#line.find('DESIGN, SETTING, AND PARTICIPANTS:') == -1 and \
		#line.find('MAIN OUTCOME MEASURES:') == -1 and \
		#line.find('OBJECTIVE:') == -1 and \
		#line.find('METHODOLOGY/PRINCIPAL FINDINGS:') == -1 and \
		#line.find('CONCLUSIONS/SIGNIFICANCE:') == -1 and \
		#line.find('SUPPLEMENTARY INFORMATION:') == -1 and \
	#	len(line) > 0:
		print(line)
		line = line.replace(u"\u2010", u"\u002D")
		file2.write(line)

file.close()
file2.close()
