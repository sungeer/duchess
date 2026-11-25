from src.domains.health import views as health_views
from src.domains.users import views as user_views


def register_routes(app):
    # 健康检查
    app.add_url_rule('/healthz.liveness', view_func=health_views.liveness, methods=['POST'])

    # 用户
    app.add_url_rule('/users.get', view_func=user_views.get_user, methods=['POST'])
    app.add_url_rule('/users.get_by_username', view_func=user_views.get_user_by_username, methods=['POST'])
    app.add_url_rule('/users.get_by_email', view_func=user_views.get_user_by_email, methods=['POST'])
    app.add_url_rule('/users.list', view_func=user_views.list_users, methods=['POST'])
    app.add_url_rule('/users.count', view_func=user_views.count_users, methods=['POST'])
    app.add_url_rule('/users.create', view_func=user_views.create_user, methods=['POST'])
    app.add_url_rule('/users.update', view_func=user_views.update_user, methods=['POST'])
    app.add_url_rule('/users.delete', view_func=user_views.delete_user, methods=['POST'])
