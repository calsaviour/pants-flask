# Running a src example
./pants run src/python/helloworld:helloworld

# Create a binary distribution
PEX_VERBOSE=1 ./pants binary src/python/helloworld:helloworld

# To execute the distribution
./dist/helloworld.pex
