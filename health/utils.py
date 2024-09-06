

def get_readable_form_of_choice(CHOICE, short_form:str):
    """
        RANDOM_CHOICE = (
            ('a', 'A'),
            ('b', 'B'),
        )

        get_readable_form_of_choice(RANDOM_CHOICE, 'a')
    """
    return [
        readable_form[1] for readable_form in CHOICE if readable_form[0] == short_form
    ][0]