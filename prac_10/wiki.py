
import wikipedia

search_content = input("What do you want to search? :")
while search_content:
    search_results = wikipedia.search(search_content)
    print(search_results)
    page = wikipedia.page(search_results)
    print(page.title)
    print(wikipedia.summary(search_results))
    print(page.url)

    search_content = input("What do you want to search? :")
