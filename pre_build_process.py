import os


def main() -> None:
    global_const_data = [
        {x.split("=")[0]: x.split("=")[1]}
        for x in open("src/keqing/global_const.py", "r")
        .read()
        .replace(" ", "")
        .replace('"', "")
        .split("\n")
        if x != ""
    ]
    global_const = {}
    for tag in global_const_data:
        global_const = {**global_const, **tag}
    print(global_const)
    # run
    setup_py_read = open("pyproject.toml", "r")
    setup_content = (
            setup_py_read.read()
            .replace("__KEQING_CORE_NAME__", global_const["KEQING_CORE_NAME"])
            .replace("__KEQING_VERSION__", global_const["KEQING_VERSION"])
        )
    setup_py_read.close()
    os.remove("pyproject.toml")
    setup_py_write = open("pyproject.toml", "w")
    setup_py_write.write(setup_content)
    setup_py_write.close()


if __name__ == "__main__":
    main()
