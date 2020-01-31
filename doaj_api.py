#! /usr/bin/env/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json
import os
import requests
import sys

def main():
    searching = get_input("Welcome! Press 1 to search journals, or 2 to search articles.")
    if searching == "1":
        searching_journals()
    if searching == "2":
        searching_articles()


def searching_journals():
    print("Search query formats: \n - keywords:[your query] - Search by keyword. \n - title:[your query] - Search within the journal's title. \n - issn:[your query] - Search by the journal's ISSN. \n- publisher:[your query] - Search by the journal's publisher (not exact match). \n- license:[your query] - Search by the exact license. \n - Example: keywords:libraries \n \nPlease type your queries and parameters in lowercase. \n")

    query = get_input("Please enter your query: ")
    page_number = get_input("Please enter the page number you would like: ")
    number_results = get_input("Please enter how many results you would like returned: ")
    print("\nSort by title, issn, publisher, or license? Results will automatically be sorted in ascending order; to sort in descending order, specify by typing 'desc' (e.g., title:desc). Otherwise, just type one of the sorting options listed above: \n")
    sorting = get_input("Sort by: ")

    journal_url = "https://doaj.org/api/v1/search/journals/{0}?page={1}&pageSize={2}&sort={3}".format(query, page_number, number_results, sorting)
    response = requests.get(journal_url)

    results = json.loads(response.text)
    print(results)


    save_journals = get_input("Save .json file of results? Type 'y' for yes or 'n' for no.")
    if save_journals == "y":
        with open('journal_search_{}.json'.format(query), 'w') as outfile:
            json.dump(results, outfile)

    search_again = get_input("Search again? Type 'y' for yes, 'n' for no.")

    if search_again == "y":
         main()
    if search_again == "n":
         print("Bye!")
         exit(0)

    if save_journals == "n":
         search_again = get_input("Search again? Type 'y' for yes, 'n' for no.")
         if search_again == "y":
              main()
         if search_again == "n":
             print("Bye!")
             exit(0)

def searching_articles():

    print("Search query formats: \n - title:[your query] - Search within the article title. \n - doi:[your query] - Search by the article's DOI. \n - issn:[your query] - Search by the article's journal's ISSN. \n - publisher:[your query] - Search by the article's journal's publisher. \n - abstract:[your query] - Search within the article's abstract. \n \nPlease type your queries and parameters in lowercase. \n")

    query = get_input("Please enter your query: ")
    page_number = get_input("Please enter the page number you would like: ")
    number_results = get_input("Please enter how many results you would like returned: ")
    print("\nSort by title, issn, publisher, or license? Results will automatically be sorted in ascending order; to sort in descending order, specify by typing 'desc' (e.g., title:desc). Otherwise, just type one of the sorting options listed above: \n")
    sorting = get_input("Sort by: ")

    article_url = "https://doaj.org/api/v1/search/journals/{0}?page={1}&pageSize={2}&sort={3}".format(query, page_number, number_results, sorting)
    response = requests.get(article_url)

    results = json.loads(response.text)
    print(results)


    save_articles = get_input("Save .json file of results? Type 'y' for yes or 'n' for no.")
    if save_articles == "y":
       with open('article_search_{}.json'.format(query), 'w') as outfile:
            json.dump(results, outfile)
       search_again = get_input("Search again? Type 'y' for yes, 'n' for no.")
       if search_again == "y":
           main()
       if search_again == "n":
           print("Bye!") 
           exit(0)
    if save_articles == "n":
        search_again = get_input("Search again? Type 'y' for yes, 'n' for no.")
        if search_again == "y":
           main()
        if search_again == "n":
           print("Bye!") 
           exit(0)

if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    main()
