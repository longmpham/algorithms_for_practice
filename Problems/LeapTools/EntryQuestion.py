"""
Given the JSON object {"sku": "VA-43", "size": "5ft", "name": "Blue Sky", "description": "A great product!"}

Change it to match the following spec:

1) All values must be lowercase.

2) Values may contain only alphanumeric characters, underscores or dots. All other characters must be replaced with underscores.
2a) start/end with . or _
							r'[^a-zA-Z0-9\_\.]'
2b)	does not start/end with . or _
							r^[a-zA-Z0-9][\w\.]+[a-zA-Z0-9]$

3) "description" is a special property, to which none of the above specifications apply.

4) If any value has more than 10 characters, trim it at 10 characters and add three trailing dots.

5) Convert imperial units into metric. For distance, use meters.
	* assumption, units in description does not exist because of explicit field.
"""

import re


def convert(string):
	# add to metrics as necessary.
	metrics = {
		'lb': [453.592, 'g'],
		'ft': [0.3048, 'm'],
	}
	regex_pattern = r'[^a-zA-Z0-9\_\.]'
	new_string = {}

	print(str)

	for key, val in string.items():

		# condition 3 ignores all conditions if in description
		if(key is not 'description'):
			# condition 1 changes values to lowercase
			val = val.lower()
			# condition 2 changes string to a regex (alphanum, _ and . only)
			val = re.sub(regex_pattern, '_', val)
			# if val is not in regex:
				# change val[char] to '_'.
			# else: if it does match so just skip (dont have to code this else! :) )

		# condition 4: trim string to 10 chars and add trailing '...'
		if (len(val) > 10):
			val = val[:10] + '...'


		# condition 5: change imperial to metric
		if (key is 'size'):
			# parse the number and the unit [ VALUE/UNIT ]
			regex_match = re.findall(r'[A-Za-z]+|\d+', val)
			size_val = float(regex_match[0])
			size_unit = regex_match[1]

			if(size_unit in metrics):
				new_unit = metrics[size_unit][1]
				conversion_ratio = metrics[size_unit][0]
				new_val = size_val * conversion_ratio
				new_val = '{}{}'.format(new_val, new_unit)
				val = new_val

		# save the new string 
		new_string[key] = val

	return new_string


str = {
"sku": "VA-43", 
"size": "52ft", 
"name": "Blue Sky", 
"description": "A great product!"
}

print(convert(str))