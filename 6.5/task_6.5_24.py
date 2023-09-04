from collections import defaultdict


def best_sender(messages, senders):
    res_dict = defaultdict(list)
    for sender, message in zip(senders, messages):
        res_dict[sender].extend(message.split())
    return max(res_dict.items(), key=lambda x: (len(x[1]), x[0]))[0]


messages = ['hi', 'hello', 'how r u', 'i am okay',
            'how r u', 'i am okay too thanks']
senders = ['Anri', 'Dima', 'Anri', 'Dima', 'Dima', 'Anri']

print(best_sender(messages, senders))
