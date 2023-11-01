import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_collector():
    add_collector = BooksCollector()
    add_collector.add_new_book('Гордость и предубеждение и зомби')
    add_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    add_collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    add_collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
    add_collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
    return add_collector
