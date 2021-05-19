ejkvne;oranv
2491r8h1239de-wfj\а53гар3490йа349-349йва932в-23-2в923
кшотм93тм9034ат4390гат49гта
countries = [
	(42, 'Russia'),
	(36, 'Germany'),
	(8, 'USA'),
	(38, 'France'),
	(42, 'Russia'),
	(42, 'Russia'),
	(42, 'Russia'),
	(42, 'Russia'),
	(42, 'Russia'),
	(36, 'Germany'),
	(36, 'Germany'),
	(36, 'Germany'),
	(36, 'Germany'),
	(36, 'Germany'),
	(24, 'Great Briatin')
]
sizes_list = ['xxs', 'xs', 's', 'm', 'l', 'xl', 'xxl', 'xxxl']
sizes = {}
for size in sizes_list:
	for country in countries:
		num = country[0]
		sizes[size].update({country[1]: list(range(num, num+16,2))})
print(sizes)
