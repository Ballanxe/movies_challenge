from moviesapp.apps.core.renderers import AppJSONRenderer


class MovieJSONRenderer(AppJSONRenderer):

	object_label = 'movie'
	object_label_plural = 'movies'

	def render(self, data, media_type=None, renderer_context=None):

		data['casting'] = data.get('casting', [])
		data['directors'] = data.get('directors', [])
		data['producers'] = data.get('producers', [])

		return super(MovieJSONRenderer, self).render(data)
