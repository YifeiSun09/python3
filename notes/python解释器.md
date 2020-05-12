# Python解释器  
常见的有CPython,IPython,PyPy,Jython,IronPthon  
相同点: 都是python解释器,遵循python的语法,大部分的代码都是兼容的  
不同点:  
1. CPython是使用最广泛的python解释器,linux下默认内置的就是cpython,使用`>>>`作为提示符  
2. IPython为基于CPython开发的python解释器,在交互方式上对比cpython有所增强,但是功能与cpython相同.ipython使用`In [序号]:`作为提示符.  
3. PyPy的目标在于执行速度,才用了JIT技术,对Python代码进行了动态编译.需要注意的是pypy与cpython并不完全兼容,可能会出现结果不一致的情况.  
4. Jython是运行在java平台上的python解释器,可以把python代码编译成java字节码.  
5. IronPython为运行在.Net平台上的python解释器,可以直接把python代码编译成.Net字节码.  

python跨平台比较好的解决方案是通过网络调用交互,而不是用jython与ironpython.  
