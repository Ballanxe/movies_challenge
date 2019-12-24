from moviesapp.apps.core.renderers import AppJSONRenderer


class PersonJSONRenderer(AppJSONRenderer):

	object_label = 'person'
	object_label_plural = 'persons'

