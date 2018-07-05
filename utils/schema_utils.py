from graphql.language.ast import FragmentSpread, Field

def find_operation_field(fields, name):
    for field in fields:
        if field.name.value == name:
            return field
    return None

def get_selections(field, fragments):
    fields = []
    for x in field.selection_set.selections:
        if isinstance(x, Field):
            if x.name.value != '__typename':
                fields.append(x.name.value)
        elif isinstance(x, FragmentSpread):
            fields += get_selections(fragments[x.name.value], fragments)
    return fields