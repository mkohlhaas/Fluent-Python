from lake import alert


class Parrot:
    def honk(self, times: int) -> None:
        print("Honk! " * times * 2)


ze_carioca = Parrot()

alert(ze_carioca)  # <2>
