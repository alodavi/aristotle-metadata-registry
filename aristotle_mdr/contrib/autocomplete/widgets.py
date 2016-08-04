from dal.autocomplete import ModelSelect2Multiple, ModelSelect2
from django.core.urlresolvers import reverse

class ConceptAutocompleteBase(object):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        if self.model:
            url = reverse(
                'aristotle-autocomplete:concept',
                args=[self.model._meta.app_label, self.model._meta.model_name]
            )
        else:
            url = 'aristotle-autocomplete:concept'
        
        kwargs.update(
            url=url,
            attrs={'data-html': 'true'}
        )
        super(ConceptAutocompleteBase, self).__init__(*args, **kwargs)


class ConceptAutocompleteSelectMultiple(ConceptAutocompleteBase, ModelSelect2Multiple):
    pass


class ConceptAutocompleteSelect(ConceptAutocompleteBase, ModelSelect2):
    pass
