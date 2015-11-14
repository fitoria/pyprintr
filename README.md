Python-printr (or PyPrintr) is a recursive printing objects module that allows
to emulate the print_r() function of PHP  by printing the objects properties of
a class instance and its internal structure. 

     NOTICE:
     If you need to use printr() function for list, tuples and dicts, 
     please, don't use printr() function. You can choose pprint module. 
     printr() function is only for objects of your own class instances. 
     Read more about Python-printr at https://pypi.python.org/pypi/pyprintr



**Developed by:**
    Eugenia Bahit
    http://www.eugeniabahit.com/


**Contributors:**
    Alejandro Ramirez
    http://www.ramirezalejandro.com.ar/


**Licence:** 
    GPL v3.0


---------------------------------------------------------------------------
Basic Usage
---------------------------------------------------------------------------
First, you must get an object of a class instance and then, you can call 
to the printr function by passing the object like an argument function.

::

    from printr import printr

    my_object = MyClass()
    printr(my_object)


---------------------------------------------------------------------------
Customization
---------------------------------------------------------------------------
Change this value by modifying the IDENTATION_CHAR constant:

::

    import printr
    printr.IDENTATION_CHAR = "."  # use point to identation
    myobject = MyClass()
    printr.printr(myobject)


Also, you can set the identation width, by modifying the TAB_WIDTH constant 
(by default is 4):

::

    import printr
    printr.TAB_WIDTH = 2
    myobject = MyClass()
    printr.printr(myobject)

