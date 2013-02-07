#!/usr/bin/python
import random
from sys import argv
def binary_word(p, n):
	word = ""
	for i in range(n):
		act = random.uniform(0, 1.0)
		if act >= 0 and act < p:
			word += "1"
		else:
			word += "0"
			
	return word
	
def channel(q01, q10, word):
	q00 = 1.0 - q01
	q11 = 1.0 - q10
	word = list(word)
	error = 0
	correct = 0
	new_word = ""
	for bit in word:
		act = random.uniform(0, 1.0)
		if bit == "0":
			if act >= 0 and act < q01:
				new_word += "1"
				error += 1
			else:
				correct += 1
				new_word += "0"
		elif bit == "1":
			if act >= 0 and act < q10:
				new_word += "0"
				error += 1
			else:
				new_word += "1"
				correct += 1
			
	#print "Correct Transmisions: %s"%correct
	#print "Errors in Transmision: %s"%error
	return error

def statistics(fn):
	data = read_data(fn)
	graph_file = open("graph.plot", "w")
	for i in range(len(data)):	
		p, q01, q10 = data[i]
		fn = "points_%s_%s_%s.dat"%(str(p).replace(".", ""), str(q01).replace(".", ""), str(q10).replace(".", ""))
		f = open(fn, "w")
		for j in range(30):
			word = binary_word(p, j)
			total = 0
			error = 0
			for k in range(300):
				if channel(q01, q10, word) > 0:
					error += 1
				total += 1
			prom = float(error)/float(total)
			f.write("%s %s\n"%(j, prom))
		f.close()
		
		if i == 0:
			graph_file.write('plot "%s" with lines title "q01 = %s q10 = %s", \\\n'%(fn, q01, q10))
		if i == len(data) - 1:
			graph_file.write('"%s" with lines title "q01 = %s q10 = %s"\npause -1'%(fn, q01, q10))
		else:
			graph_file.write('"%s" with lines title "q01 = %s q10 = %s", \\\n'%(fn, q01, q10))
	f.close()

def read_data(fn):
	f = open(fn, "r")
	data = []
	for line in f.readlines():
		if "#" not in line:
			p, q01, q10 = line.split(" ")
			data.append((float(p), float(q01), float(q10)))
	f.close()
	return data
	
if __name__ == "__main__":
	statistics(argv[1])
		
	
		
