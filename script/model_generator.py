import csv

f = open('nf1.csv', 'r')
data = list(csv.reader(f))
f.close()

field_map = {
    '단어(character)': 'models.CharField',
    '자연수(positive integer)': 'models.PositiveIntegerField',
    '소수점이있는실수(decimal)': 'models.DecimalField',
    '줄글(text)': 'models.TextField',
    '날짜(date)': 'models.DateField',
    '날짜와시각(datetime)': 'models.DateField',
    '선택이있는데이터(choices)': 'models.IntegerField',
}

print([row[0] for row in data[2:]])

for row in data[2:]:
    field = {
        'column_name': row[0],
        'display_name': row[1],
        'help_text': row[2].replace("\n", "<br/>"),
        'field_type': row[3],
    }
    if len(row[6]) > 0:
        field['choice_count'] = int(row[6]) + 1
    else:
        field['choice_count'] = 0
    # print(field)

    # TODO(좀 더 이쁘게 바꾸고싶음..)
    field_text = f"{field['column_name']} = {field_map[field['field_type']]}('{field['display_name']}'"
    if field['field_type'] == '선택이있는데이터(choices)':
        field_text += f", choices=[(i, i) for i in range({field['choice_count']})], null=True, blank=True"
    elif field['field_type'] == '소수점이있는실수(decimal)':
        field_text += f", max_digits=10, decimal_places=2, null=True, blank=True"
    else:
        field_text += f", null=True, blank=True"

    if len(field['help_text']) > 0:
        field_text += f", help_text='{field['help_text']}'"

    field_text += ")"

    print(field_text)


