# main.py
import sqlite3


DB_NAME = "blog.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            published_date TEXT NOT NULL,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            author_name TEXT NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES posts(id)
        )
    """)

    conn.commit()


def add_author(conn, name):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO authors (name)
        VALUES (?)
    """, (name,))

    conn.commit()


def add_authors(conn, names):
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT OR IGNORE INTO authors (name)
        VALUES (?)
    """, [(name,) for name in names])

    conn.commit()


def find_author_by_name(conn, name):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM authors
        WHERE name = ?
    """, (name,))

    return cursor.fetchone()


def get_posts_by_date(conn, date):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            posts.id,
            posts.title,
            posts.content,
            posts.published_date,
            authors.name AS author_name
        FROM posts
        JOIN authors ON posts.author_id = authors.id
        WHERE posts.published_date = ?
    """, (date,))

    return cursor.fetchall()


def get_post_with_comments(conn, post_id):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            posts.id,
            posts.title,
            posts.content,
            posts.published_date,
            authors.name AS author_name
        FROM posts
        JOIN authors ON posts.author_id = authors.id
        WHERE posts.id = ?
    """, (post_id,))

    post = cursor.fetchone()

    if post is None:
        return None

    cursor.execute("""
        SELECT 
            id,
            author_name,
            text
        FROM comments
        WHERE post_id = ?
    """, (post_id,))

    comments = cursor.fetchall()

    return {
        "post": post,
        "comments": comments
    }


def seed_test_data(conn):
    cursor = conn.cursor()

    add_authors(conn, [
        "Иван Иванов",
        "Мария Петрова",
        "Алексей Смирнов"
    ])

    cursor.execute("SELECT id FROM authors WHERE name = ?", ("Иван Иванов",))
    ivan_id = cursor.fetchone()["id"]

    cursor.execute("SELECT id FROM authors WHERE name = ?", ("Мария Петрова",))
    maria_id = cursor.fetchone()["id"]

    cursor.execute("""
        INSERT INTO posts (author_id, title, content, published_date)
        VALUES (?, ?, ?, ?)
    """, (
        ivan_id,
        "Первый пост",
        "Текст первого поста",
        "2026-05-29"
    ))

    cursor.execute("""
        INSERT INTO posts (author_id, title, content, published_date)
        VALUES (?, ?, ?, ?)
    """, (
        maria_id,
        "Второй пост",
        "Текст второго поста",
        "2026-05-28"
    ))

    cursor.execute("""
        INSERT INTO comments (post_id, author_name, text)
        VALUES (?, ?, ?)
    """, (
        1,
        "Пользователь 1",
        "Хороший пост"
    ))

    cursor.execute("""
        INSERT INTO comments (post_id, author_name, text)
        VALUES (?, ?, ?)
    """, (
        1,
        "Пользователь 2",
        "Спасибо за информацию"
    ))

    conn.commit()


def print_author(author):
    if author is None:
        print("Автор не найден")
    else:
        print(f"Автор найден: id={author['id']}, name={author['name']}")


def print_posts(posts):
    if not posts:
        print("Посты не найдены")
        return

    for post in posts:
        print("-" * 40)
        print(f"ID: {post['id']}")
        print(f"Автор: {post['author_name']}")
        print(f"Дата: {post['published_date']}")
        print(f"Заголовок: {post['title']}")
        print(f"Текст: {post['content']}")


def print_post_with_comments(data):
    if data is None:
        print("Пост не найден")
        return

    post = data["post"]
    comments = data["comments"]

    print("-" * 40)
    print(f"ID поста: {post['id']}")
    print(f"Автор: {post['author_name']}")
    print(f"Дата: {post['published_date']}")
    print(f"Заголовок: {post['title']}")
    print(f"Текст: {post['content']}")

    print("\nКомментарии:")

    if not comments:
        print("Комментариев нет")
    else:
        for comment in comments:
            print(f"- {comment['author_name']}: {comment['text']}")


def main():
    conn = get_connection()

    create_tables(conn)

    # Тестовые данные
    seed_test_data(conn)

    print("\n1. Поиск автора по имени")
    author = find_author_by_name(conn, "Иван Иванов")
    print_author(author)

    print("\n2. Посты за определенную дату")
    posts = get_posts_by_date(conn, "2026-05-29")
    print_posts(posts)

    print("\n3. Добавление нескольких авторов")
    add_authors(conn, [
        "Новый Автор 1",
        "Новый Автор 2",
        "Новый Автор 3"
    ])
    print("Авторы добавлены")

    print("\n4. Пост по id вместе с комментариями")
    post_data = get_post_with_comments(conn, 1)
    print_post_with_comments(post_data)

    conn.close()


if __name__ == "__main__":
    main()
