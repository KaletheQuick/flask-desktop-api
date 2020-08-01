from application.app import chop

def test_chop_emptyString():
    assert chop("") == ""

def test_chop_smallString():
    assert chop("ex") == "" 

def test_chop_bigString():
    assert chop("example") == "al" 