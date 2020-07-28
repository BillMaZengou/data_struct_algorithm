def gcd(m, n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

class Fraction(object):
	def __init__(self, top, bottom):
		if type(top) is int and type(bottom) is int:
			self.num = top
			self.den = bottom

			common = gcd(self.num, self.den)
			self.num /= common
			self.den /= common
		else:
			raise TypeError("Error: input is not 'int' type")

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def __str__(self):
		if self.num%self.den == 0:
			return str(int(self.num // self.den))
		else:
			return str(int(self.num)) + "/" + str(int(self.den))

	""" Arithmetic """
	def __add__(self, other_fraction):
		new_num = self.num*other_fraction.den + other_fraction.num*self.den
		new_den = self.den * other_fraction.den
		return Fraction(int(new_num), int(new_den))

	def __sub__(self, other_fraction):
		new_num = self.num*other_fraction.den - other_fraction.num*self.den
		new_den = self.den * other_fraction.den
		return Fraction(int(new_num), int(new_den))

	def __mul__(self, other_fraction):
		new_num = self.num * other_fraction.num
		new_den = self.den * other_fraction.den
		return Fraction(int(new_num), int(new_den))

	def __truediv__(self, other_fraction):
		new_num = self.num * other_fraction.den
		new_den = self.den * other_fraction.num
		return Fraction(int(new_num), int(new_den))

	""" Inequality """
	def __eq__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num == second_num

	def __gt__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num > second_num

	def __ge__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num >= second_num

	def __lt__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num < second_num

	def __le__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num < second_num

	def __ne__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num != second_num


if __name__ == '__main__':
	a = Fraction(1, 3)
	b = Fraction(3, 6)
	c = 2
	# print(b)
	# print(b - a)
	# print(a * b)
	# print(Fraction(6, 2))
