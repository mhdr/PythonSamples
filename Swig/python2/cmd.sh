swig -python hello.i
gcc -fpic -c hellomodule.c hello_wrap.c -I/usr/include/python2.7/
gcc -shared hellomodule.o hello_wrap.o -o _hello.so
