import sys


res = [int(line) for line in sys.stdin]
if not res:
    print('нет учеников')
else:
    print(f'Рост самого низкого ученика: {min(res)}\n'
          f'Рост самого высокого ученика: {max(res)}\n'
          f'Средний рост: {sum(res) / len(res)}')
