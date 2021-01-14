from DATA import create_app
from collect_posts import get_post_data

app = create_app()
with app.app_context():
    get_post_data()
