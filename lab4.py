class Perfume:
    def __init__(self, volume=0, price=0.0, brand_name="Невідомо"):
        self.__volume = volume
        self.__price = price
        self.__brand_name = brand_name
        self.discount = 0
        self.category = "жіночі"

    def get_volume(self):
        return self.__volume

    def get_price(self):
        return self.__price

    def get_brand_name(self):
        return self.__brand_name

    def __str__(self):
        return (
            f"Парфуми {self.__brand_name}, {self.__volume} мл, "
            f"{self.__price} грн"
        )

    def __repr__(self):
        return (
            f"Perfume({self.__volume!r}, {self.__price!r}, "
            f"{self.__brand_name!r})"
        )

    def __del__(self):
        print(f"Об'єкт {self.__brand_name} видалено")
#bbb

def main():
    perfume1 = Perfume()
    perfume2 = Perfume(50, 1200.0, "Chanel")
    perfume3 = Perfume(100, 2500.0, "Dior")

    for perfume in (perfume1, perfume2, perfume3):
        print(perfume)
        print("Об'єм:", perfume.get_volume())
        print("Ціна:", perfume.get_price())
        print("Виробник:", perfume.get_brand_name())
        print("Знижка:", perfume.discount)
        print("Категорія:", perfume.category)


main()
