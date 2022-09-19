cext:
	cd cextension && gcc -shared add.c -I/usr/include/python3.8 -o add.so

cyth:
	cd cython && python3 setup.py build_ext --inplace

all: cext cyth

clean:
	cd cython && rm -rf *.so && rm -rf build
	cd cextension && rm -rf *.so
