# Google-Search-Python
🎗 Search and get full query for search

used mudules ```requests, bs4```

first ```pip install requests bs4```

```python
from googlesearch import (
    getQuery,
    searchQuery
)

cls = searcher(userAgent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0")

print(cls.search_query("khazar sea")) # -> (title, link)
    # > [('Caspian Sea: Largest Inland Body of Water - Live Science', 'https://www.livescience.com/57999-caspian-sea-facts.html')...

print(cls.get_query("khazar sea")) # -> get full query
    # > ['khazar sea', 'khazar sea shipping lines', 'are sea shepherds still active', 'who are the hasidim'...
```
