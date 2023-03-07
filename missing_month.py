#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : missing_month.py.py
@Time : 3/24/22 12:03 AM
@Desc:
In django, when use TruncMonth(showing count or sum value month wise) function it returns only months which are exist
in the database field or columns.So for showing missing month, you can user this approach.
This example shows a list with previous 12 months data.
"""

import datetime
now = datetime.datetime.now()

result = [{
    'year': now.strftime("%Y"),
    'month': now.strftime("%b"),
    "total": 0
}]
# Making previous 12 months
for _ in range(0, 11):
    now = now.replace(day=1) - datetime.timedelta(days=1)
    result.append({
        'year': now.strftime("%Y"),
        'month': now.strftime("%b"),
        "total": 0
    })

# new_result = sorted(result, key=lambda d: d['year'])
# result.reverse()
# print(result)

original_date = [{'year': '2021', 'month': 'Apr', 'total': 0}, {'year': '2021', 'month': 'May', 'total': 0},
                 {'year': '2021', 'month': 'Jun', 'total': 0}, {'year': '2021', 'month': 'Jul', 'total': 0},
                 {'year': '2021', 'month': 'Aug', 'total': 0}, {'year': '2021', 'month': 'Sep', 'total': 0},
                 {'year': '2021', 'month': 'Oct', 'total': 0}, {'year': '2021', 'month': 'Nov', 'total': 0},
                 {'year': '2021', 'month': 'Dec', 'total': 0}, {'year': '2022', 'month': 'Jan', 'total': 0},
                 {'year': '2022', 'month': 'Feb', 'total': 0}, {'year': '2022', 'month': 'Mar', 'total': 0}]

query_data = [{'year': '2021', 'month': 'May', 'total': 15}, {'year': '2021', 'month': 'Jun', 'total': 7},
              {'year': '2021', 'month': 'Jul', 'total': 2}, {'year': '2021', 'month': 'Aug', 'total': 1},
              {'year': '2021', 'month': 'Sep', 'total': 13}, {'year': '2021', 'month': 'Oct', 'total': 4},
              {'year': '2021', 'month': 'Nov', 'total': 3}, {'year': '2021', 'month': 'Dec', 'total': 8},
              {'year': '2022', 'month': 'Jan', 'total': 4}, {'year': '2022', 'month': 'Mar', 'total': 1}]

output = []
for e2 in original_date:
    found = False
    for e1 in query_data:
        if e1['year'] == e2['year'] and e1['month'] == e2['month']:
            output.append(e1)
            found = True
            break
    if not found:
        output.append(e2)
print(output)
