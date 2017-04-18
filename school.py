class Institution(object):
	def __init__(self, name, address):
		self.name = name
		self.address = address

class School(Institution):
	def __init__(self, students = [], teachers= [], subjects= []):
		self.students = students
		self.teachers = teachers
		self.subjects = subjects

	def add_subject(self, subj):
		return self.subjects.append(subj)

	def add_teacher(self, teacher):
		return self.teachers.append(teacher)

	def add_student(self, student):
		return self.students.append(student)







