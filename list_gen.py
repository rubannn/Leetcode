import requests
from pathlib import Path

lnk = 'https://leetcode.com/problems/calculate-money-in-leetcode-bank/'


def get_task_data(url):
    titleSlug = [x for x in url.split('/') if x][-1]
    posturl = 'https://leetcode.com/graphql'
    data = {"operationName": "questionData",
            "variables": {"titleSlug": titleSlug},
            "query": "query questionData($titleSlug: String!) {\n question(titleSlug: $titleSlug) {\n questionFrontendId\n title\n difficulty\n}\n}\n"}

    r = requests.post(posturl, json=data).json()['data']['question']
    id = r['questionFrontendId']
    title = r['title']
    difficulty = r['difficulty']
    return {'id': id, 'title': title, 'difficulty': difficulty}


def tryint(t):
    try:
        res = int(t)
    except ValueError:
        res = None
    return res


color = {'Easy': 'green', 'Medium': 'orange', 'Hard': 'red'}
folder = ['0001 - 0250', '0251 - 0500', '0751 - 1000',
          '1001 - 2000', '2001 - 2xxx']
task = get_task_data(lnk)
tid = int(task['id'])
hard = f"${{\\color{{{color[task['difficulty']]}}}{task['difficulty']}}}$"

for fld in folder:
    left, right = [tryint(x.strip()) for x in fld.split('-')]
    if (left <= tid) and (right is None or tid <= right):
        code = fld.replace(' ', '%20')

codelink = f"/rubannn/Leetcode/tree/main/{code}/{tid:04d}.py"
mask = f"| `{tid:04d}` | [{task['title']}]({lnk}) | {hard} | [code]({codelink}) |\n"

with open(Path("README.md"), "r") as f:
    content = f.readlines()


newcontent = []
can_write = True
for c in content:
    if '| `' in c:
        cid = int(c.split('|')[1].strip(' `'))
        if tid == cid:
            print('Double record!!!')
            can_write = False
        elif tid < cid and can_write:
            newcontent.append(mask)
            can_write = False
    newcontent.append(c)

if can_write:
    newcontent.append(mask)

print(task)
Path("README.md").write_text(''.join(newcontent))
