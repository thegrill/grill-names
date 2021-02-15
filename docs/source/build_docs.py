from sphinx.cmd import build
if __name__=='__main__':
    import shutil
    shutil.rmtree(r"B:\write\code\git\grill-names\docs\build")
    build.build_main([r"B:\write\code\git\grill-names\docs\source", r"B:\write\code\git\grill-names\docs\build"])
