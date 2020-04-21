# UniSat UNEPG — Linux Test Report
## Part 1 : General test results
<table style="width:100%">
 <tr>
    <th>Index</th>
    <th>Student</th>
    <th>Score</th>
  </tr>{% for each in result.keys() %}
   <tr>
    <th>{{loop.index}}</th>
    <th>{{each}}</th>
    <th>{{result[each]}}</th>
   </tr>{% endfor %}
</table>
## Part 2 : Test Data Analysis

Total Participants: **{{ total }}**

Heighest Score: {{ high }}

Lowest Score: {{ low }}

Avarege Score: {{ avg }}

Standard Variance: {{ std }}

### Data Analysis Result

According to the comprehensive analysis of the various data above, it is found that：

1. The students' overall academic performance is good. 
2. Students have a strong overall acceptance of the course. 
3. The difficulty of the course is moderate. 
4. There is a big difference between the highest and lowest grades of students. 
5. The standard deviation of student performance is relatively large.

### Areas for improvement

According to the large variance of student achievements, it can be found that students have different levels of cognition due to factors such as age and academic qualifications. Therefore, for certain more difficult courses, students can be divided into different groups according to the learning situation,give certain groups more help and guidance.

## Part 3 : Data Visualization

1.  

   ![](./.AzatAI/barchart.png)

2.  

   ![](./.AzatAI/scorechart.png)







NOTE FOR STUDENTS: ** You can download your own report from the `report` folder.**


 Last updated on {{ now }}.

Report Auto-generated by `reporter.py` Done with &#9829; by Yaakov Azat. 