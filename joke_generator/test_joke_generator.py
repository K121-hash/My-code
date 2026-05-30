"""Unit tests for the Joke Generator."""

import unittest
from unittest.mock import patch, MagicMock
from joke_generator import JokeGenerator


class TestJokeGenerator(unittest.TestCase):
    """
    Test cases for JokeGenerator class.
    """
    
    def setUp(self):
        """Initialize test fixtures."""
        self.generator = JokeGenerator()
    
    def test_initialization(self):
        """Test JokeGenerator initialization."""
        self.assertIsNotNone(self.generator)
        self.assertIsNotNone(self.generator.official_joke_api)
        self.assertIsNotNone(self.generator.joke_api)
    
    @patch('requests.get')
    def test_get_random_joke_official_success(self, mock_get):
        """Test successful fetch from Official Joke API."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'type': 'general',
            'setup': 'Why did the chicken cross the road?',
            'punchline': 'To get to the other side!',
            'id': 1
        }
        mock_get.return_value = mock_response
        
        joke = self.generator.get_random_joke_official()
        
        self.assertIsNotNone(joke)
        self.assertEqual(joke['type'], 'general')
        self.assertIn('setup', joke)
        self.assertIn('punchline', joke)
    
    @patch('requests.get')
    def test_get_random_joke_official_failure(self, mock_get):
        """Test failed fetch from Official Joke API."""
        mock_get.side_effect = Exception("Connection error")
        
        joke = self.generator.get_random_joke_official()
        
        self.assertIsNone(joke)
    
    @patch('requests.get')
    def test_get_random_joke_jokeapi_success(self, mock_get):
        """Test successful fetch from JokeAPI."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'error': False,
            'category': 'Programming',
            'type': 'twopart',
            'setup': 'Why do programmers prefer dark mode?',
            'delivery': 'Because light attracts bugs!',
            'id': 1,
            'safe': True
        }
        mock_get.return_value = mock_response
        
        joke = self.generator.get_random_joke_jokeapi(category='Programming')
        
        self.assertIsNotNone(joke)
        self.assertFalse(joke['error'])
        self.assertEqual(joke['category'], 'Programming')
    
    @patch('requests.get')
    def test_get_random_joke_jokeapi_failure(self, mock_get):
        """Test failed fetch from JokeAPI."""
        mock_get.side_effect = Exception("Connection error")
        
        joke = self.generator.get_random_joke_jokeapi()
        
        self.assertIsNone(joke)
    
    def test_format_joke_official(self):
        """Test formatting of Official Joke API response."""
        joke = {
            'type': 'general',
            'setup': 'Why did the chicken cross the road?',
            'punchline': 'To get to the other side!',
            'id': 1
        }
        
        formatted = self.generator.format_joke_official(joke)
        
        self.assertIn('RANDOM JOKE', formatted)
        self.assertIn('Why did the chicken cross the road?', formatted)
        self.assertIn('To get to the other side!', formatted)
    
    def test_format_joke_jokeapi(self):
        """Test formatting of JokeAPI response."""
        joke = {
            'error': False,
            'category': 'Programming',
            'type': 'twopart',
            'setup': 'Why do programmers prefer dark mode?',
            'delivery': 'Because light attracts bugs!',
            'id': 1,
            'safe': True
        }
        
        formatted = self.generator.format_joke_jokeapi(joke)
        
        self.assertIn('RANDOM JOKE', formatted)
        self.assertIn('Programming', formatted)
        self.assertIn('Why do programmers prefer dark mode?', formatted)
    
    def test_format_joke_official_none(self):
        """Test formatting when joke is None."""
        formatted = self.generator.format_joke_official(None)
        self.assertEqual(formatted, "No joke available")
    
    def test_format_joke_jokeapi_none(self):
        """Test formatting when joke is None."""
        formatted = self.generator.format_joke_jokeapi(None)
        self.assertEqual(formatted, "No joke available")


if __name__ == '__main__':
    unittest.main()
