from sphinx.cmd import build
if __name__=='__main__':
    import shutil
    try:
        shutil.rmtree(r"B:\write\code\git\grill-names\docs\build")
    except FileNotFoundError:
        pass
    build.build_main([r"B:\write\code\git\grill-names\docs\source", r"B:\write\code\git\grill-names\docs\build"])
