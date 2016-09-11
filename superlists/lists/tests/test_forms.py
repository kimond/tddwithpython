from django.test import TestCase

from ..models import List, Item
from ..forms import ItemForm, EMPTY_LIST_ERROR


class ItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.errors['text'],
            [EMPTY_LIST_ERROR]
        )

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data={'text': 'do me'})
        new_item = form.save(for_list=list_)
        self.assertEquals(new_item, Item.objects.first())
        self.assertEquals(new_item.text, 'do me')
        self.assertEquals(new_item.list, list_)