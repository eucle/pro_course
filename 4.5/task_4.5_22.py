from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        json_string = json.loads(string)
        return True
    except:
        return False


def verify_and_add_player(player):
    if player['team'] == 'Arsenal':
        res.append(player['first_name'] + ' ' + player['last_name'])


res: list = []
with ZipFile('data.zip', mode='r') as zip_file:
    for obj in zip_file.infolist():
        if not obj.is_dir():
            with zip_file.open(obj.filename) as file:
                try:
                    string = file.read().decode('utf-8')
                    if is_correct_json(string):
                        verify_and_add_player(json.loads(string))
                except:
                    pass
res.sort()
print(*res, sep='\n')
