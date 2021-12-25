from bs4 import BeautifulSoup
import requests


def get_hacker_news_git_links() -> set:
    """
    :return: articles with git repositories, filtering by keywords if needed
    """
    keywords = set()
    while need_keyword():
        keywords.add(input("Enter keyword: "))
    else:
        if len(keywords) > 0:
            print(f"Thanks! \nYour keywords: {', '.join(keywords)}")
    return parse_hacker_news_page(keywords)


def need_keyword():
    return input_validation()


def input_validation():
    if input("Add keyword - 1 \nContinue - any other key\nEnter: ") == "1":
        return True
    else:
        return False


def parse_hacker_news_page(keywords: set) -> set:
    """
    :param keywords: keywords for filtering articles
    :return: parsed articles from Hacker News
    """
    articles = []
    url = "https://news.ycombinator.com/news?p="
    max_num_of_pages = 7
    for page_num in range(max_num_of_pages):
        page = requests.get(url + str(page_num))
        soup = BeautifulSoup(page.text, "html.parser")
        article_info = soup.find_all("td", class_="title")
        articles.append(article_info)
    return search_git_repositories(articles, keywords)


def search_git_repositories(articles: list, keywords: set) -> set:
    """
    :param articles: parsed articles from Hacker News
    :param keywords: keywords for filtering articles
    :return: articles that contain git links
    """
    articles_with_git_repos = set()
    for article in articles:
        for article_details in article:
            article_details = article_details.find("a", {"class": "titlelink"})
            if article_details is not None and "github.com" in str(article_details):
                sub_link = article_details.get("href")
                if len(keywords) > 0:
                    if keywords.intersection(str(article_details.text).lower().split()):
                        articles_with_git_repos.add(f"{article_details.text}: {sub_link}")
                else:
                    articles_with_git_repos.add(f"{article_details.text}: {sub_link}")
    return articles_with_git_repos


def print_git_repositories(articles: list or set) -> None:
    [print(article) for article in articles]


if __name__ == '__main__':
    articles_with_git = get_hacker_news_git_links()
    print_git_repositories(articles_with_git)
