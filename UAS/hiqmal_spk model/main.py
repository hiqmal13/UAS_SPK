import sys
from colorama import Fore, Style
from models import Base, Smartphone
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import (
    DEV_SCALE_brand,
    DEV_SCALE_ram,
    DEV_SCALE_prosesor,
    DEV_SCALE_storage,
    DEV_SCALE_baterai,
    DEV_SCALE_harga,
    DEV_SCALE_ukuran_layar,
)

session = Session(engine)


def create_table():
    Base.metadata.create_all(engine)
    print(f"{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!")


class BaseMethod:
    def __init__(self):
        # 1-5
        self.raw_weight = {
            "brand": 5,
            "ram": 3,
            "prosesor": 4,
            "storage": 3,
            "baterai": 4,
            "ukuran_layar": 3,
            "harga": 1,
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v / total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(Smartphone)
        return [
            {
                "id": ponsel.id,
                "brand": DEV_SCALE_brand.get(ponsel.brand, 0),
                "ram": DEV_SCALE_ram.get(ponsel.ram, 0),
                "prosesor": DEV_SCALE_prosesor.get(ponsel.prosesor, 0),
                "storage": DEV_SCALE_storage.get(ponsel.storage, 0),
                "baterai": DEV_SCALE_baterai.get(ponsel.baterai, 0),
                "ukuran_layar": DEV_SCALE_ukuran_layar.get(ponsel.ukuran_layar, 0),
                "harga": DEV_SCALE_harga.get(ponsel.harga, 0),
            }
            for ponsel in session.scalars(query)
        ]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brand = []  # max
        ram = []  # max
        prosesor = []  # max
        storage = []  # max
        baterai = []  # max
        ukuran_layar = []  # max
        harga = []  # min
        for data in self.data:
            brand.append(data["brand"])
            ram.append(data["ram"])
            prosesor.append(data["prosesor"])
            storage.append(data["storage"])
            baterai.append(data["baterai"])
            ukuran_layar.append(data["ukuran_layar"])
            harga.append(data["harga"])

        # Handling empty lists
        max_brand = max(brand) if brand else 0
        max_ram = max(ram) if ram else 0
        max_prosesor = max(prosesor) if prosesor else 0
        max_storage = max(storage) if storage else 0
        max_baterai = max(baterai) if baterai else 0
        max_ukuran_layar = max(ukuran_layar) if ukuran_layar else 0
        min_harga = min(harga) if harga else 0

        return [
            {
                "id": data["id"],
                "brand": data["brand"] / max_brand if max_brand != 0 else 0,  # benefit
                "ram": data["ram"] / max_ram if max_ram != 0 else 0,  # benefit
                "prosesor": data["prosesor"] / max_prosesor
                if max_prosesor != 0
                else 0,  # benefit
                "storage": data["storage"] / max_storage
                if max_storage != 0
                else 0,  # benefit
                "baterai": data["baterai"] / max_baterai
                if max_baterai != 0
                else 0,  # benefit
                "ukuran_layar": data["ukuran_layar"] / max_ukuran_layar
                if max_ukuran_layar != 0
                else 0,  # benefit
                "harga": min_harga / data["harga"] if data["harga"] != 0 else 0,  # cost
            }
            for data in self.data
        ]


class WeightedProduct(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {
            row["id"]: round(
                row["brand"] ** weight["brand"]
                * row["ram"] ** weight["ram"]
                * row["prosesor"] ** weight["prosesor"]
                * row["storage"] ** weight["storage"]
                * row["baterai"] ** weight["baterai"]
                * row["ukuran_layar"] ** weight["ukuran_layar"]
                * row["harga"] ** weight["harga"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))


class SimpleAdditiveWeighting(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result = {
            row["id"]: round(
                row["brand"] * weight["brand"]
                + row["ram"] * weight["ram"]
                + row["prosesor"] * weight["prosesor"]
                + row["storage"] * weight["storage"]
                + row["baterai"] * weight["baterai"]
                + row["ukuran_layar"] * weight["ukuran_layar"]
                + row["harga"] * weight["harga"],
                2,
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x: x[1]))


def run_saw():
    saw = SimpleAdditiveWeighting()
    print("result:", saw.calculate)


def run_wp():
    wp = WeightedProduct()
    print("result:", wp.calculate)


if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg == "create_table":
        create_table()
    elif arg == "saw":
        run_saw()
    elif arg == "wp":
        run_wp()
    else:
        print("command not found")
