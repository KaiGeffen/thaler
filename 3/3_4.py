# Fix some prime p of your choosing.
# Write a Python program that takes as input an
# array of length 2^l specifying all evaluations of a
# function f : {0,1}^l → Fp and a vector r ∈ Fp,
# and outputs f ̃(r).
import sys


P = 17

def get_MLE(ary, r):
	# ary of length 2^l specifying all evaluations of a function f
	# r a vector in the p-finite field

	def mle(x):
		return 2 * x

	return mle


# Take an r + array from the command line
r = sys.argv[0]
ary = [1,2,3,4] # sys.argv[1]

get_MLE(ary, r)
print(get_MLE(ary, r)(3))
