# import importlib
# import pkgutil
#
#
# def import_submodules(package, recursive=True):
#     """ Import all submodules of a module, recursively, including subpackages
#
#     :param package: package (name or actual module)
#     :type package: str | module
#     :rtype: dict[str, types.ModuleType]
#     """
#     if isinstance(package, str):
#         package = importlib.import_module(package)
#     results = {}
#     for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
#         full_name = package.__name__ + '.' + name
#         results[full_name] = importlib.import_module(full_name)
#         if recursive and is_pkg:
#             results.update(import_submodules(full_name))
#     return results
#
# print(import_submodules(__name__).keys())
# __all__ = import_submodules(__name__).keys()

#
# def import_submodules(package_name):
#     """ Import all submodules of a module, recursively
#
#     :param package_name: Package name
#     :type package_name: str
#     :rtype: dict[types.ModuleType]
#     """
#     package = sys.modules[package_name]
#     return {
#         name: importlib.import_module(package_name + '.' + name)
#         for loader, name, is_pkg in pkgutil.walk_packages(package.__path__)
#     }
#
# import imp
# import sys
# #----------------------------------------------------------------------
# def dynamic_importer(name, class_name):
#     """
#     Dynamically imports modules / classes
#     """
#     try:
#         fp, pathname, description = imp.find_module(name)
#     except ImportError:
#         print("unable to locate module: " + name)
#         return (None, None)
#
#     try:
#         example_package = imp.load_module(name, fp, pathname, description)
#     except Exception, e:
#         print(e)
#
#     try:
#         myclass = imp.load_module("%s.%s" % (name, class_name), fp, pathname, description)
#         print(myclass)
#     except Exception, e:
#         print(e)
#
#     return example_package, myclass
