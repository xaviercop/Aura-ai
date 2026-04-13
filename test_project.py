from project import format_message, get_system_prompt, get_response

def test_format_message():
    result = format_message("user", "hello")
    assert result == {"role": "user", "content": "hello"}

def test_format_message_system():
    result = format_message("system", "you are helpful")
    assert result == {"role": "system", "content": "you are helpful"}

def test_get_system_prompt():
    result = get_system_prompt()
    assert isinstance(result, str)
    assert len(result) > 0

def test_get_response():
    messages = [{"role": "user", "content": "say hello"}]
    result = get_response(messages)
    assert isinstance(result, str)
    assert len(result) > 0
