from flask import Blueprint, render_template, request

from .utils import search_for_posts

# Create blueprint
search = Blueprint('search', __name__, template_folder='templates')


@search.get('/search/')
def page_search():
    query = request.args.get('s')

    if not query:
        # If no arguments provided, render an empty search page
        return render_template('search.html')

    posts_found = search_for_posts(query)
    results_count = len(posts_found)
    return render_template(
        'search.html',
        posts=posts_found,
        results_count=results_count,
        query=query
    )


@search.get('/tag/<tag_name>')
def page_tag(tag_name):
    hashtag = '#' + tag_name
    posts = search_for_posts(hashtag)
    return render_template('tag.html', posts=posts, tag=tag_name)
