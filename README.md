![capGen Banner](https://via.placeholder.com/1200x400/fafafa/1a1a1a?text=capGen)

> AI-powered Instagram caption, hashtag & song recommendation generator.

Upload a photo, pick a vibe, and get ready-to-post captions with trending hashtags and song previews — all in one click.



## Features

- 📸 **Image Upload** — Drag & drop or click to upload (JPG, PNG, JPEG)
- 🎨 **12 Vibe Presets** — Aesthetic, Funny, Professional, Poetic, Sassy, Casual, Romantic, Trendy, Motivational, Nostalgic, Minimal, Adventurous
- ✍️ **AI Captions** — Context-aware captions generated from your image
- #️⃣ **Smart Hashtags** — Relevant hashtags with popularity indicators (Low / Medium / High / Trending)
- 🎵 **Song Recommendations** — Curated songs with 30-second previews via iTunes Search API
- 📱 **Fully Responsive** — Works beautifully on mobile, tablet, and desktop
- 🚦 **Daily Limits** — Free-tier rate limiting with Redis (IP-based)

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML, Tailwind CSS, Vanilla JavaScript |
| **Backend** | Django, LangChain |
| **AI / Vision** | Google Gemini 1.5 Flash (multimodal) |
| **Cache / Rate Limit** | Redis |
| **Music Previews** | iTunes Search API |
| **Deployment** | Railway |

## Live Demo

🚀 **[Try capGen](https://your-railway-url.up.railway.app)** *(replace with your URL)*

## Screenshots

| Upload | Results |
|--------|---------|
| ![Upload](https://via.placeholder.com/400x300/f3f4f6/6b7280?text=Upload+Zone) | ![Results](https://via.placeholder.com/400x300/f3f4f6/6b7280?text=Results+Cards) |

## Getting Started

### Prerequisites

- Python 3.10+
- Redis (local or cloud)
- Google AI Studio API key

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/capgen.git
cd capgen

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# 5. Run Redis (if local)
redis-server

# 6. Start Django server
python manage.py runserver
```

Visit `http://localhost:8000`

### Environment Variables

Create a `.env` file in the project root:

```env
# Required
GEMINI_API_KEY=your_google_ai_studio_api_key
REDIS_URL=redis://localhost:6379/0

# Optional
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### API Keys You'll Need

| Service | Purpose | Get Key |
|---------|---------|---------|
| **Google AI Studio** | Image analysis + caption generation | [aistudio.google.com](https://aistudio.google.com) |
| **iTunes Search** | Song metadata + 30s previews | *(No key required)* |
| **Redis** | Rate limiting cache | [upstash.com](https://upstash.com) or local |

## Project Structure

```
capgen/
├── backend/
│   ├── capgen/              # Django project settings
│   ├── core/                # Main app (views, utils)
│   │   ├── views.py         # API endpoints
│   │   ├── llm_service.py   # LangChain + Gemini integration
│   │   ├── itunes_service.py# iTunes Search API client
│   │   └── rate_limiter.py  # Redis-based rate limiting
│   ├── static/              # CSS, JS, images
│   ├── templates/           # HTML templates
│   └── manage.py
├── requirements.txt
├── Procfile                 # Railway deployment
├── runtime.txt              # Python version for Railway
└── README.md
```

## Usage

1. **Upload** a photo you want to post
2. **Select a Vibe** that matches your mood (e.g., *Aesthetic*, *Funny*)
3. **Choose** how many results you want (3, 5, or 10)
4. **Click Generate** and wait a few seconds
5. **Browse results** — copy captions, check hashtag popularity, preview songs
6. **Post to Instagram** 🎉

## Deployment (Railway)

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Initialize project
railway init

# 4. Add Redis plugin
railway add --plugin redis

# 5. Set environment variables
railway variables set GEMINI_API_KEY=your_key

# 6. Deploy
railway up
```

Railway automatically handles:
- Gunicorn WSGI server
- Nginx reverse proxy
- SSL/HTTPS
- Redis connection

## Rate Limiting

Free users are limited to **5 generations per IP per 24 hours**.

| Plan | Daily Generations |
|------|-------------------|
| Free | 5 |
| Pro | Unlimited |

> Rate limits are enforced server-side via Redis. Clearing browser data won't bypass them.

## Roadmap

- [ ] User accounts & saved favorites
- [ ] Pro tier with unlimited generations
- [ ] Batch upload for carousel posts
- [ ] Direct "Copy to Instagram" share intent
- [ ] Hashtag performance analytics

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Built with 💛 for Instagram creators everywhere.

> **Disclaimer:** capGen is an independent tool and is not affiliated with, endorsed by, or connected to Instagram or Meta Platforms, Inc.
