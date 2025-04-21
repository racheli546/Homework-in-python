import pytest
from library import Library, Book

def test_add_book_success():
    lib = Library()
    book = Book("hello", "ab cd")
    lib.add_book(book)
    assert book in lib.books


# 2. בדיקות פעולות השאלה והחזרה
#  בדיקה שהספר הושאל בהצלחה למשתמש רשום
def test_check_out_book_success():
    lib = Library()
    user = "user"
    book = Book("hello", "ab cd")
    lib.add_user(user)
    lib.add_book(book)
    lib.check_out_book(user, book)
    assert lib.checked_out_books[user] == book
    assert book.is_checked_out == True


# 3. בדיקות חיפוש ספרים
# ✅ בדיקה שהחיפוש אינו תלוי ברישיות אותיות
def test_search_books_case_insensitive():
    lib = Library()
    book = Book("hello", "ab cd")
    lib.add_book(book)
    results = lib.search_books("Hello")
    assert book in results



# 4. בדיקות מקרים חריגים
# השאלה של ספר לא קיים
# ❌ בדיקה שהמערכת מונעת השאלת ספר שלא קיים במערכת
def test_check_out_non_existing_book():
    lib = Library()
    lib.add_user("user")
    fake_book = Book("not exist", "not created")
    x = 'a'
    while(fake_book in lib.books):
        fake_book = Book("not exist" + x, "not created" + x)
    with pytest.raises(ValueError):
        lib.check_out_book("user", fake_book)


# 5. בדיקות נכונות פעולה עם מקרים לא חוקיים
# ❌ בדיקה שהמערכת אינה מקבלת ערכים לא חוקיים, כמו כותרת ספר ריקה או שם משתמש ריק.
def test_add_book_empty_fields():
    lib = Library()
    with pytest.raises(ValueError):
        Book("","author")
    with pytest.raises(ValueError):
        Book("title","")