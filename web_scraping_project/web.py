import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_article_content(url, session):
    """Fetch the main text of an article from its URL."""
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract article paragraphs
        paragraphs = soup.find_all("p")
        content = " ".join(p.get_text(strip=True) for p in paragraphs)
        return content if content else "Content not available"
    except Exception as e:
        print(f"Error fetching article content from {url}: {e}")
        return "Content not available"

def scrape_nyt_articles(sections, max_articles=500, pages_per_section=10):
    articles = []
    visited_urls = set()
    session = requests.Session()

    # Set a User-Agent header to mimic a browser request
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    })

    section_index = 0  # Start with the first section (Business)
    pages_scraped = 0  # Counter for the number of pages scraped

    while len(articles) < max_articles and section_index < len(sections):
        section_url = sections[section_index]
        page_number = 1  # Start from page 1 for the current section
        
        print(f"\nScraping {section_url}...")

        while pages_scraped < pages_per_section * (section_index + 1) and len(articles) < max_articles:
            current_url = f"{section_url}?page={page_number}"
            print(f"Scraping page {page_number}...")

            try:
                # Fetch the main page content using the session
                response = session.get(current_url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
            except Exception as e:
                print(f"Error fetching {current_url}: {e}")
                break  # If there's an error, stop the loop

            # Extract article links
            for link_tag in soup.find_all("a", href=True):
                url = link_tag['href']
                if "/2024/" in url:  # Filter links to articles (assuming URL contains year, can be adjusted)
                    full_url = f"https://www.nytimes.com{url}" if not url.startswith("http") else url
                    if full_url not in visited_urls and len(articles) < max_articles:
                        content = get_article_content(full_url, session)
                        if content and content != "Content not available":
                            title = link_tag.get_text(strip=True) or "No title available"
                            articles.append({"Title": title, "URL": full_url, "Content": content})
                            visited_urls.add(full_url)
                            print(f"Scraped ({len(articles)}/{max_articles}): {title}")

            page_number += 1  # Move to the next page
            pages_scraped += 1
            time.sleep(2)  # Be polite to the server

        # Move to the next section after finishing 10 pages
        section_index += 1

    # Save to a CSV file
    df = pd.DataFrame(articles)
    df.to_csv("nyt_articles.csv", index=False)
    print(f"\nScraping completed! {len(articles)} articles saved to nyt_articles.csv")

# Run the scraper
if __name__ == "__main__":
    # List of sections to scrape (Business, Lifestyle, World)
    sections = [
        "https://www.nytimes.com/section/business", 
        "https://www.nytimes.com/spotlight/lifestyle", 
        "https://www.nytimes.com/section/world"
    ]
    scrape_nyt_articles(sections, max_articles=500, pages_per_section=10)
