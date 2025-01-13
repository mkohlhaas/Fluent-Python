from lake import alert


class Swan:
    def honk(self, repetitions: int) -> None:
        print("Honk! " * repetitions)

    def swim(self) -> None:
        pass


bella = Swan()

alert(bella)
