    articles = []
        try:
            # Wait for articles to load, maybe increase this timeout
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.gs-c-promo-heading"))
            )
            
            # Find article elements
            article_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.gs-c-promo-heading")
            self.logger.info(f"Found {len(article_elements)} article elements")
            for element in article_elements:
                title = element.text.strip()
                link = element.get_attribute("href")
                if link and link not in self.visited_urls:
                    self.visited_urls.add(link)
                    articles.append({"Title": title, "Link": link})
        except Exception as e:
            self.logger.error(f"Error while extracting articles: {e}", exc_info=True)  # Log the exception details
        
        return articles