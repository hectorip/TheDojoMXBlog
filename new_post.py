import begin
from datetime import datetime
from slugify import slugify

template = """---
title: "{}"
date: {}
author: Héctor Patricio
tags:
comments: true
excerpt: ""
header:
  image: #image
---"""

@begin.start(auto_convert=True)
def main(draft=False, *names):
    """ Creates a new file with today's date and title as slug in _posts dir """
    t = datetime.today()
    date = "{}-{:02d}-{:02d}".format(t.year, t.month,t.day)
    directory = "_drafts" if draft else "_posts"
    for name in names:
      
        file_name = "{}/{}-{}.md".format(directory, date, slugify(name))
        with open(file_name, "w") as f:
            f.write(template.format(name, date))
