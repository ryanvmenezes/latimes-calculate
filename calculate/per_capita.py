def per_capita(value, population, per=10000, fail_silently=True):
	"""
	Accepts two numbers, a value and population total, and returns the per capita rate.
	
	By default, the result is returned as a per 10,000 person figure.
	
	If you divide into zero -- an illegal operation -- a null value 
	is returned by default. If you prefer for an error to be raised, 
	set the kwarg 'fail_silently' to False.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.per_capita()
	
	h3. Documentation
	
		* "per capita":http://en.wikipedia.org/wiki/Per_capita
	
	"""
	if not isinstance(value, (int,long,float)):
		return ValueError('Input values should be a number, your first input is a %s' % type(value))
	if not isinstance(population, (int,long,float)):
		return ValueError('Input values should be a number, your second input is a %s' % type(population))
	try:
		rate = (float(value) / population) * per
		return rate
	except ZeroDivisionError:
		# If there's a zero involved return null if set to fail silent
		if fail_silently:
			return None
		# but otherwise shout it all out
		else:
			raise ZeroDivisionError("Sorry. You can't divide into zero.")