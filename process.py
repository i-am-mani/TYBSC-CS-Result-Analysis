

import re

class Student():
	"""student result info includes: name, sgp of sem 1 - 6 and final CGPA."""
	def __init__(self):
		self.name = ""
		self.college_name = ""
		self.sgp1 = ""
		self.sgp2 = ""
		self.sgp3 = ""
		self.sgp4 = ""
		self.sgp5 = ""
		self.sgp6 = ""
		self.final_cgpa = ""

	def __str__(self):
		return f"{self.name} {self.college_name} {self.final_cgpa}"



inital_digits = r"[\d]{7}"
regex_final_cgpa = r"(FINAL\W*CGPA\W*[\d|\.]*)"
regex_sgp1 = r"(SGP1:\s?[\d\.]*)"
regex_sgp2 = r"(SGP2:\s?[\d\.]*)"
regex_sgp3 = r"(SGP3:\s?[\d\.]*)"
regex_sgp4 = r"(SGP4:\s?[\d\.]*)"
regex_sgp5 = r"(SGP5:\s?[\d\.]*)"
regex_sgp6 = r"(SGP6:\s?[\d\.]*)"
regex_name = r"[\d]{7}\s?([\W\w*]+?)(?=\s+\d)"
regex_college = r"\s+([a-zA-Z]*)(?=\W\S)"

FILE_PATH = "sample.txt"
count = 0
_gp = 0
max_gp = 0

all_students = []

def extract_name(line):
	g1 = re.match(regex_name, line)	
	return g1.groups()[0].strip()

def extract_college(line):
	if(len(line) > 25):
		return line[25:].split()[0]

def get_first_match(regex,student):
	match = re.findall(regex, line)
	if(match != None and len(match) != 0):
		gpa_str = match[0]
		if(regex != regex_final_cgpa):
			gpasplit = gpa_str.split(':')
			sem = gpasplit[0]
			gpa = gpasplit[-1]
			print(f"{sem} - {gpa}")
			student[sem] = gpa
		else:
			gpasplit = gpa_str.split(' ')
			gpa = gpasplit[-1]
			student["CGPA"] = gpa

with open(FILE_PATH) as file:
	next_line_is_college = False
	# doc_text = ''.join(file.readlines())
	prev_student = None
	for line in file.readlines()[20:60]:
		# filter heading text
		if(re.search(inital_digits, line) or prev_student):			
			obj = re.match(inital_digits, line)
			# print(f"matched object {obj.group()}")
			# update name
			if(obj != None):
				[i for i in line if i]
				name = extract_name(line)
				print(name)
				if(prev_student != None):	
					all_students.append(prev_student)
				prev_student = dict()
				prev_student['name'] = name
				next_line_is_college = True

				continue
			if(next_line_is_college):				
				college_name = extract_college(line)
				print(college_name)
				next_line_is_college = False
				prev_student['college_name'] = college_name
				continue
			match = re.findall(regex_sgp1, line)
			if(match != None and len(match) != 0):
				print(match[0])	
			get_first_match(regex_sgp1,prev_student)
			get_first_match(regex_sgp2,prev_student)
			get_first_match(regex_sgp3,prev_student)
			get_first_match(regex_sgp4,prev_student)
			get_first_match(regex_sgp5,prev_student)
			get_first_match(regex_sgp6,prev_student)
			get_first_match(regex_final_cgpa,prev_student)
			# print(line)
			# break
			

		

for i in all_students:
	print(i)

	# print(doc_text[0:100])
	# matches = re.finditer(regex, doc_text, re.MULTILINE)

	# for matchNum, match in enumerate(matches, start=1):
	# 	try:			
	# 		gp = float(match.group().split(" ")[-1])
	# 		_gp += gp
	# 		count += 1
	# 		max_gp = max(max_gp,gp)
	# 	except:
	# 		print("Failed for {match}")


			
# print(_gp / count)
# print(max_gp)



  