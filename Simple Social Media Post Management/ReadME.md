
# Social Media Platform Simulation

This project simulates a simple social media platform using Python. Users can create posts, like them, comment on them, and reply to comments. The platform uses an SQLite database to store users, posts, comments, likes, and replies.

## Features
- **User management**: Users can create accounts, and every post and comment is associated with a user.
- **Post creation**: Users can create posts, which are saved to a database.
- **Like posts**: Users can like posts, and the like count is updated in real-time.
- **Comment on posts**: Users can add comments to posts, and replies can be added to comments (threaded commenting).
- **Edit and delete posts**: Users can modify or delete their own posts.
- **Display posts**: Posts are displayed in reverse chronological order with comments and replies.

## Project Structure

\`\`\`bash
social_media_app/
│
├── post.py      # Contains the Post class with database integration
├── user.py      # Contains the User class with database integration
├── main.py      # Main program that handles user interactions and operations
├── db.py        # Handles the SQLite database connection and table creation
└── utils.py     # Optional utility functions (if needed)
\`\`\`

## Setup

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/social_media_app.git
cd social_media_app
\`\`\`

### 2. Install Requirements
No external packages are needed. The project uses Python’s built-in \`sqlite3\` library.

### 3. Initialize the Database
Before running the application, you need to set up the SQLite database.

\`\`\`bash
python db.py
\`\`\`

This will create a \`social_media.db\` file with the necessary tables (\`users\`, \`posts\`, \`comments\`).

### 4. Run the Application
To start interacting with the social media simulation:

\`\`\`bash
python main.py
\`\`\`

You’ll be presented with a menu to create users, posts, like posts, comment, reply, and display the feed.

## Usage

After running \`main.py\`, the menu offers the following options:

\`\`\`
--- Social Media Menu ---
1. Create User
2. Create Post
3. Like Post
4. Comment on Post
5. Reply to Comment
6. Display Feed
7. Exit
\`\`\`

### Example Workflow

1. **Create a User**: Enter a username, and it will be saved to the database.
2. **Create a Post**: Input post content, which will be linked to the user and saved.
3. **Like a Post**: Increase the like count of any post.
4. **Comment on a Post**: Add a comment to a post.
5. **Reply to a Comment**: Reply to specific comments in a threaded format.
6. **Display Feed**: View all posts with likes, comments, and replies in reverse chronological order.

### Example Interactions:

- **Create User**:
    \`\`\`
    Enter your username: Alice
    User 'Alice' created.
    \`\`\`

- **Create Post**:
    \`\`\`
    Enter your username: Alice
    Enter your post content: Hello, this is my first post!
    Post created by Alice.
    \`\`\`

- **Like Post**:
    \`\`\`
    Enter the post ID to like: 1
    Post 1 liked.
    \`\`\`

- **Comment on Post**:
    \`\`\`
    Enter the post ID to comment on: 1
    Enter your username: Bob
    Enter your comment: Nice post!
    Comment added to post 1.
    \`\`\`

## Database Structure

- **users**:
  - \`id\` (INTEGER, PRIMARY KEY)
  - \`username\` (TEXT, UNIQUE)
  
- **posts**:
  - \`id\` (INTEGER, PRIMARY KEY)
  - \`content\` (TEXT)
  - \`author\` (TEXT, FOREIGN KEY to users)
  - \`timestamp\` (DATETIME, default current timestamp)
  - \`likes\` (INTEGER, default 0)
  
- **comments**:
  - \`id\` (INTEGER, PRIMARY KEY)
  - \`post_id\` (INTEGER, FOREIGN KEY to posts)
  - \`author\` (TEXT, FOREIGN KEY to users)
  - \`content\` (TEXT)
  - \`reply_to\` (INTEGER, NULL, FOREIGN KEY to comments for threaded replies)
  - \`timestamp\` (DATETIME, default current timestamp)

## Future Enhancements

- **Authentication**: Add user login and authentication functionality.
- **Post Editing/Deletion**: Allow users to edit and delete their own posts.
- **Enhanced Comment Threads**: Improve display of nested comment threads.
- **Additional Reactions**: Add more interaction options such as emojis or reactions.
- **Search and Filters**: Implement searching for posts and users, and adding filters for posts by likes or dates.

## Contributing

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Make your changes and commit (\`git commit -m 'Add some feature'\`).
4. Push the branch (\`git push origin feature-branch\`).
5. Open a pull request.



## Contact

If you have any questions, feel free to open an issue or contact me directly at [tanmoydn2003@email.com].
