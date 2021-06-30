import pandas as pd
import json
import uuid
from json import JSONEncoder
from uuid import UUID
JSONEncoder_olddefault = JSONEncoder.default
def JSONEncoder_newdefault(self, o):
    if isinstance(o, UUID): return str(o)
    return JSONEncoder_olddefault(self, o)
JSONEncoder.default = JSONEncoder_newdefault

class QAS:
    def setdata(self, question, id, answers):
        self.question = question
        self.id = id
        self.answers = answers

class Answers:
    def setdata(self, answer_start, text):
        self.answer_start = answer_start
        self.text = text


df = pd.read_csv('sample.csv')
def get_nested_rec(grp):
    rec = {}
    rec['id'] = str(grp['id'])
    rec['title'] = grp['title']

    par = {}
    qas = []
    par['context'] = grp['context']
    question_list = list(dict.fromkeys(str(grp['question']).split('|')))
    text_list = list(dict.fromkeys(str(grp['answer_text']).split('|')))

    answers_list = []
    for i in range(len(text_list)):
        tmpTextList = str(text_list[i]).split('_')
        for j in range(len(tmpTextList)):
            answer = Answers()
            answer.setdata(str(par['context']).find(tmpTextList[j]), tmpTextList[j])
            answers_list.append(answer.__dict__)
        qas_data = QAS()
        qas_data.setdata(question_list[i], uuid.uuid1(), answers_list)
        qas.append(qas_data.__dict__)
        answers_list = []


    par['qas'] = qas

    rec['paragraphs'] = par

    return rec

records = []
for grp in df.iterrows():
    rec = get_nested_rec(grp[1])
    records.append(rec)

records = dict(data = records)
with open("sample.json", 'w', encoding='UTF-8') as f:
    f.write(json.dumps(records, ensure_ascii=False, indent=4))