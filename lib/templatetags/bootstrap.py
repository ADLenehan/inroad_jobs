from django import template
from django.template import Context
from django.template.loader import get_template

register = template.Library()


def _preprocess_fields(form):
    for field in form.fields:
        name = form.fields[field].widget.__class__.__name__.lower()
        if not name.startswith("radio") and not name.startswith("checkbox"):
            if 'class' not in form.fields[field].widget.attrs or 'form-control' not in form.fields[field].widget.attrs["class"]:
                try:
                    form.fields[field].widget.attrs["class"] += " form-control"
                except KeyError:
                    form.fields[field].widget.attrs["class"] = "form-control"
    return form


@register.filter
def bootstrap_form(form):
    template = get_template("bootstrap/form.html")
    form = _preprocess_fields(form)

    c = Context({
        "form": form,
        "labels": True
    })
    return template.render(c)


@register.filter
def bootstrap_form_inline(form):
    template = get_template("bootstrap/form.html")
    form = _preprocess_fields(form)

    for field in form.fields:
        name = form.fields[field].widget.__class__.__name__.lower()
        if not name.startswith("radio") and not name.startswith("checkbox"):
            form.fields[field].widget.attrs["placeholder"] = form.fields[field].label

    css_classes = {
        "label": "sr-only",
        "single_container": "",
        "wrap": "",
    }

    c = Context({
        "form": form,
        "css_classes": css_classes,
    })
    return template.render(c)


@register.filter
def bootstrap_form_horizontal(form, label_classes=""):
    template = get_template("bootstrap/form.html")
    form = _preprocess_fields(form)

    if label_classes == "":
        label_classes = "col-md-2"

    css_classes = {
        "label": label_classes,
        "single_container": "",
        "wrap": "",
    }

    for label_class in label_classes.split(" "):
        split_class, column_count = label_class.rsplit("-", 1)
        column_count = int(column_count)

        if column_count < 12:
            offset_class = "{split_class}-offset-{column_count}".format(
                split_class=split_class,
                column_count=column_count,
            )
            wrap_class = "{split_class}-{column_count}".format(
                split_class=split_class,
                column_count=12 - column_count,
            )
            css_classes["single_container"] += offset_class + " " + wrap_class + " "
            css_classes["wrap"] += wrap_class + " "

    c = Context({
        "form": form,
        "css_classes": css_classes,
    })
    return template.render(c)

@register.simple_tag
def bootstrap_field(form, field, **kwargs):
    template = get_template("bootstrap/field.html")

    if 'class' not in form.fields[field.name].widget.attrs:
        form.fields[field.name].widget.attrs["class"] = "form-control"
    elif 'form-control' not in form.fields[field.name].widget.attrs["class"]:
        form.fields[field.name].widget.attrs["class"] += " form-control"


    if 'labels' not in kwargs:
        kwargs['labels'] = True

    c = Context({
        "form": form,
        "field": field,
        "labels": kwargs['labels']
    })
    return template.render(c)

@register.filter
def bootstrap_widget_class(field):
    return field.field.widget.__class__.__name__.lower()

@register.filter
def bootstrap_field_class(field):
    return field.field.__class__.__name__.lower()