def create_class(class_name, secrets=None):
    if not class_name:
        return None
    return type(class_name, (), secrets or {})
