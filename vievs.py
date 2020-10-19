def index():
    with open('index.html') as idex_page:
        return idex_page.read()


def blog():
    with open('blog.html') as blog_page:
        return blog_page.read()
