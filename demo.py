#!/usr/bin/env python
#
#	Use "/usr/bin/env python" rather than a fixed python location or version
#	"/usr/bin/env" should exist on all *nix machines.
#


def main():
	print( "In my main method." )
	

#	How to process command line arguments?

#	How to process files passed on the command line as well as STDIN?



#	Apparently, when called from the command line, __name__ is set to "__main__"
#	When included as a library, I am guessing, it is not.
if __name__ == "__main__":
	print ( 'Script called from command line.' ) 
	main()
	#	print REQUIRES parentheses! lame.
	#	NOT needed in ipython. Inconsistency. Yay.
#
#	The above is a common way, in other languages as well, to define classes,
#		methods, variables, etc. as a library in a runnable script.
#	Usually, this is the last line of a script which then calls a
#		previously defined method called "main()" or whatever you prefer.
#
