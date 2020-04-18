
#      ____ ___      .__  _________       __
#      |    |   \____ |__|/   _____/____ _/  |_
#      |    |   /    \|  |\_____  \\__  \\   __\
#      |    |  /   |  \  |/        \/ __ \|  |
#      |______/|___|  /__/_______  (____  /__|
#              \/           \/     \/

# UniSat Nano-Satellite Educational Program for Girls
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import jinja2
from datetime import datetime

__version__ = '1.0.3'
__license__ = 'MIT'
__Author__ = 'yaakovazat@gmail.com'





def barchart():
    freq = {i: list(result_dict.values()).count(i)
            for i in result_dict.values()}
    fig, ax = plt.subplots()
    points = list(result_dict.values())
    frequency = list([freq[x] for x in result_dict.values()])
    ax.bar(points, frequency)
    ax.set_title('Linux Test Students Scores')
    ax.set_xlabel('Points')
    ax.set_ylabel('Frequency')
    fig.savefig('./.AzatAI/barchart.png')


def scorechart():
    fig, ax = plt.subplots()
    scores = list(result_dict.values())
    students = list(result_dict.keys())
    ax.tick_params(labelrotation=90)
    ax.bar(students, scores)
    ax.set_title('Linux Test Students Scores')
    # ax.set_xlabel('student')
    ax.set_ylabel('score')
    # fig.autofmt_xdate()
    fig.savefig('./.AzatAI/scorechart.png', bbox_inches='tight')


def generate_readme():
    """Generates and saves the report to readme.md"""

    md_table = []
    searchpath = os.path.join(here, '.AzatAI')
    print(searchpath)
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template('README.md')
    index = 0
    for each in result_dict.keys():
        md_table.append(
            f"* {index} {each}  {result_dict[each]} "
        )
        index += 1
    np_array = np.array(list(result_dict.values()))
    content = {
        'total':len(result_dict),
        'result': result_dict,
        'high':max(result_dict.values()),
        'low':min(result_dict.values()),
        'avg': np.mean(np_array),
        'std': np.std(np_array,ddof=1),
        'now':datetime.now(),
    }
    with open('README.md', 'w') as f:
        f.write(template.render(content))


def convert_md():
    """Converts readme.md to report.pdf and index.html"""
    os.system('python -m markdown2 README.md > index.html')
    os.system('weasyprint index.html report.pdf')


if __name__ == "__main__":
    here = os.getcwd()
    report_dir = os.path.join(here, 'report')
    files = glob.glob(f'{report_dir}/*.pdf')
    result = ['.'.join(x.split('.')[:-1]).split('/')[-1].strip() for x in files]
    result_dict = {}
    for each in result:
        student = ' '.join(each.split(' ')[:-1])
        score = float(each.split(' ')[-1])
        result_dict[student] = score
    barchart()
    scorechart()
    generate_readme()
    convert_md()