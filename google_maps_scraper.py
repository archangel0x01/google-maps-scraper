import json
import requests
import re
import browser_cookie3
import time

def get_browser_cookies():
    browsers = {
        1: ('Chrome', browser_cookie3.chrome),
        2: ('Firefox', browser_cookie3.firefox),
        3: ('Edge', browser_cookie3.edge),
        4: ('Opera', browser_cookie3.opera),
        5: ('Brave', browser_cookie3.brave),
        6: ('Vivaldi', browser_cookie3.vivaldi)
    }
    
    print("\nAvailable browsers:")
    for idx, (browser_name, _) in browsers.items():
        print(f"{idx}. {browser_name}")
    
    while True:
        try:
            choice = int(input("\nSelect your browser (enter number): "))
            if choice in browsers:
                browser_name, browser_func = browsers[choice]
                print(f"\nUsing {browser_name} cookies...")
                return browser_func()
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def extract_data_from_url(url, headers, cookies):
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        response.raise_for_status()
        
        title_match = re.search(r'<meta content="([^"]+)" property="og:title">', response.text)
        title = title_match.group(1) if title_match else "Title not found"

        phone_match = re.search(r'\\\"tel:([+\d]+)\\\"', response.text)
        phone = phone_match.group(1) if phone_match else "Phone not found"
        
        result = {
            "name": title,
            "phone": phone
        }
        
        print("\nExtracted data:")
        print(f"Name: {title}")
        print(f"Phone: {phone}")
        print("-" * 50)
        
        return result
    except Exception as e:
        print(f"Error processing URL {url}: {e}")
        return None

def process_urls():
    try:
        # Get browser cookies
        cookies = get_browser_cookies()
        
        # Read URLs from links.json
        with open('links.json', 'r', encoding='utf-8') as file:
            urls = json.load(file)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        results = []
        for url in urls:
            print(f"Processing URL: {url}")
            data = extract_data_from_url(url, headers, cookies)
            if data:
                results.append(data)
            time.sleep(2)
        
        with open('output.json', 'w', encoding='utf-8') as file:
            json.dump(results, file, indent=4, ensure_ascii=False)
            
        print(f"Processing complete. Results written to output.json")
        
    except FileNotFoundError:
        print("links.json file not found")
    except json.JSONDecodeError:
        print("Error decoding links.json file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_urls()
