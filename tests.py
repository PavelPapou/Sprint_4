from main import BooksCollector
import pytest
from data import BOOK1, BOOK2, HORROR_GENRE, SPECIFIC_GENRE, FANTASTIC_GENRE


class TestBooksCollector:

    def test_add_new_book_true(self, collector): 
        collector.add_new_book(BOOK1)
        assert BOOK1 in collector.books_genre

    def test_set_book_genre_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.set_book_genre(BOOK1,HORROR_GENRE)
        assert collector.books_genre[BOOK1] == HORROR_GENRE
 
    def test_get_book_genre_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.set_book_genre(BOOK1,HORROR_GENRE)
        assert collector.get_book_genre(BOOK1) == HORROR_GENRE

    def test_get_books_with_specific_genre_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.set_book_genre(BOOK1,HORROR_GENRE)
        assert collector.get_books_with_specific_genre(HORROR_GENRE) == [BOOK1]


    def test_get_books_with_specific_genre_dont_add_specific_genre_book(self, collector): 
        collector.add_new_book(BOOK1)
        collector.set_book_genre(BOOK1,HORROR_GENRE)
        collector.add_new_book(BOOK2)
        collector.set_book_genre(BOOK2,SPECIFIC_GENRE)
        assert not collector.get_books_with_specific_genre(SPECIFIC_GENRE)

    @pytest.mark.parametrize('book_name, book_genre', [(BOOK1, HORROR_GENRE),(BOOK2, FANTASTIC_GENRE)])
    def test_get_books_genre_true(self, collector, book_name, book_genre): 
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,book_genre)
        bookcollection = { book_name:book_genre }
        assert collector.get_books_genre() == bookcollection

    def test_get_books_for_children_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.set_book_genre(BOOK1,FANTASTIC_GENRE)
        assert collector.get_books_for_children() == [BOOK1]

    def test_add_book_in_favorites_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.add_book_in_favorites(BOOK1)
        assert BOOK1 in collector.favorites

    def test_delete_book_from_favorites_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.add_book_in_favorites(BOOK1)
        collector.delete_book_from_favorites(BOOK1)
        assert BOOK1 not in collector.favorites 

    def test_get_list_of_favorites_books_true(self, collector): 
        collector.add_new_book(BOOK1)
        collector.add_book_in_favorites(BOOK1)
        assert BOOK1 in collector.favorites
