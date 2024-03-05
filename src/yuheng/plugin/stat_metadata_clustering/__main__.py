def main(obj):
    # if run in standalone cli, only support input a xml file and then parse it to Carto
    # if run by import, both parse xml or pass Carto object is acceptable.
    if isinstance(obj, type(str)):
        # parse mode
        pass
    else:
        world = obj


if __name__ == "__main__":
    main()
