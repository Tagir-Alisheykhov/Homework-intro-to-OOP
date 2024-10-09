from src.utils import create_objects_from_json


def main() -> list:
    """Объединяет в себе весь функционал программы"""
    return create_objects_from_json()


if __name__ == "__main__":
    print(main())
