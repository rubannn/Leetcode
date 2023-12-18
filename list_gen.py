from pathlib import Path
import os
import re
import requests


lnk = "https://leetcode.com/problems/design-a-food-rating-system/"


def get_task_data(url):
    titleSlug = [x for x in url.split("/") if x][-1]
    posturl = "https://leetcode.com/graphql"
    data = {
        "operationName": "questionData",
        "variables": {"titleSlug": titleSlug},
        "query": "query questionData($titleSlug: String!) {\n question(titleSlug: $titleSlug) {\n questionFrontendId\n title\n difficulty\n codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    } \n}\n}\n",
    }

    # data = {"operationName":"questionData","variables":
    # {"titleSlug":titleSlug},
    # "query":"query questionData($titleSlug: String!)
    # {\n  question(titleSlug: $titleSlug) {\n    questionId\n
    # questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n
    # translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n
    #      likes\n    dislikes\n    isLiked\n    contributors
    # {\n      username\n      profileUrl\n      avatarUrl\n
    #  __typename\n    } \n  langToValidPlayground\n
    # topicTags {\n      name\n      slug\n translatedName\n
    #   __typename\n    }\n companyTagStats\n
    #  codeSnippets {\n      lang\n      langSlug\n      code\n
    # __typename\n    }\n  stats\n    hints\n
    # judgerAvailable\n    judgeType\n  mysqlSchemas\n    enableRunCode\n
    # enableTestMode\n    libraryUrl\n    __typename\n  }\n}\n"}

    r = requests.post(posturl, json=data).json()["data"]["question"]
    id = r["questionFrontendId"]
    title = r["title"]
    difficulty = r["difficulty"]
    codelangs = [langinfo["lang"] for langinfo in r["codeSnippets"]]
    extention = ".sql" if any(["SQL" in c for c in codelangs]) else ".py"
    return {"id": id, "title": title, "difficulty": difficulty, "file_ext": extention}


def tryint(t):
    try:
        res = int(t)
    except ValueError:
        res = None
    return res


color = {"Easy": "green", "Medium": "orange", "Hard": "red"}
folder = [
    "0001 - 0250",
    "0251 - 0500",
    "0501 - 0750",
    "0751 - 1000",
    "1001 - 1250",
    "1251 - 1500",
    "1501 - 1750",
    "1751 - 2000",
    "2001 - 2250",
    "2251 - 2500",
    "2501 - 2750",
    "2751 - 3000",
]

task = get_task_data(lnk)
tid = int(task["id"])
title = task["title"]
ext = task["file_ext"]
hard = f"${{\\color{{{color[task['difficulty']]}}}{task['difficulty']}}}$"

for fld in folder:
    left, right = [tryint(x.strip()) for x in fld.split("-")]
    if (left <= tid) and (right is None or tid <= right):
        foldername = fld
        code = fld.replace(" ", "%20")

codelink = f"(/rubannn/Leetcode/tree/main/{code}/{tid:04d}{ext})"
mask = f"| `{tid:04d}` | [{title}]({lnk}) |{hard}|[\\</code\\>]{codelink} |\n"

with open(Path("README.md"), "r") as f:
    content = f.readlines()

newcontent = []
can_write = True
for c in content:
    if "| `" in c:
        cid = int(c.split("|")[1].strip(" `"))
        if tid == cid:
            print("Double record!!!")
            can_write = False
        elif tid < cid and can_write:
            newcontent.append(mask)
            Path(f"{foldername}/{tid:04d}{ext}").write_text("")
            can_write = False
    newcontent.append(c)

if can_write:
    newcontent.append(mask)

Path("README.md").write_text("".join(newcontent))

with open(Path("README.md"), "r") as f:
    content = f.readlines()

solved = {"Easy": -1, "Medium": -1, "Hard": -1}

pattern = r"\d{4}\.(py|sql)"
regex = re.compile(pattern)
names_in_md = []
for cont in content:
    match = regex.search(cont)
    if match:
        names_in_md.append(match.group(0))
    for kind in solved.keys():
        if f"{kind}}}$" in cont:
            solved[kind] += 1

solved["Total"] = sum(solved.values())
content[5] = f"|{' | '.join(f'**{v}**' for k, v in solved.items())}|\n"

folder = os.getcwd()
total_files = 0
names_real = []
for root, dirs, files in os.walk(folder):
    if " - " in root:
        total_files += len(files)
        names_real += files

if solved["Total"] != total_files:
    print(
        f"\tWarning not all files sync with Git! \
          \n\t\t[Lost {solved['Total'] - total_files} files...]\
          \n\t\tReadme names: {list(set(names_in_md) - set(names_real))}\
          \n\t\tFiles: {list(set(names_real) - set(names_in_md))}"
    )

Path("README.md").write_text("".join(content))
print(task, solved, sep="\n")
