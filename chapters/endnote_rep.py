import re, glob

for f in glob.glob('*.tex'):
    t = open(f, encoding='utf-8').read()
    print(re.findall(r'(\S+ \S+)\\endnote{(?:\\lr{)?(.+?)(?:})?}', t))
    t = re.sub(r'(\S+ \S+)\\endnote{(?:\\lr{)?(.+?)(?:})?}', lambda x: '\\پاورق{'+x.group(1)+'}{'+x.group(2)+'}', t)
    open(f, 'w', encoding='utf-8').write(t)
