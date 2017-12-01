
class Course_mark():

	def __init__(self, code="undef", units=6, mark=-1):
		self.code = code
		self.units = units
		self.mark = mark

def calculate_wam(courses=[], thesis=[]):
	merged = courses + thesis
	units_total = 0
	marks_total = 0
	for course in merged:
		if course.mark != -1:
			units_total = units_total + course.units
			marks_total = marks_total + (course.mark*(course.units/6))
	wam = (marks_total/units_total)*6
	return wam, units_total

def calculate_cse_wam(courses=[]):
	units_totals = {}
	ratio_top = 0
	ratio_bottom = 0
	units_total = 0
	for course in courses:
		if course.mark == -1: # no mark
			continue
		w = 0
		u = course.units
		# thesis
		if course.code[:4] == "THES":
			w = u + 6
		# general education or level 1
		elif (not course.code[:4] in ["COMP", "ENGG", "SENG", "MATH"]) or course.code[4] == "1":
			w = 1
		# level 2
		elif course.code[4] == "2":
			w = 2
		# level 3
		elif course.code[4] == "3":
			w = 3
		# level 4 or thesis
		elif course.code[4] in ["4", "9"]:
			w = 4
		else:
			raise TypeError("Weird course code: " + course.code)
		if course.code[:4] == "THES":
			u = u + 6
		units_total = units_total + u
		ratio_top = ratio_top + (w * u * course.mark)
		ratio_bottom = ratio_bottom + (w * u)
	cse_wam = ratio_top / ratio_bottom
	return cse_wam

def main():
	courses = [
		# 14s1
		Course_mark(code="COMP1917", mark=81),
		Course_mark(code="ENGG1000", mark=74),
		Course_mark(code="MATH1081", mark=57),
		Course_mark(code="MATH1131", mark=59),

		# 14s2
		Course_mark(code="COMP1927", mark=77),
		Course_mark(code="COMP2041", mark=69),
		Course_mark(code="MATH1231", mark=61),
		Course_mark(code="SENG1031", mark=79),

		# 15s1
		Course_mark(code="COMP2111", mark=87),
		Course_mark(code="COMP2121", mark=75),
		Course_mark(code="COMP2911", mark=58),
		Course_mark(code="SENG2011", mark=71),

		# 15s2
		Course_mark(code="COMP3331", mark=74),
		Course_mark(code="MATH2400", mark=83, units=3),
		Course_mark(code="MATH2859", mark=73, units=3),
		Course_mark(code="PHYS1160", mark=89),
		Course_mark(code="SENG2021", mark=75),

		# 16s1
		Course_mark(code="COMP3311", mark=83),
		Course_mark(code="COMP3411", mark=75),
		Course_mark(code="COMP3821", mark=77),
		Course_mark(code="SENG3011", mark=87),

		# 16s2
		Course_mark(code="COMP3421", mark=70),
		Course_mark(code="COMP4121", mark=85),
		Course_mark(code="COMP4920", mark=67),
		Course_mark(code="COMP9447", mark=67),

		# 17s1
		Course_mark(code="COMP9417", mark=77),
		Course_mark(code="THES0001"),

		# 17s2
		Course_mark(code="THES0002", units=12, mark=79)
	]

	print(calculate_wam(courses))
	print(calculate_cse_wam(courses))

if (__name__ == "__main__"):
	main()
