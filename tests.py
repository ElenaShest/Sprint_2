from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books_result_two_books(self, add_collector):
        assert len(add_collector.get_books_genre()) == 2

    def test_dict_books_genre_is_empty(self, collector):
        assert len(collector.get_books_genre()) == 0

    def test_list_genre_has_five_genres(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_add_long_name_empty_dict(self, collector):
        collector.add_new_book('12345678910121314151617181920212223242526')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_add_genre_book_with_genre(self, add_collector):
        assert add_collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('name', ['123', 'Лягушка-путешественница', 'Гарри Поттер и узник Азкабана'])
    def test_get_book_genre_not_added_books_None(self, collector, name):
        assert collector.get_book_genre(name) == None

    def test_get_books_with_specific_genre_horror_add_book(self, add_collector):
        assert add_collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_genre_two_books_true(self, add_collector):
        assert len(add_collector.get_books_genre()) == 2

    def test_get_books_for_children_fantastic_add_one_book(self, add_collector):
        assert add_collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorites_one_book_from_dict_add(self, add_collector):
        assert add_collector.get_list_of_favorites_books() == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_one_book_empty_list(self, add_collector):
        add_collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert add_collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_one_book_in_list(self, add_collector):
        assert len(add_collector.get_list_of_favorites_books()) == 1


