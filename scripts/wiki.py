import wikipediaapi

print('imported')


wiki_wiki = wikipediaapi.Wikipedia(
        language='tr',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)


page_py = wiki_wiki.page('asal sayılar')
if page_py.exists():
    print(page_py.summary)
else:
    print('Page does not exist')





