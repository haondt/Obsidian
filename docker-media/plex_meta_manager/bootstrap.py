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


# regex to keep existing trakt auth data
p = r'(trakt:[\n ]*\n(?:\s{2}[#A-Za-z][^\n]+(?:[\n ]*\n))*)(\s{2}authorization:[\n ]*?(?:[\n ]*\n {4}[#A-Za-z][^\n]+)*)'
of = ''
with open('/data/output') as f:
    of = f.read()
if re.search(p, of) and re.search(p, s):
    go = re.search(p, of).groups()
    gi = re.search(p, s).groups()
    if len(go) == 2 and len(gi) == 2:
        s = re.sub(p, gi[0] + go[1], s)

with open('/data/output', 'w') as f:
    f.write(s)

