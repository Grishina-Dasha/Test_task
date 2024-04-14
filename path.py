import os

# путь к текущей папке
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_ROOT_PATH)
# путь к папке с файлами
OUTPOOT_PATH = os.path.join(PROJECT_ROOT_PATH, "output")
print(OUTPOOT_PATH)
