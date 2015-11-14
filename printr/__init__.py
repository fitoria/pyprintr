#! -*- coding: utf-8 -*-
"""
 Python-printr (or PyPrintr) is a recursive printing objects module that allows 
 to emulate the print_r() function of PHP  by printing the objects properties of
 a class instance and its internal structure. 

    =========================================================================
     NOTICE:
    ·········································································
     If you need to use printr() function for list, tuples and dicts, 
     please, don't use printr() function. You can choose pprint module. 
     printr() function is only for objects of your own class instances. 
     Read more about Python-printr at https://pypi.python.org/pypi/pyprintr
    =========================================================================

     Developed by:
        F. Eugenia Bahit
        http://www.eugeniabahit.com/
    
     Contributors:
        R. Alejandro Ramirez
        http://www.ramirezalejandro.com.ar/
        
        Mariano García Berrotaran
    
     Licence:
        GPL v3.0
        
    =========================================================================
     BASIC USAGE
    =========================================================================
    First, you must get an object of a class instance and then, you can call 
    to the printr function by passing the object like an argument function.

    Example:

        class Vidrio(object):

            def __init__(self):
                self.color = ''
                
                
        class Marco(object):

            def __init__(self):
                self.color = ''
                self.material = ''
                self.vidrio = Vidrio()


        class Ventana(object):
            
            def __init__(self):
                self.posicion = ''
                self.marco = Marco()


        from printr import printr
        ventana = Ventana()
        printr(ventana)


    Returns:

        <Ventana object>
            {
                posicion: ''
                marco: <Marco object>
                {
                    color: ''
                    vidrio: <Vidrio object>
                    {
                        color: ''
                    }
                    material: ''
                }
            }

    =========================================================================
     ADVANCED USE
    =========================================================================
    You can set the character using for identation. By default is white space.
    
    -------------------------------------------------------------------------
     IDENTATION CHAR
    -------------------------------------------------------------------------
    Change this value by modifying the IDENTATION_CHAR constant:

        import printr
        printr.IDENTATION_CHAR = "."  # use point to identation
        myobject = MyClass()
        printr.printr(myobject)

    -------------------------------------------------------------------------
     TAB WIDTH
    -------------------------------------------------------------------------
    Also, you can set the identation width, by modifying the TAB_WIDTH 
    constant (by default is 4):

        import printr
        printr.TAB_WIDTH = 2
        myobject = MyClass()
        printr.printr(myobject)
"""
__author__ = "Eugenia Bahit"
__copyright__ = "Copyright 2011, Eugenia Bahit"
__credits__ = ["Ruben Alejandro Ramirez", "Mariano Garcia Berrotaran"]
__license__ = "GPL v 3.0"
__version__ = "1.0"
__maintainer__ = "Eugenia Bahit"
__email__ = "ebahit@member.fsf.org"
__status__ = "Stable"

IDENTATION_CHAR = " "
TAB_WIDTH = 4


def get_human_object_name(obj, is_collection=False):
    """
    Convert an object type in a human readable string
    """
    aditional = ' collection' if is_collection else ''
    return "<%s object%s>" % (obj.__class__.__name__, aditional)


def get_human_value(value):
    """
    Convert an object value in a human readable string
    """

    if str(value) == '':
        return "''"
    elif str(value) == '[]':
        return "[empty collection]"
    elif str(value).startswith('<'):
        return get_human_object_name(value)
    elif isinstance(value, list):
        if str(value[0]).startswith('<'):
            return get_human_object_name(value[0], True)
        else:
            return value
    else:
        return value


def printr(obj, tabs=TAB_WIDTH, object_as_element=False):
    """
    Print the object properties recursively in a human readable mode
    """

    if tabs == TAB_WIDTH or object_as_element:
        print get_human_object_name(obj)

    ident = IDENTATION_CHAR * tabs
    spaces = IDENTATION_CHAR * (tabs + TAB_WIDTH)

    print "%s{" % ident

    for prop, value in vars(obj).iteritems():
        print "%s%s: %s" % (spaces, prop, get_human_value(value))

        if str(value).startswith('<') and str(value).endswith('>'):
            printr(value, (tabs + TAB_WIDTH))
        elif str(value) == '[]':
            pass
        elif isinstance(value, list):
            if str(value[0]).startswith('<'):
                for elemento in value:
                    printr(elemento, (tabs + TAB_WIDTH), True)

    print "%s}" % ident

