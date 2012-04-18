# Code that is reused across multiple scripts

################
# MEMOIZATION  #
################
# works, but really slow compared to hand-done memoization because of pickling.
# http://pko.ch/2008/08/22/memoization-in-python-easier-than-what-it-should-be/
import functools
import cPickle
def memoize(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(*args,**kwargs):
                haxh = cPickle.dumps((args, sorted(kwargs.iteritems())))
                if haxh not in memory:
                        memory[haxh] = fctn(*args,**kwargs)
                return memory[haxh]
        if memo.__doc__:
            memo.__doc__ = "\n".join([memo.__doc__,"This function is memoized."])
        return memo

def memoize_fast_args_only(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(*args):
                haxh = args
                if haxh not in memory:
                        memory[haxh] = fctn(*args)
                return memory[haxh]
        return memo
 
# Still not exactly as fast as hand-done implementation, probably because of the function wrapping overhead, but much closer than above.
def memoize_fast_1_arg(fctn):
        memory = {}
        @functools.wraps(fctn)
        def memo(a):
	    haxh = a
	    if haxh in memory:
	      return memory[haxh]
	    else :
	      result       = fctn(a)
	      memory[haxh] = result
	      return result
        return memo
 
