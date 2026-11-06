from .app import App
from .config import Settings


def main():
    App(Settings()).run()


if __name__ == "__main__":
    main()