import pkgutil 

# This code imports any other modules in this directory
# e.g local, facebook, twitter, openid, etc

__path__ = pkgutil.extend_path(__path__, __name__)
        
for importer, modname, ispkg in pkgutil.walk_packages(path=__path__, prefix=__name__+'.'):
    # print(modname)
    __import__(modname)
