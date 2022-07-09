from kqs.model_basic import Base


class OSM(Base):
    def __init__(self) -> None:
        super().__init__()


class OSH(Base):
    def __init__(self) -> None:
        super().__init__()


class OSC(Base):
    def __init__(self) -> None:
        super().__init__()

    def Modify():
        pass

    def Create():
        # Call create function to create them in memory
        pass

    def Delete():
        # If element already in memory, delete it. (And save other unfound id)
        pass
