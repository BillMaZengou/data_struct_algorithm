class Fraction(object):
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom

	def __str__(self):
		return str(self.num) + "/" + str(self.den)

	def __add__(self, other_fraction):
		new_num = self.num*other_fraction.den + other_fraction.num*self.den
		new_den = self.den * other_fraction.den
		common = gcd(new_num, new_den)
		new_num = new_num//common
		new_den = new_den//common
	
		if new_num%new_den == 0:
			return new_num // new_den
		else:
			return Fraction(new_num//common, new_den//common)

	def __eq__(self, other_fraction):
		first_num = self.num * other_fraction.den
		second_num = self.den * other_fraction.num
		return first_num == second_num

def gcd(m, n):
	while m%n != 0:
		oldm = m
		oldn = n
		
		m = oldn
		n = oldm%oldn
	return n

