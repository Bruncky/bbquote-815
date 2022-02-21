from bbquote.lib import get_quote

def test_get_quote_in_possible_quotes():
    quote = get_quote()
    assert isinstance(quote, str)
