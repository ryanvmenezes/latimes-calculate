import math
from __future__ import division # to ensure integer division does not happen

def zval_prop(numerator, denominator, mean_pct = sum(numerator) / sum(denominator)):
	'''
	A calculation to determine how many standard errors (deviations)
	a proportion is from a mean value.

	This borrows from the null hypothesis test for a single proportion: 
	http://stattrek.com/hypothesis-test/proportion.aspx?Tutorial=AP

	It is most useful when trying to rank a collection of percentages
	while giving greater weight to those with more observations in the
	denominator.

	

	'''
	try:
        numerator = list(map(float, numerator))
        denominator = list(map(float, denominator))
    except ValueError:
        raise ValueError('Input values must contain numbers')

    if len(numerator) != len(denominator):
        raise ValueError('The two lists you provided do not have the same \
number of entries. Pearson\'s r can only be calculated with paired data.')
	return [ (( n / d ) - mean_pct) / math.sqrt( mean_pct * (1 - mean_pct) /  d ) for n, d in zip(numerator, denominator) ]