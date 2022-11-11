import json
import os


def main(mode:str)->None:
    global_const=json.loads(open("src/kqs/global_const.json","r").read())
    if mode=="setup.py":
        setup_py_read=open("setup.py","r")
        setup_content=setup_py_read.read().replace("__KQS_VERSION__",global_const["KQS_VERSION"]).replace("__KQS_CORE_NAME__",global_const["KQS_CORE_NAME"])
        print(setup_content)
        setup_py_read.close()
        os.remove("setup.py")
        setup_py_write=open("setup.py","w")
        setup_py_write.write(setup_content)
        setup_py_write.close()



if __name__ == "__main__":
    main(mode="setup.py")