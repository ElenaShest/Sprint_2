# qa_python
1. test_dict_books_genre_is_empty - проверка, что изначально словарь self.books_genre пустой

2. test_list_genre_has_five_genres - проверка, что список self.genre имеет 5 жанров

3. test_add_new_book_add_long_name_empty_dict - проверка, что в словарь self.books_genre не добавляются книги с названием длиннее 40 символов

4. test_set_book_add_genre_book_with_genre - проверка, что книге устанавливается жанр

5. test_get_book_genre_not_added_books_None (параметризованный) - проверка, что по недобавленным книгам не получим жанров

6. test_get_books_with_specific_genre_horror_add_book - проверка, что по жанру 'Ужасы' в список добавится книга

7. test_get_books_genre_two_books_true - проверка, что в словаре self.books_genre есть две книги

8. test_get_books_for_children_fantastic_add_one_book - проверка, что в список попадает одна книга с жанром 'Фантастика'

9. test_add_book_in_favorites_one_book_from_dict_add - проверка, что книга из словаря self.books_genre попала в список self.favorites

10. test_delete_book_from_favorites_one_book_empty_list - проверка, что единственная книга из списка self.favorites удаляется
11. test_get_list_of_favorites_books_one_book_in_list - проверка, что единственная книга в списке self.favorites отображается


