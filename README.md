# OnRec Podcast API

This project is a Django-based RESTful API for managing podcasts, guests, and related blogs. The API provides endpoints to retrieve and explore podcasts, view associated guests, and fetch blog details linked to specific podcasts.

## Features

- **Podcast Management**: Create, view, update, and delete podcast entries.
- **Guest Management**: Manage guest information associated with podcasts.
- **Blog Management**: Associate blogs with specific podcasts and manage their content.
- **API**: RESTful API for accessing podcasts, guests, and blogs data.

## Models

- **Guest**: Contains information about the guest, such as name, description, designation, and image.
- **Podcast**: Contains information about the podcast series, title, guest, description, and links to Spotify and YouTube.
- **Blog**: Contains information about blog posts associated with podcasts, including content and a Medium link.

## Installation

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- pip

## Endpoints

### Podcasts

- **Get All Podcasts**  
  `GET /podcasts/all`  
  Retrieves a list of all podcasts along with their details.

- **Explore Podcasts by Series**  
  `GET /explore/<str:series>/`  
  Retrieves podcasts filtered by the specified series.

- **Get Podcast by ID**  
  `GET /podcast/<int:podcast_id>/`  
  Retrieves a specific podcast by its ID, along with associated guest and blog data.


### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/skywalker139/onRec_backend.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
 
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    - Go to `http://127.0.0.1:8000/` to access the application.
    - Go to `http://127.0.0.1:8000/admin/` to access the Django admin panel.
## Data Model

### Guest
- `id`: Auto-generated ID
- `name`: Name of the guest
- `description`: Detailed description of the guest
- `designation`: Guest's designation or title
- `image`: URL or file path to the guest's image
- `created_at`: Timestamp of guest creation

### Podcast
- `id`: Auto-generated ID
- `series`: Series category of the podcast (e.g., career, wellness)
- `title`: Title of the podcast
- `release_date`: Date of release
- `guest`: Foreign key linking to the Guest model
- `description`: Detailed description of the podcast
- `spotify_link`: URL to the podcast on Spotify
- `youtube_link`: URL to the podcast on YouTube
- `thumbnail`: URL or file path to the podcast's thumbnail image

### Blog
- `id`: Auto-generated ID
- `title`: Title of the blog
- `content`: Main content of the blog
- `release_date`: Date of blog release
- `podcast`: Foreign key linking to the Podcast model
- `medium_link`: URL to the blog post on Medium

## Dummy Data

To load dummy data into the database:

1. **Guests**: Use `guests.csv` to load guest data via Django Admin.
2. **Podcasts**: Use `podcasts.csv` to load podcast data via Django Admin.
3. **Blogs**: Use `blogs.csv` to load blog data via Django Admin.


## API Usage

You can use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to interact with the API endpoints.

Example request to get all podcasts:
```bash
GET /podcasts/all
```


## Contact

For any questions or suggestions, feel free to contact me at [akshatnamdeo2412@gmail.com].

