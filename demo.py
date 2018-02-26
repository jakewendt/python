#!/usr/bin/env python
#
#	Use "/usr/bin/env python" rather than a fixed python location or version
#	"/usr/bin/env" should exist on all *nix machines.
#


def main():
#	x=1
#	print( id(x) )
	print( "In my main method." )

	import sys
	if( not sys.stdin.isatty() ):	#	is False when STDIN being used.
		print("STDIN:BEGIN")
		for line in sys.stdin:
			print( line )
		print("STDIN:END")
	

#	interesting python variable value keep same id. Surprised this doesn't consume a lot of memory.
#x=1
#print( id(x) )






#	Apparently, when called from the command line, __name__ is set to "__main__"
#	When included as a library, I am guessing, it is not.
#	if __name__ == "__main__": main()
if __name__ == "__main__":
	print ( 'Script called from command line.' ) 

	#	https://docs.python.org/3/library/argparse.html

	import argparse
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-s', action='store', dest='simple_value',
	                    help='Store a simple value')
	
	parser.add_argument('-c', action='store_const', dest='constant_value',
	                    const='value-to-store',
	                    help='Store a constant value')
	
	parser.add_argument('-t', action='store_true', default=False,
	                    dest='boolean_switch',
	                    help='Set a switch to true')
	parser.add_argument('-f', action='store_false', default=False,
	                    dest='boolean_switch',
	                    help='Set a switch to false')
	
	parser.add_argument('-a', action='append', dest='collection',
	                    default=[],
	                    help='Add repeated values to a list',
	                    )
	
	parser.add_argument('-A', action='append_const', dest='const_collection',
	                    const='value-1-to-append',
	                    default=[],
	                    help='Add different values to list')
	parser.add_argument('-B', action='append_const', dest='const_collection',
	                    const='value-2-to-append',
	                    help='Add different values to list')
	
	parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
	
	results = parser.parse_args()
	print( 'simple_value     =', results.simple_value )
	print( 'constant_value   =', results.constant_value )
	print( 'boolean_switch   =', results.boolean_switch )
	print( 'collection       =', results.collection )
	print( 'const_collection =', results.const_collection )

	main()

	#	print REQUIRES parentheses! lame. (In v3, print is now a function)
	#	NOT needed in ipython. Inconsistency. Yay.
#
#	The above is a common way, in other languages as well, to define classes,
#		methods, variables, etc. as a library in a runnable script.
#	Usually, this is the last line of a script which then calls a
#		previously defined method called "main()" or whatever you prefer.
#
