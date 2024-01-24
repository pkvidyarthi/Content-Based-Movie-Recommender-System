# Content-Based-Movie-Recommender-System
## Steps :
1. Import Libraries: Import the necessary libraries for the code.

2. Define posterFetching Function: Define the function to fetch movie posters using the TMDb API.

3. Define Recommend Function: Define the function to recommend similar movies based on a selected movie title.

4. Load Movie Data: Load the movie data from the JSON file using Pandas.

5. Load Similarity Matrix: Load the similarity matrix from a JSON file located at a specific URL.

6. Create Streamlit UI: Set up the Streamlit UI for the movie recommender system.

7. Select Favorite Movie: Create a selectbox for users to choose their favorite movie from the available options.

8. Recommend Button: Create a button to trigger the recommendation process.

9. Recommendation Display: Display the recommended movies and their poster images on the webpage.

10. End of Code.

## Explanation :

* sklearn - A machine learning library used for various tasks.

* sklearn.feature_extraction.text - A module for text feature extraction.

* CountVectorizer - Converts text data into numerical vectors.

* stop_words - Removes common English stopwords during vectorization.

* fit_transform - Fits the vectorizer on input data and transforms text into a matrix.

* toarray - Converts a sparse matrix to a dense array.

* shape - Returns the dimensions of an array.

* get_feature_names_out - Returns the feature names from the vectorizer.

* nltk - A library for natural language processing.

* PorterStemmer - A class for word stemming.

* stemming - A function that applies stemming to text.

* apply - Applies a function to each element or column of a DataFrame.

* cosine_similarity - Calculates cosine similarity between vectors.

* df - A Pandas DataFrame for tabular data.

* iloc - Integer-based indexing for retrieving rows from a DataFrame.

* enumerate - Iterates over a sequence while keeping track of the index.

* sorted - Sorts a sequence in ascending or descending orderpickle is used to serialize and save Python objects to files.

* pickle - Used to serialize and save Python objects to files.

### Fetching Data with Website
1. Login to TMDB
2. Go to Settings
3. API
4. Copy API KEY
5. Paste API KEY as place of 'url' in the PosterFetching Function.


### Movie Recommendations System
Website (Project Link) : https://pkvidyarthi-content-based-movie-recommender-system-app-brv1f5.streamlit.app/
