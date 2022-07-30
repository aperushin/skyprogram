from dataclasses import dataclass
from file_utils import load_json
from config import COMMENTS_FILE


@dataclass(slots=True)
class Post:

    poster_name: str
    poster_avatar: str
    pic: str
    content: str
    views_count: int
    likes_count: int
    pk: int

    @property
    def content_short(self) -> str:
        if len(self.content) > 50:
            return self.content[:50] + ' …'
        return self.content

    @property
    def content_tagged(self):
        result = []

        for word in self.content.split():
            if word.startswith('#') and len(word) > 1:
                word_stripped = word.lstrip('#').lower()
                linked_hashtag = f'<a href="/tag/{word_stripped}">{word}</a>'
                result.append(linked_hashtag)
            else:
                result.append(word)

        return ' '.join(result)

    @property
    def comments(self):
        """Get comments for post"""
        all_comments = load_json(COMMENTS_FILE)
        result = []
        for comment in all_comments:
            if comment['post_id'] == self.pk:
                result.append(comment)
        return result

    @property
    def comments_count(self) -> str:
        """Get a string with comments count"""
        count = len(self.comments)
        ending = get_ending(count)
        result = f'{count} комментари{ending}'
        return result


def get_ending(number: int) -> str:
    """
    Возвращает окончание слова, согласующееся с числительным

    Версия для слова "комментарий"
    """
    n_abs = abs(number)
    last_digit = n_abs % 10
    if (10 < (n_abs % 100) < 15) or last_digit > 4 or last_digit == 0:
        return 'ев'
    if last_digit == 1:
        return 'й'
    if 2 <= last_digit <= 4:
        return 'я'
