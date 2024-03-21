# Builds

- **Create Build**
  - **Endpoint:** `/builds/`
  - **Method:** `POST`
  - **Body:** JSON object containing build data.
  - **Response:** Returns a `build_id` with a status code of `201` if a new build is created, or `200` if an existing build is updated.
  - **Error:** Returns a JSON object with an `error` key explaining the issue (e.g., "Invalid JSON", "Empty Build").

- **Get Build Details**
  - **Endpoint:** `/builds/<str:build_id>/`
  - **Method:** `GET`
  - **URL Params:** `build_id` as string.
  - **Response:** Returns build details as a JSON object.
  - **Error:** Returns a JSON object with an `error` key and a `404` status code if no build is found.

# News

- **News Index**
  - **Endpoint:** `/news/`
  - **Method:** `GET`
  - **Query Params:** Optional `type` (str), `page` (int), and `per_page` (int) for filtering and pagination.
  - **Response:** Returns a list of news articles and pagination data, optionally filtered by type.
  - **Details:** Returns news articles with slug, title, body preview, creation and update timestamps, type, and author.

- **News Detail**
  - **Endpoint:** `/news/<slug:slug>`
  - **Method:** `GET`
  - **URL Params:** `slug` as string.
  - **Response:** Returns detailed information about a news article, including title, body, creation and update timestamps, type, and author.
  - **Error:** Returns a JSON object with an `error` key and a `404` status code if no news article is found with the provided slug.

# Stuff

- **Get All Stuff Data**
  - **Endpoint:** `/stuff/`
  - **Method:** `GET`
  - **Response:** Returns all stuff data as a JSON object.

- **Get Build Info**
  - **Endpoint:** `/stuff/build/<str:build_id>/`
  - **Method:** `GET`
  - **URL Params:** `build_id` as string.
  - **Response:** Returns equipment data including companions, skills, main runes, sub runes, mp, and maxMp.

- **Get MP Info**
  - **Endpoint:** `/stuff/mp/`
  - **Method:** `POST`
  - **Body:** JSON object containing equipment data.
  - **Response:** Returns `mp` and `maxMp` as a JSON object.
  - **Error:** Returns a JSON object with an `error` key explaining the issue (e.g., "Invalid request").
