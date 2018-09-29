
from pathlib import Path
p = Path('F:\python程序\第10周\作业')
for i in p.iterdir():
    if i.suffix == '.py':
        print(i.name)
