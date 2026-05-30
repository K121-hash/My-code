# 😂 Random Joke Generator

A simple Python application that fetches random jokes from external APIs. Perfect for adding some humor to your projects!

## Features

✨ **Multiple API Support:**
- Official Joke API
- JokeAPI with category filtering

🎯 **Functionality:**
- Fetch random jokes on demand
- Support for different joke categories (Programming, General, Knock-knock, etc.)
- Beautiful formatted joke output
- Error handling for API failures
- Type hints for better code clarity

📊 **Joke Types:**
- Single-liner jokes
- Two-part jokes (setup + punchline)

## Installation

### Prerequisites
- Python 3.6+
- pip (Python package manager)

### Setup

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd joke_generator
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### As a Script

```bash
python joke_generator.py
```

This will fetch and display 3 random jokes from different sources.

### As a Module

```python
from joke_generator import JokeGenerator

# Initialize the generator
generator = JokeGenerator()

# Get a random joke from Official Joke API
generator.display_random_joke(source="official")

# Get a random joke from JokeAPI
generator.display_random_joke(source="jokeapi", category="Any")

# Get a Programming joke specifically
generator.display_random_joke(source="jokeapi", category="Programming")
```

### Advanced Usage

```python
from joke_generator import JokeGenerator
import json

generator = JokeGenerator()

# Fetch raw joke data (without formatting)
joke_data = generator.get_random_joke_official()
print(json.dumps(joke_data, indent=2))

# Fetch from specific category
joke_data = generator.get_random_joke_jokeapi(category="Programming")

# Format and display
formatted = generator.format_joke_jokeapi(joke_data)
print(formatted)
```

## API Documentation

### Official Joke API
**Endpoint:** `https://official-joke-api.appspot.com/random_joke`

**Response:**
```json
{
    "type": "general",
    "setup": "What do you call a joke that is not funny?",
    "punchline": "A miss-fire",
    "id": 123
}
```

**Advantages:**
- Simple, lightweight API
- Fast response times
- No API key required

### JokeAPI
**Endpoint:** `https://v2.jokeapi.dev/joke/{category}`

**Categories:**
- `Any` - Random from all categories
- `General` - General jokes
- `Programming` - Programming/Developer jokes
- `Knock-knock` - Knock-knock jokes
- `Misc` - Miscellaneous jokes

**Response Example:**
```json
{
    "error": false,
    "category": "Programming",
    "type": "twopart",
    "setup": "Why do programmers prefer dark mode?",
    "delivery": "Because light attracts bugs!",
    "flags": {
        "nsfw": false,
        "religious": false,
        "political": false,
        "racist": false,
        "sexist": false,
        "explicit": false
    },
    "id": 123,
    "safe": true
}
```

**Advantages:**
- Multiple categories
- Content flags for filtering
- Higher quality jokes
- Type information (single/two-part)

## Code Examples

### Example 1: Get a Single Joke

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
generator.display_random_joke(source="official")
```

### Example 2: Get Multiple Jokes

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

# Get 5 jokes
for i in range(5):
    print(f"\n--- Joke {i+1} ---")
    generator.display_random_joke(source="jokeapi")
```

### Example 3: Programming Jokes

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

# Get 10 programming jokes
for _ in range(10):
    generator.display_random_joke(source="jokeapi", category="Programming")
```

### Example 4: Handle Errors

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

joke = generator.get_random_joke_official()
if joke:
    print(generator.format_joke_official(joke))
else:
    print("Failed to fetch joke. Check your internet connection.")
```

## Output Example

```
╔════════════════════════════════════════╗
║          😂 RANDOM JOKE 😂             ║
╚════════════════════════════════════════╝

Type: GENERAL

What do you call a joke that is not funny?

>>> A miss-fire

╚════════════════════════════════════════╝
```

## Error Handling

The application includes built-in error handling for:
- Network connection failures
- API timeouts (5 seconds)
- Invalid responses
- HTTP errors

When an error occurs, the function returns `None` and prints an error message.

## Troubleshooting

### "No module named 'requests'"
```bash
pip install requests
```

### "Connection refused" or "Timeout"
Check your internet connection and ensure the APIs are accessible.

### "JokeAPI returned an error"
Ensure you're using a valid category. Valid categories: `Any`, `General`, `Programming`, `Knock-knock`, `Misc`

## Performance

- **Response Time:** ~200-500ms per joke
- **Data Size:** ~1-2 KB per request
- **Rate Limiting:** No strict rate limits (reasonable usage)

## Future Enhancements

- [ ] Add joke caching to reduce API calls
- [ ] Add joke filtering by safety flags
- [ ] Create a web interface (Flask/Django)
- [ ] Add joke persistence (save favorite jokes)
- [ ] Add more API sources
- [ ] Create a Telegram/Discord bot
- [ ] Add humor rating system

## Technologies Used

- **Python 3.6+**
- **Requests Library** - HTTP requests
- **Official Joke API** - Joke source
- **JokeAPI** - Alternative joke source

## License

MIT License - Feel free to use this for personal or commercial projects!

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add new API sources

## Author

**Kyauta Ayuba Dabu**
- GitHub: [@K121-hash](https://github.com/K121-hash)
- Email: kyautadabu@gmail.com

---

**Made with ❤️ and 😂**
