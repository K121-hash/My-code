"""Examples demonstrating different ways to use the Joke Generator."""

from joke_generator import JokeGenerator
import json


def example_1_basic_usage():
    """
    Example 1: Basic Usage - Get a single joke
    """
    print("\n" + "="*50)
    print("EXAMPLE 1: Basic Usage")
    print("="*50)
    
    generator = JokeGenerator()
    generator.display_random_joke(source="official")


def example_2_multiple_jokes():
    """
    Example 2: Get multiple jokes in a loop
    """
    print("\n" + "="*50)
    print("EXAMPLE 2: Multiple Jokes")
    print("="*50)
    
    generator = JokeGenerator()
    
    for i in range(3):
        print(f"\n--- Joke {i+1} ---")
        generator.display_random_joke(source="jokeapi")


def example_3_programming_jokes():
    """
    Example 3: Get jokes from a specific category
    """
    print("\n" + "="*50)
    print("EXAMPLE 3: Programming Jokes")
    print("="*50)
    
    generator = JokeGenerator()
    
    for i in range(3):
        print(f"\n--- Programming Joke {i+1} ---")
        generator.display_random_joke(source="jokeapi", category="Programming")


def example_4_raw_data():
    """
    Example 4: Work with raw joke data
    """
    print("\n" + "="*50)
    print("EXAMPLE 4: Raw Joke Data")
    print("="*50)
    
    generator = JokeGenerator()
    
    print("\n[Official Joke API Response]:")
    joke = generator.get_random_joke_official()
    if joke:
        print(json.dumps(joke, indent=2))
    
    print("\n[JokeAPI Response]:")
    joke = generator.get_random_joke_jokeapi(category="Programming")
    if joke:
        print(json.dumps(joke, indent=2))


def example_5_error_handling():
    """
    Example 5: Handle errors gracefully
    """
    print("\n" + "="*50)
    print("EXAMPLE 5: Error Handling")
    print("="*50)
    
    generator = JokeGenerator()
    
    print("\nAttempting to fetch joke...")
    joke = generator.get_random_joke_official()
    
    if joke:
        formatted = generator.format_joke_official(joke)
        print(formatted)
    else:
        print("\n⚠️ Failed to fetch joke.")
        print("Possible reasons:")
        print("- No internet connection")
        print("- API is temporarily unavailable")
        print("- Request timeout")


def example_6_mixed_sources():
    """
    Example 6: Mix different joke sources
    """
    print("\n" + "="*50)
    print("EXAMPLE 6: Mixed Sources")
    print("="*50)
    
    generator = JokeGenerator()
    
    sources = [
        ("official", None),
        ("jokeapi", "General"),
        ("jokeapi", "Programming"),
    ]
    
    for i, (source, category) in enumerate(sources, 1):
        print(f"\n--- Joke {i} from {source.upper()} ---")
        if category:
            generator.display_random_joke(source=source, category=category)
        else:
            generator.display_random_joke(source=source)


def example_7_joke_statistics():
    """
    Example 7: Collect statistics about jokes
    """
    print("\n" + "="*50)
    print("EXAMPLE 7: Joke Statistics")
    print("="*50)
    
    generator = JokeGenerator()
    
    statistics = {
        "one_part": 0,
        "two_part": 0,
        "total_jokes": 0
    }
    
    print("\nFetching 10 jokes to analyze...")
    
    for _ in range(10):
        joke = generator.get_random_joke_jokeapi()
        if joke:
            statistics["total_jokes"] += 1
            joke_type = joke.get('type')
            if joke_type == 'twopart':
                statistics["two_part"] += 1
            else:
                statistics["one_part"] += 1
    
    print("\n📊 Statistics:")
    print(f"   Total jokes fetched: {statistics['total_jokes']}")
    print(f"   One-part jokes: {statistics['one_part']}")
    print(f"   Two-part jokes: {statistics['two_part']}")


if __name__ == "__main__":
    print("\n" + "*"*50)
    print("   JOKE GENERATOR - USAGE EXAMPLES")
    print("*"*50)
    
    # Run all examples
    example_1_basic_usage()
    example_2_multiple_jokes()
    example_3_programming_jokes()
    example_4_raw_data()
    example_5_error_handling()
    example_6_mixed_sources()
    example_7_joke_statistics()
    
    print("\n" + "*"*50)
    print("   ALL EXAMPLES COMPLETED")
    print("*"*50 + "\n")
