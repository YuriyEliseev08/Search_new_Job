from src.saves import JsonSave
from src.iterration import user_interaction

# стираем фаил json из пребедущего цикла если есть
JsonSave.delete_file()
user_interaction()
