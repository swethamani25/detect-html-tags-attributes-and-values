import re
num_lines = input()
lines = [raw_input() for i in xrange(num_lines)]
text = ' '.join(lines)
text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)

from HTMLParser import HTMLParser
class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for name, val in attrs:
            print '->', name, '>', val

Parser().feed(text)