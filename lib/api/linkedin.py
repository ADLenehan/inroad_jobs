import requests
import json
def make_request(method, url, token ,data=None, params=None, headers=None, timeout=60):
    headers = {'x-li-format': 'json', 'Content-Type': 'application/json'}
    params = {} 
    kw = dict(data=data, params=params, headers=headers, timeout=timeout)
    params.update({'oauth2_access_token': token})
    return requests.request(method.upper(), url, **kw)   

def linkedin_post(comment, title, description, submitted_url, submitted_image_url, token):
    post = {
        'comment': comment,
        'content': {
        'title': title,
        'submitted-url': submitted_url,
        'submitted-image-url': submitted_image_url,
        'description': description
    },
    'visibility': {
        'code': 'anyone'
    }
    }
    url = 'https://api.linkedin.com/v1/people/~/shares'
    try:
        response = make_request('POST', url, token,data=json.dumps(post))
        response = response.json()
        return response
    except Exception:
        return False