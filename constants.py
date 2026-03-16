from pathlib import Path


path = Path(__file__).parent
path = path.joinpath("assets")


def load(img: str) -> str:
    return ASSETS[img]


ASSETS = {
    "zoro": str(path.joinpath("characters/zoro-paint.png")),
    "stars": str(path.joinpath("maps/background-image.jpg")),
    "ocean": str(path.joinpath("maps/ocean.jpg")),
    "ocena": str(path.joinpath("maps/ocena-platform.jpg")),
}
