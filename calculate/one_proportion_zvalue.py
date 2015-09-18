import math
from __future__ import division # to ensure integer division does not happen

def zval_prop(numerator, denominator, mean_pct = sum(numerator) / sum(denominator)):
	'''
	A calculation to determine how unusual a proportion is, by counting
	how many standard errors (deviations) it is from a mean value.

	This borrows from the null hypothesis test for a one-sample proportion.


	'''

	return [ (( n / d ) - mean_pct) / math.sqrt( mean_pct * (1 - mean_pct) /  d ) for n, d in zip(numerator, denominator) ]