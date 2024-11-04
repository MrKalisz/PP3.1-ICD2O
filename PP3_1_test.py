import os.path
import sys
import PP3_1

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP3_1.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-5', '-5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_1.input = mock_input

	PP3_1.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In:\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP3_1.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_1.input = mock_input

	PP3_1.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 1 2 3 4 5\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP3_1.py")
		assert exists
	except:
		sys.exit()

	input_values = ['5']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_1.input = mock_input

	PP3_1.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 0 1 2 3 4 5 6 7 8 9\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP3_1.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_1.input = mock_input

	PP3_1.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: 1 2 3 4 5 6 7 8 9 10\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP3_1.py")
		assert exists
	except:
		sys.exit()

	input_values = ['10']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP3_1.input = mock_input

	PP3_1.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19\n"

