# -*- coding: utf-8 -*-
class IdolOtaku:

#Read Author/Title/Body in this page.
    def parse_blog_in_page(soup):
        parsed_title = soup.find_all('span', {'class': 'entrytitle'})
        parsed_author = soup.find_all('span', {'class': 'author'})
        parsed_bodie = soup.find_all('div', {'class': 'entrybody'})
        return parsed_title, parsed_author, parsed_bodie

#Get all picture links in this blog.
    def get_blog_pic(soup, assay):
        bodies = soup.find_all('div', {'class': 'entrybody'})
        pic = []
        for piclinks in bodies[assay].find_all('img'):
            piclink = piclinks.get('src')
            if piclink.find('jpeg') > 0:
                pic.append(piclink)
        return pic

#Get all picture links in this page.
    def get_all_pics_link(soup):
        pic = []
        for piclinks in soup.find_all('img'):
            piclink = piclinks.get('src')
            if piclink.find('jpeg') > 0:
                pic.append(piclink)
        return pic

# Check if the title belongs to blog body.
    def title_is_not_blog(title):
        if title.find_all("a") == []:
            return True

# Write Full Page source to txt.
    def full_page_source(soup):
        f = open('htmlsource.txt', 'wb')
        f.write(soup.prettify().encode())
        f.close()
