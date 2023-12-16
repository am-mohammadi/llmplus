def headers(authorization):
    h = {
        'authority': 'chatgot-ai.chatgot.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJtbWRpLmpvYkBnbWFpbC5jb20iLCJleHBpcmUiOjE3MDM5ODA4MDAwMDAsInJhbmRvbSI6IjJmYjgxMTFkYWU3YWRkYmVhOGFlZmU2MjNkZjNkZDIyIn0=.lmeREpHYMi9YWUkaPI8PNIjYWzj7CYHAR4qbO3vlI9k=',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://start.chatgot.io',
        'pragma': 'no-cache',
        'referer': 'https://start.chatgot.io/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    return h