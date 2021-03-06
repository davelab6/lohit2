#!/usr/bin/python
# -*- coding: UTF-8 -i*-
# Copyright (C) 2013-14, Sneha Kore <skore@redhat.com>, Pravin Satpute <psatpute@redhat.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os, sys, commands

def generate_outfile(txt_file,ttf_file):
	inputfile=open(txt_file)
	outputfile=open("std-test-out.txt","w")

	#Read the test-case input	
	flines=inputfile.readlines()
	ttfname = ttf_file
	
	#Exceute hb-shape command for each test-case from input file
	for string in flines:
		print "String : "+string
		words=string.split()		
		cmd="hb-shape %s %s"%(ttfname,words[0])
		print "Command : "+cmd+"\n"		
		status, output = commands.getstatusoutput(cmd)
		# Write output to the output file		
		print "Output : "+output+"\n"	
		outputfile.write(words[0]+"\t"+""+output+"\n")
	outputfile.close()
	inputfile.close()
 
def generate_testfile(txt_file,ttf_file):
	inputfile=open(txt_file)
	outputfile=open("output.txt","w")
	fout=open("failed_test_case.txt","w")

	#Read the test-case input	
	flines=inputfile.readlines()
	ttfname = ttf_file
	count=0

	#Exceute hb-shape command for each test-case from output file
	for string in flines:
		print " String : "+string
		words=string.split()	
		cmd="hb-shape %s %s"%(ttfname,words[0])
		print " Command : "+cmd+"\n"		
		status, output = commands.getstatusoutput(cmd)
		print " Output : "+output+"\n"		
		# Test to check, wheather test-case from output file & the result, are matching		
		if words[1] == output:
			print " "+words[1]+" EQUALS "+" "+string				
			print " [SUCESS]\n"	
			outputfile.write("  *  "+words[0]+"\t"+""+output+"\n")
		else:
			print " [FAILURE]\n"	
			fout.write("  *  "+words[0]+"\t"+""+output+"\n")
			count=count+1
	#Count for failed test-cases	
	print "%d Test Cases Failed"%count			
	inputfile.close()
	outputfile.close()
 

if __name__ == "__main__":

 if len(sys.argv) < 4:
        print "USAGE: python auto_test.py <test-case doc-name> <ttf_filename> <generate/test> \n For <generate> : test-case-doc-name will be <test-case.txt> \n For <test> : test-case-doc-name will be <std-test-out.txt>"
 else:
	txt_filename = sys.argv[1]
	ttf_filename = sys.argv[2]
	if "generate" in sys.argv[3]:
		generate_outfile(txt_filename,ttf_filename)
	else:
		generate_testfile(txt_filename,ttf_filename)	
			


