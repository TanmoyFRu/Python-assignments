import sqlite3
from User import User
from Post import Post

def create_database():
    """Creates the necessary database tables if they do not exist."""
    connection = sqlite3.connect("social_media.db")
    cursor = connection.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    )
    """)

    # Create posts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        author TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        likes INTEGER DEFAULT 0,
        FOREIGN KEY (author) REFERENCES users (username)
    )
    """)

    # Create comments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id INTEGER,
        author TEXT,
        content TEXT,
        reply_to INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (post_id) REFERENCES posts (id),
        FOREIGN KEY (author) REFERENCES users (username),
        FOREIGN KEY (reply_to) REFERENCES comments (id)
    )
    """)

    connection.commit()
    connection.close()

def main():
    create_database()
    users = {}

    while True:
        print("\n--- Social Media Menu ---")
        print("1. Create User")
        print("2. Create Post")
        print("3. Like Post")
        print("4. Comment on Post")
        print("5. Reply to Comment")
        print("6. Display Feed")
        print("7. Display Users")
        print("8. Update Post")  # New option for updating posts
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter your username: ")
            user = User(username)
            user.save_to_db()
            users[username] = user
            print(f"User '{username}' created with User ID: {user.user_id}.")

        elif choice == "2":
            username = input("Enter your username: ")
            content = input("Enter your post content: ")
            if username in users:
                users[username].create_post(content)
                print(f"Post created by {username}.")
            else:
                print("User not found.")

        elif choice == "3":
            post_id = input("Enter the post ID to like: ")
            if post_id.isdigit():
                post_id = int(post_id)
                username = input("Enter your username: ")
                if username in users:
                    users[username].like_post(post_id)
                    print(f"Post {post_id} liked.")
                else:
                    print("User not found.")
            else:
                print("Invalid post ID. Please enter a numeric value.")

        elif choice == "4":
            post_id = input("Enter the post ID to comment on: ")
            if post_id.isdigit():
                post_id = int(post_id)
                username = input("Enter your username: ")
                comment = input("Enter your comment: ")
                if username in users:
                    users[username].comment_on_post(post_id, comment)
                    print(f"Comment added to post {post_id}.")
                else:
                    print("User not found.")
            else:
                print("Invalid post ID. Please enter a numeric value.")

        elif choice == "5":
            post_id = input("Enter the post ID to reply to: ")
            comment_id = input("Enter the comment ID to reply to: ")
            if post_id.isdigit() and comment_id.isdigit():
                post_id = int(post_id)
                comment_id = int(comment_id)
                username = input("Enter your username: ")
                reply_content = input("Enter your reply: ")
                if username in users:
                    users[username].reply_to_comment(comment_id, post_id, reply_content)
                    print(f"Reply added to comment {comment_id} on post {post_id}.")
                else:
                    print("User not found.")
            else:
                print("Invalid post or comment ID. Please enter numeric values.")

        elif choice == "6":
            posts = Post.get_all_posts()
            for post in posts:
                print(f"Post ID: {post[0]}, Content: {post[1]}, Author: {post[2]}, Timestamp: {post[3]}, Likes: {post[4]}")
                comments = Post.get_comments(post[0])
                for comment in comments:
                    print(f"\tComment ID: {comment[0]}, Content: {comment[3]}, Author: {comment[2]}, Reply To: {comment[4]}")

        elif choice == "7":
            print("\n--- Registered Users ---")
            users_list = User.display_all_users()
            for user in users_list:
                print(f"User ID: {user[0]}, Username: {user[1]}")

        elif choice == "8":  # Update post
            post_id = input("Enter the post ID you want to update: ")
            if post_id.isdigit():
                post_id = int(post_id)
                username = input("Enter your username: ")
                new_content = input("Enter the new content for your post: ")

                # Check if the post exists and if the user is the author
                connection = sqlite3.connect("social_media.db")
                cursor = connection.cursor()
                cursor.execute("SELECT author FROM posts WHERE id = ?", (post_id,))
                result = cursor.fetchone()
                connection.close()

                if result and result[0] == username:
                    Post.update_post(post_id, new_content)
                    print(f"Post {post_id} updated.")
                else:
                    print("Post not found or you are not the author of this post.")
            else:
                print("Invalid post ID. Please enter a numeric value.")

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
