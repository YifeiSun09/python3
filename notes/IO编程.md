# IO编程  
1. 同步IO  
IO操作在执行时，一直被阻塞，直到该任务执行完成  
2. 异步IO  
IO操作在未执行完成时，就可以继续执行接下来的工作，在未完成的任务执行完成时，系统会进行通知。  

## 文件读写  
### 读  
```
f = open(文件名,'r')
```
如果文件不存在，则会报错.  
我们可以使用`read()`方法将文件内容全部读取出来。  
在文件读取完成之后，必须要关闭文件对象。因为文件对象对占用操作系统的资源，系统同一时间能够打开的文件数量也是有限的。  
```
f.close()
```  
在文件读取的过程中可能会出现`IOError`错误，一旦出错`f.close`就不会调用，所以需要使用`try...finally`结构来实现文件读写:  
```
try:
    f = open('/path/to/file','r')
    print(f.read())
finally:
    if f: # 文件错误
        f.close()
```  
在读取大文件的时候，使用不带参数的`read`方法并不是特别合理，我们应该给它传递一个读取长度的参数。  
对于配置文件，我们可以调用`readlines`方法：  
```
for line in f.readlines():
    print(line.strip()) # 删除末尾的\n
```

## 类文件对象  
像`open`函数返回的这种有个`read`方法的对象，在python中叫类文件对象。除了file之外，还可以是内存的字节流，网络流，自定义刘。  
类文件对象不要求从特定的类继承，只要写个`read`方法就行.  

## 二进制文件  
我们需要读取二进制文件时，只需要在之前指定的文件模式后面加上一个b，表示二进制  
```
>>> f = open('/path/to/file','rb') # 读取二进制文件
>>> f.read()
```

## 字符编码  
要赌球非UTF-8编码的文本文件，我们需要给`open`函数传入一个encoding参数,例如读取GBK编码文件。  
```
>>> f = open('/path/to/gbk.txt','r',encoding='gbk')
>>> f.read()
```
遇到有些编码不规范的文件，可能会遇到`UnicodeDecodeError`，这个是因为文件中可能夹杂了一些非法编码字符，遇到这种情况，我们可以给`open`函数传入一个`errors`参数，表示遇到编码错误后如何处理。  
```
>>> f = open('/path/to/file.txt','r',encoding='gbk',errors='ignore')
```  
### 写文件  
和读文件的形式大致差不多，在文件打开时，指定一个`w`文件模式即可。  
```
f = open('/path/to/file.txt','w')
f.write('Hello,World!')
f.close()
```  
## 操作文件和目录  
与操作系统相关的功能在os模块中。  
```
>>> import os
>>> os.name # 操作系统类型
>>> os.uname() # windows上不存在
>>> os.environ # 环境变量
>>> os.environ.get('PATH') # PATH变量
>>> os.environ.get('x','default')
>>> os.path.abspath('.') # 当前路径的绝对路径
>>> os.path.join('/apple','boy') # 路径拼接，自适应操作系统
>>> os.mkdir(目录路径) # 创建目录
>>> os.rmdir(目录路径) # 删除目录
>>> os.path.split(路径) # 拆分目录和文件名
>>> os.path.splittext(路径) # 拆分路径和后缀
>>> os.rename(旧文件,新文件) # 重命名
>>> os.remove(文件) # 删除文件
>>> os.listdir('.') # 列出当前目录
>>> os.isdir(路径) # 判断路径是否为目录
>>> os.isfile(路径) # 判断当前路径是否为文件
```