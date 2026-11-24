# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Streamlit. This application recommends movies similar to a user's selected movie by analyzing genres, keywords, taglines, cast, and directors.

## 🚀 Features

- **Movie Selection:** Select a movie from a dropdown list.
- **Content-Based Filtering:** Recommends movies based on their content and features.
- **TF-IDF Vectorization:** Converts movie metadata into numerical feature vectors.
- **Cosine Similarity:** Measures similarity between movies.
- **Top 5 Recommendations:** Displays the five most similar movies.
- **Interactive Web Interface:** Simple and user-friendly interface powered by Streamlit.
- **Efficient Loading:** Uses Streamlit caching to avoid repeatedly processing the dataset.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Web application framework.
- **Pandas** – Data loading and manipulation.
- **Scikit-learn** – TF-IDF Vectorizer and Cosine Similarity.
- **Pathlib** – File path management.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py              # Main Streamlit application
├── movies_clean.csv    # Movie dataset
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Movie-Recommendation-System
```

### 3. Install Dependencies

```bash
pip install streamlit pandas scikit-learn
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🧠 How It Works

The recommendation system follows these steps:

1. **Dataset Loading:** Loads movie information from `movies_clean.csv`.
2. **Feature Selection:** Extracts five important features:
   - Genres
   - Keywords
   - Tagline
   - Cast
   - Director
3. **Feature Combination:** Combines the selected features into a single text representation for each movie.
4. **TF-IDF Vectorization:** Converts the combined text data into numerical vectors.
5. **Similarity Calculation:** Uses Cosine Similarity to calculate how similar movies are to each other.
6. **Recommendation:** Identifies and displays the top five most similar movies, excluding the selected movie.

## 📊 Dataset Requirements

The application requires a CSV file named `movies_clean.csv`.

The dataset must contain the following columns:

| Column | Description |
|---|---|
| `title` | Movie title |
| `genres` | Movie genres |
| `keywords` | Movie-related keywords |
| `tagline` | Movie tagline |
| `cast` | Movie cast |
| `director` | Movie director |

Make sure the dataset is placed in the same directory as `app.py`.

## 📸 Application Preview

The application provides a simple interface where users can:

1. Select their favorite movie.
2. Click the **Get Recommendations** button.
3. View five recommended movies based on content similarity.

## 🔮 Future Improvements

- Display movie posters and descriptions.
- Add movie ratings and release years.
- Integrate a movie database API.
- Improve the user interface.
- Add search functionality.
- Deploy the application online.

## 👨‍💻 Author

**Your Name**

GitHub: # 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python and Streamlit. This application recommends movies similar to a user's selected movie by analyzing genres, keywords, taglines, cast, and directors.

## 🚀 Features

- **Movie Selection:** Select a movie from a dropdown list.
- **Content-Based Filtering:** Recommends movies based on their content and features.
- **TF-IDF Vectorization:** Converts movie metadata into numerical feature vectors.
- **Cosine Similarity:** Measures similarity between movies.
- **Top 5 Recommendations:** Displays the five most similar movies.
- **Interactive Web Interface:** Simple and user-friendly interface powered by Streamlit.
- **Efficient Loading:** Uses Streamlit caching to avoid repeatedly processing the dataset.

## 🛠️ Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Web application framework.
- **Pandas** – Data loading and manipulation.
- **Scikit-learn** – TF-IDF Vectorizer and Cosine Similarity.
- **Pathlib** – File path management.

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py              # Main Streamlit application
├── movies_clean.csv    # Movie dataset
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

### 2. Navigate to the Project Directory

```bash
cd Movie-Recommendation-System
```

### 3. Install Dependencies

```bash
pip install streamlit pandas scikit-learn
```

Alternatively, install dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🧠 How It Works

The recommendation system follows these steps:

1. **Dataset Loading:** Loads movie information from `movies_clean.csv`.
2. **Feature Selection:** Extracts five important features:
   - Genres
   - Keywords
   - Tagline
   - Cast
   - Director
3. **Feature Combination:** Combines the selected features into a single text representation for each movie.
4. **TF-IDF Vectorization:** Converts the combined text data into numerical vectors.
5. **Similarity Calculation:** Uses Cosine Similarity to calculate how similar movies are to each other.
6. **Recommendation:** Identifies and displays the top five most similar movies, excluding the selected movie.

## 📊 Dataset Requirements

The application requires a CSV file named `movies_clean.csv`.

The dataset must contain the following columns:

| Column | Description |
|---|---|
| `title` | Movie title |
| `genres` | Movie genres |
| `keywords` | Movie-related keywords |
| `tagline` | Movie tagline |
| `cast` | Movie cast |
| `director` | Movie director |

Make sure the dataset is placed in the same directory as `app.py`.

## 📸 Application Preview

The application provides a simple interface where users can:

1. Select their favorite movie.
2. Click the **Get Recommendations** button.
3. View five recommended movies based on content similarity.

## 🔮 Future Improvements

- Display movie posters and descriptions.
- Add movie ratings and release years.
- Integrate a movie database API.
- Improve the user interface.
- Add search functionality.
- Deploy the application online.

## 👨‍💻 Author

Manikanta Vana

GitHub: https://github.com/Manikanta-Vana

