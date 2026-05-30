import requests
import json
from typing import Dict, Optional


class JokeGenerator:
    """
    A simple joke generator that fetches random jokes from external APIs.
    
    Supported APIs:
    - Official Joke API (https://official-joke-api.appspot.com/)
    - JokeAPI (https://v2.jokeapi.dev/)
    """
    
    def __init__(self):
        self.official_joke_api = "https://official-joke-api.appspot.com"
        self.joke_api = "https://v2.jokeapi.dev/joke"
    
    def get_random_joke_official(self) -> Optional[Dict]:
        """
        Fetch a random joke from the Official Joke API.
        
        Returns:
            Dict: Joke data containing 'setup' and 'punchline'
            None: If the API request fails
        
        Example:
            {
                'type': 'general',
                'setup': 'What do you call a joke that is not funny?',
                'punchline': 'A miss-fire',
                'id': 123
            }
        """
        try:
            endpoint = f"{self.official_joke_api}/random_joke"
            response = requests.get(endpoint, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke from Official Joke API: {e}")
            return None
    
    def get_random_joke_jokeapi(self, category: str = "Any") -> Optional[Dict]:
        """
        Fetch a random joke from JokeAPI.
        
        Args:
            category (str): Category of joke - 'Any', 'General', 'Programming', 
                          'Knock-knock', 'Programming', 'Misc'
                          Default: 'Any'
        
        Returns:
            Dict: Joke data
            None: If the API request fails
        
        Example:
            {
                'error': False,
                'category': 'Programming',
                'type': 'twopart',
                'setup': 'Why do programmers prefer dark mode?',
                'delivery': 'Because light attracts bugs!',
                'flags': {...},
                'id': 123,
                'safe': True
            }
        """
        try:
            endpoint = f"{self.joke_api}/{category}"
            response = requests.get(endpoint, timeout=5)
            response.raise_for_status()
            joke_data = response.json()
            
            if joke_data.get('error'):
                print("JokeAPI returned an error")
                return None
            
            return joke_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke from JokeAPI: {e}")
            return None
    
    def format_joke_official(self, joke: Dict) -> str:
        """
        Format joke from Official Joke API for display.
        
        Args:
            joke (Dict): Joke data
        
        Returns:
            str: Formatted joke string
        """
        if not joke:
            return "No joke available"
        
        setup = joke.get('setup', '')
        punchline = joke.get('punchline', '')
        joke_type = joke.get('type', 'general')
        
        return f"""
╔════════════════════════════════════════╗
║          😂 RANDOM JOKE 😂             ║
╚════════════════════════════════════════╝

Type: {joke_type.upper()}

{setup}

>>> {punchline}

╚════════════════════════════════════════╝
        """
    
    def format_joke_jokeapi(self, joke: Dict) -> str:
        """
        Format joke from JokeAPI for display.
        
        Args:
            joke (Dict): Joke data
        
        Returns:
            str: Formatted joke string
        """
        if not joke:
            return "No joke available"
        
        category = joke.get('category', 'General')
        joke_type = joke.get('type', 'single')
        
        if joke_type == 'twopart':
            setup = joke.get('setup', '')
            delivery = joke.get('delivery', '')
            content = f"{setup}\n\n>>> {delivery}"
        else:
            content = joke.get('joke', '')
        
        return f"""
╔════════════════════════════════════════╗
║          😂 RANDOM JOKE 😂             ║
╚════════════════════════════════════════╝

Category: {category}
Type: {joke_type.upper()}

{content}

╚════════════════════════════════════════╝
        """
    
    def display_random_joke(self, source: str = "official", category: str = "Any"):
        """
        Fetch and display a random joke.
        
        Args:
            source (str): 'official' or 'jokeapi'. Default: 'official'
            category (str): Category for JokeAPI. Default: 'Any'
        """
        if source.lower() == "official":
            joke = self.get_random_joke_official()
            formatted = self.format_joke_official(joke)
        elif source.lower() == "jokeapi":
            joke = self.get_random_joke_jokeapi(category)
            formatted = self.format_joke_jokeapi(joke)
        else:
            print("Invalid source. Use 'official' or 'jokeapi'")
            return
        
        print(formatted)
        return joke


def main():
    """
    Main function to demonstrate the joke generator.
    """
    generator = JokeGenerator()
    
    print("\n" + "="*40)
    print("     RANDOM JOKE GENERATOR v1.0")
    print("="*40)
    
    # Fetch from Official Joke API
    print("\n[1] Fetching from Official Joke API...")
    generator.display_random_joke(source="official")
    
    # Fetch from JokeAPI (Random category)
    print("\n[2] Fetching from JokeAPI (Random)...")
    generator.display_random_joke(source="jokeapi", category="Any")
    
    # Fetch specific category from JokeAPI
    print("\n[3] Fetching Programming Joke from JokeAPI...")
    generator.display_random_joke(source="jokeapi", category="Programming")


if __name__ == "__main__":
    main()
