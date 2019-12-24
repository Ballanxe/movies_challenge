from moviesapp.apps.core.renderers import AppJSONRenderer


class UserJSONRenderer(AppJSONRenderer):

    """
    This is an especial case because here we have to handle the token c
    """

    object_label = 'user'
    pagination_object_label = 'users'
    pagination_count_label = 'usersCount'

    def render(self, data, media_type=None, renderer_context=None):

        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):

            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)
