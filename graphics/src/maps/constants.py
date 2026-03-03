from pathlib import Path


path = Path(__file__).parent
path = path.joinpath("assets")


ASSETS = {
    "background": str(path.joinpath("background-image.jpg"))
}