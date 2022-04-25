from .importer import import_module_from_home


module = import_module_from_home('moduleA','some_stuff.py')
SomeClass = module.SomeClass

__all__ = ['SomeClass']
