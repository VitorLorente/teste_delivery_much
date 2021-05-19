data_mock = [
    {
        "argument": "1000",
        "expected_content_pt": b'{"extenso": "mil"}',
        "expected_content_en": b'{"full": "one thousand"}',
        "is_valid": True,
        "method": "get"
    },
    {
        "argument": "-1000",
        "expected_content_pt": b'{"extenso": "menos mil"}',
        "expected_content_en": b'{"full": "minus one thousand"}',
        "is_valid": True,
    },
    {
        "argument": "10000",
        "expected_content_pt": b'{"extenso": "dez mil"}',
        "expected_content_en": b'{"full": "ten thousand"}',
        "is_valid": True,
    },
    {
        "argument": "-10000",
        "expected_content_pt": b'{"extenso": "menos dez mil"}',
        "expected_content_en": b'{"full": "minus ten thousand"}',
        "is_valid": True,
    },
    {
        "argument": "1",
        "expected_content_pt": b'{"extenso": "um"}',
        "expected_content_en": b'{"full": "one"}',
        "is_valid": True,
    },
    {
        "argument": "-1",
        "expected_content_pt": b'{"extenso": "menos um"}',
        "expected_content_en": b'{"full": "minus one"}',
        "is_valid": True,
    },
    {
        "argument": "1234",
        "expected_content_pt": b'{"extenso": "mil duzentos e trinta e quatro"}',
        "expected_content_en": b'{"full": "one thousand, two hundred and thirty-four"}',
        "is_valid": True,
    },
    {
        "argument": "-1234",
        "expected_content_pt": b'{"extenso": "menos mil duzentos e trinta e quatro"}',
        "expected_content_en": b'{"full": "minus one thousand, two hundred and thirty-four"}',
        "is_valid": True,
    },
    {
        "argument": "12345",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "-12345",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "50000",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "-50000",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "100000",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "-100000",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "XPTO",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "-XPTO",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "+200",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
    {
        "argument": "-2a",
        "expected_content_pt": b'{"extenso": "Invalid data"}',
        "expected_content_en": b'{"full": "Invalid data"}',
        "is_valid": False,
    },
]
