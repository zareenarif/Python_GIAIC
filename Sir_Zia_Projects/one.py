import streamlit as st
import json
import os

# variable banana hy jis me file store karay gay
LIBRARY_FILE = "library.txt"

# Load existing books
def Load():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:  # r= read mode
            return json.load(file)
    return []

# Save books
def save_books(books):
    with open(LIBRARY_FILE, "w") as file: #w= write mode
        json.dump(books, file, indent=4)

# Streamlit UI
st.title("📚 AI-Powered Personal Library Manager")
books = Load()

# Add a new book
st.header("➕ Add a Book")
with st.form("add_book_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1800, max_value=2025, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Have you read this book?", ["Yes", "No"])
    submitted = st.form_submit_button("Add Book")
    if submitted:
        book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status == "Yes"}
        books.append(book)
        save_books(books)
        st.success("Book added successfully!")

# Search for a book
st.header("🔍 Search for a Book")
search_query = st.text_input("Enter book title or author to search:")
if st.button("Search"):
    results = [book for book in books if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
    if results:
        for book in results:
            st.write(f"📖 *{book['title']}* by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        st.warning("No matching books found.")

# Display all books
st.header("📖 Library Collection")
if books:
    for book in books:
        st.write(f"📕 *{book['title']}* by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
else:
    st.info("Your Library is empty. Add books to see them here.")

# Remove a book
st.header("🗑 Remove a Book")
remove_title = st.text_input("Enter book title to remove:")
if st.button("Remove Book"):
    books = [book for book in books if book["title"].lower() != remove_title.lower()]
    save_books(books)
    st.success(f"✅ '{remove_title}' removed from library!")

# Display statistics
st.header("📊 Library Statistics")
total_books = len(books)
read_books = sum(1 for book in books if book["read"])
percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

st.write(f"📚 *Total Books:* {total_books}")
st.write(f"📖 *Books Read:* {read_books}")
st.write(f"📈 *Percentage Read:* {percentage_read:.2f}%")