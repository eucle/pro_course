import csv
import json


results: dict = {}
with open('exam_results.csv', 'r', encoding='utf-8') as file:
    for n, sur, sco, d, e in list(csv.reader(file))[1:]:
        results[e] = results.setdefault(e, {})
        results[e]['name'] = n
        results[e]['surname'] = sur
        results[e]['best_score'] = (results[e].get('best_score', []) +
                                    [(int(sco), d)])
        results[e]['date_and_time'] = results[e].get('date_and_time', []) + [d]
        results[e]['email'] = e

best_scores: list = []
for key in sorted(results):
    res: dict = {}
    res['name'] = results[key]['name']
    res['surname'] = results[key]['surname']
    res['best_score'] = max(results[key]['best_score'])[0]
    res['date_and_time'] = results[key]['date_and_time'][results[key]['best_score'].index(max(results[key]['best_score']))]
    res['email'] = results[key]['email']
    best_scores.append(res)

with open('best_scores.json', 'w', encoding='utf-8') as out_file:
    json.dump(best_scores, out_file, indent=3)
