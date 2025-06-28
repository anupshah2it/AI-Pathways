from translators.js import JsTranslator


def test_js_translator(tmp_path):
    # Use provided sample script
    translator = JsTranslator("translators/sample.js")
    result = translator.translate({"foo": "bar"})
    assert result == {"wrapped": {"foo": "bar"}}
