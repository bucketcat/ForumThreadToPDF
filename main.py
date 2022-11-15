import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


# the whtmltopdf path settings above are very important, since it was the only way I managed to get it to work,
# even after setting it both as sys and env path variable and directly pointing to it. Above solution is the only,
# thing that worked, courtesy of some stackOverflow poster


class Counter:
    def __init__(self, low, high):
        self.current = low - 1
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):  # Python 2: def next(self)
        self.current += 1
        if self.current < self.high:
            return self.current
        raise StopIteration


# specify page range of forum post you want to save as PDF,
# works both for printable versions and regular version if page numbering is sequential and consistent.

# page 1 is 0

for c in Counter(0, 2):
    pdfkit.from_url('https://dbsoft.org/forum/printthread.php?tid=1&page={0}'.format(c), "name{0}.pdf".format(c),
                    configuration=config)

# also works for forums of following format
# pdfkit.from_url('https://forums.tomshardware.com/threads/vintage-pc-technology-mega-discussion-thread.2817216/page={0}'.format(c),
#                   "name{0}.pdf".format(c),configuration=config)
