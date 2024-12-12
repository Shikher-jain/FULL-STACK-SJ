# YouTube Clone

A full-stack YouTube clone built using React and modern web development technologies. This project mimics core YouTube functionalities such as video streaming, comments, video search, live comments, and video filters, providing a user-friendly and interactive experience.

## Features

- **Video Streaming**: Watch videos seamlessly with responsive playback.
- **Search Functionality**: Search for videos with real-time search suggestions.
- **Filters**: Filter videos based on categories or other criteria.
- **Comments Section**: Add and view comments under videos.
- **Live Comments**: Experience real-time comments during live streams.
- **User Authentication**: Sign up, log in, and manage user profiles using Firebase Authentication.

## Technologies Used

- **Frontend**:
  - React
  - Redux
  - Tailwind CSS

- **Backend**:
  - Firebase (Authentication and Firestore)

- **API**:
  - YouTube API

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/youtube-clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd youtube-clone
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     REACT_APP_YOUTUBE_API_KEY=your_youtube_api_key
     REACT_APP_FIREBASE_API_KEY=your_firebase_api_key
     REACT_APP_FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
     REACT_APP_FIREBASE_PROJECT_ID=your_firebase_project_id
     REACT_APP_FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
     REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
     REACT_APP_FIREBASE_APP_ID=your_firebase_app_id
     ```

5. Start the development server:
   ```bash
   npm start
   ```

6. Open the app in your browser at `http://localhost:3000`.

## Folder Structure

```
youtube-clone/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   ├── redux/
│   ├── styles/
│   ├── utils/
│   ├── App.js
│   ├── index.js
├── .env
├── package.json
└── README.md
```

## Screenshots

_Add screenshots or GIFs here to showcase your application._

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Built with ❤️ by [Vishakha Jain](https://github.com/your-username).
