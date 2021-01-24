import requests
import json
from settings import API_KEY
from time import sleep
from DATA.model import db, Post, Comment
from datetime import datetime

version = 5.126
group_id = -76982440


def get_post_data():
    offset_post = 0
    all_posts = []

    while True:
        sleep(0.4) #ограничение vk - с ключом доступа пользователя обращение не чаще 3 раз в секунду
        url_post = f'https://api.vk.com/method/wall.get?owner_id={group_id}&count=100&offset={offset_post}&access_token={API_KEY}&v={version}'
        request_post = requests.get(url_post)
        posts = request_post.json()['response']['items']
        all_posts.extend(posts)
        offset_post += 100  #смещение
        if len(all_posts) >= 200:
            break

    for post in all_posts:
        post_id = post.get('id')
        post_likes_count = post.get('likes', {}).get('count')
        post_comments_count = post.get('comments', {}).get('count')
        post_time = int(post.get('date'))
        post_published = datetime.fromtimestamp(post_time) #преобразование даты и времени из используемого vk формата timestamp в UTC
        post_text = post.get('text', 'No text')
        data = {
            'post_id': post_id,
            'post_likes_count': post_likes_count,
            'post_comments_count': post_comments_count,
            'post_published': post_published,
            'post_text': post_text
        }
        save_post_data(post_id, post_likes_count, post_comments_count, post_published, post_text)

        post_id = post['id']
        all_comments = []
        try:
            offset_comment = 0
            while True:
                sleep(0.4)
                url_comment = f'https://api.vk.com/method/wall.getComments?owner_id={group_id}&post_id={post_id}&count=100&offset={offset_comment}&need_likes=1&access_token={API_KEY}&v={version}'
                request_comment = requests.get(url_comment)
                comments = request_comment.json()['response']['items']
                all_comments.extend(comments)
                comments_count = request_comment.json()['response']['current_level_count']
                offset_comment += 100  #смещение
                if len(all_comments) == comments_count:
                    break
            
            for comment in all_comments:
                comment_id = comment.get('id')
                comment_likes_count = comment.get('likes', {}).get('count', 0)
                comment_text = comment.get('text', 'No text')                
                data = {
                    'post_id': post_id,
                    'comment_id': comment_id,
                    'comment_likes_count': comment_likes_count,
                    'comment_text': comment_text
                }
                save_comment_data(post_id, comment_id, comment_likes_count, comment_text)
        except:
            pass


def save_post_data(post_id, post_likes_count, post_comments_count, post_published, post_text):
    new_post = Post(post_id=post_id, post_likes_count=post_likes_count, post_comments_count=post_comments_count, post_published=post_published, post_text=post_text)
    try:
        db.session.add(new_post)
        db.session.commit()
    except:
        pass

def save_comment_data(post_id, comment_id, comment_likes_count, comment_text):
    new_comment = Comment(post_id=post_id, comment_id=comment_id, comment_likes_count=comment_likes_count, comment_text=comment_text)
    try:
        db.session.add(new_comment)
        db.session.commit()
    except:
        pass