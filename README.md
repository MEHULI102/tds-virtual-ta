# TDS Virtual TA

A Virtual Teaching Assistant (TA) for IIT Madras' Online BSc in Data Science program.  
This API helps answer student queries based on course content and past Discourse discussions.

## Features

- Accepts student questions via a POST API.
- Optionally supports base64-encoded images (e.g., screenshots).
- Uses scraped course data and Discourse posts (Jan–Apr 2025).
- Returns helpful answers along with relevant Discourse links.

## API Endpoint

```
POST /api/
Content-Type: application/json
```

### Example Request

```json
{
  "question": "Should I use gpt-4o-mini or gpt-3.5 turbo?",
  "image": "<base64-encoded-image>"
}
```

### Example Response

```json
{
  "answer": "You must use `gpt-3.5-turbo-0125`...",
  "links": [
    {
      "url": "https://discourse.onlinedegree.iitm.ac.in/t/example-post",
      "text": "Clarification from Prof. Anand"
    }
  ]
}
```

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/MEHULI102/tds-virtual-ta.git
   cd tds-virtual-ta
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the server locally:

   ```bash
   python app/main.py
   ```

## Deployment

This project is deployed at:  
**[https://your-deployment-url.vercel.app/api/](https://tds-virtual-ta.vercel.app/)**  


## License

This project is licensed under the [MIT License](LICENSE).
