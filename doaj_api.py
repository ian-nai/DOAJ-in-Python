import urllib2
import os
import json

def API_Main():
    searching = raw_input("Welcome! Press 1 to search journals, or 2 to search articles.")
    if searching == "1":
        searching_journals()
    if searching == "2":
        searching_articles()


def searching_journals():
    print "Search query formats: \n - keywords:[your query] - Search by keyword. \n - title:[your query] - Search within the journal's title. \n - issn:[your query] - Search by the journal's ISSN. \n- publisher:[your query] - Search by the journal's publisher (not exact match). \n- license:[your query] - Search by the exact license. \n - Example: keywords:libraries \n \nPlease type your queries and parameters in lowercase. \n"

    query = raw_input("Please enter your query: ")
    number_results = raw_input("Please enter how many results you would like returned: ")
    print("\nSort by title, issn, publisher, or license? Results will automatically be sorted in ascending order; to sort in descending order, specify by typing 'desc' (e.g., title:desc). Otherwise, just type one of the sorting options listed above: \n")
    sorting = raw_input("Sort by: ")

    journal_url = "https://doaj.org/api/v1/search/journals/bibjson.{0}?pageSize={1}&sort={2}".format(query, number_results, sorting)
    response = urllib2.urlopen(journal_url)

    response2 = json.loads(response.read())
    print response2


    save_journals = raw_input("Save .json file of results? Type 'y' for yes or 'n' for no.")
    if save_journals == "y":
        with open('journal_search.json', 'w') as outfile:
            json.dump(response2, outfile)

    search_again = raw_input("Search again? Type 'y' for yes, 'n' for no.")

    if search_again == "y":
         API_Main()  
    if search_again == "n":
         print("Bye!")
         exit(0)

    if save_journals == "n":
         search_again2 = raw_input("Search again? Type 'y' for yes, 'n' for no.")
         if search_again2 == "y":
              API_Main()
         if search_again2 == "n":
             print("Bye!")
             exit(0)

def searching_articles():

    print "Search query formats: \n - title:[your query] - Search within the article title. \n - doi:[your query] - Search by the article's DOI. \n - issn:[your query] - Search by the article's journal's ISSN. \n - publisher:[your query] - Search by the article's journal's publisher. \n - abstract:[your query] - Search within the article's abstract. \n \nPlease type your queries and parameters in lowercase. \n"

    query2 = raw_input("Please enter your query: ")
    number_results2 = raw_input("Please enter how many results you would like returned: ")
    print("\nSort by title, issn, publisher, or license? Results will automatically be sorted in ascending order; to sort in descending order, specify by typing 'desc' (e.g., title:desc). Otherwise, just type one of the sorting options listed above: \n")
    sorting2 = raw_input("Sort by: ")

    article_url = "https://doaj.org/api/v1/search/journals/bibjson.{0}?pageSize={1}&sort={2}".format(query2, number_results2, sorting2)
    response3 = urllib2.urlopen(article_url)

    response4 = json.loads(response3.read())
    print response4


    save_articles = raw_input("Save .json file of results? Type 'y' for yes or 'n' for no.")
    if save_articles == "y":
       with open('article_search.json', 'w') as outfile2:
            json.dump(response4, outfile2)
       search_again3 = raw_input("Search again? Type 'y' for yes, 'n' for no.")
       if search_again3 == "y":
           API_Main()
       if search_again3 == "n":
           print("Bye!") 
           exit(0)
    if save_articles == "n":
        search_again4 = raw_input("Search again? Type 'y' for yes, 'n' for no.")
        if search_again4 == "y":
           API_Main()
        if search_again4 == "n":
           print("Bye!") 
           exit(0)
API_Main()
