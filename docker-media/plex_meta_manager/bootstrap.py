import re, os

s = ''
with open('/data/input') as f:
    s = f.read()

for var in set(re.findall(r'\${([A-Za-z_]+)}', s)):
    val = os.environ.get(var)
    if val is None:
        print(f'failed to find env variable for {var}')
        continue
    print(f'replacing ${{{var}}} with {val}')
    s = s.replace(f'${{{var}}}', val)

with open('/data/output', 'w') as f:
    f.write(s)

