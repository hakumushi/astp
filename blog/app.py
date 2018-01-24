from blog import Blog


MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
blogs = dict()


def menu():
    print_blogs()

    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))


def ask_read_blog():
    title = input('Enter the blog title you want to read: ')
    for post in blogs[title]:
        print(post)


def ask_create_post():
    title = input('Type the blog title: ')
    post_title = input('Type the post title: ')
    content = input('Type the post content: ')
    blogs[title].create_post(post_title, content)


