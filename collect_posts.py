import requests
import json
from settings import API_KEY
from time import sleep

version = 5.126
group_id = -76982440


def get_post_data(post):
    post_id = post.get('id')
    likes_cnt = post.get('likes', {}).get('count')
    comments_cnt = post.get('comments', {}).get('count')
    text = post.get('text', 'No text')[:50] # для примера - первые 50 символов
    data = {
        'post_id': post_id,
        'post_likes_cnt': likes_cnt,
        'comments_cnt': comments_cnt,
        'post_text': text
    }
    return data


def get_comment_data(comment):
    comment_id = comment.get('id')
    text = comment.get('text', 'No text')[:50] # для примера - первые 50 символов
    likes_cnt = comment.get('likes', {}).get('count')
    data = {
        'comment_id': comment_id,
        'comment_likes_cnt': likes_cnt,
        'comment_text': text
    }
    return data


def main():
    offset_post = 0
    all_posts = []

    while True:
        sleep(0.4) # ограничение vk - с ключом доступа пользователя обращение не чаще 3 раз в секунду
        url_post = f'https://api.vk.com/method/wall.get?owner_id={group_id}&count=100&offset={offset_post}&access_token={API_KEY}&v={version}'
        request_post = requests.get(url_post)
        posts = request_post.json()['response']['items']
        all_posts.extend(posts)
        offset_post += 100  #смещение
        if len(all_posts) >= 100:
            break

    for post in all_posts:
        post_data = get_post_data(post)
        print(post_data)

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
                comments_data = get_comment_data(comment)
                print(comments_data)
        except:
            print('No comments')
        print('------------')

    print(len(all_posts))

if __name__ == '__main__':
    main()
