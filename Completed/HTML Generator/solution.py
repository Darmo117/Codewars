class HTMLGen:
    def __getattr__(self, tag_name: str):
        if tag_name == 'comment':
            return lambda s: f'<!--{s}-->'
        return lambda s: f'<{tag_name}>{s}</{tag_name}>'
