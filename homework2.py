seconds = int(input('Количество секунд '))
hours = seconds // 3600
hours = hours % 24
minutes = seconds // 60
minutes = minutes % 60
seconds = seconds % 60
print(f"{hours}:{minutes}:{seconds}")





