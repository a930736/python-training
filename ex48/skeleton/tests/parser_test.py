from nose.tools import*
from ex48.parser import*
import ex48.lexicon
def test_peak():
    assert_equal(peek([("direction","east")]),"direction")
    assert_equal(peek([]),None)
    result = peek([("noun", "east"),("verb","go")])
    assert_equal(result,"noun")

def test_match():
    assert_equal(match([("verb","kill")],"verb"),("verb","kill"))
    assert_equal(match([("noun","bear")], "verb"),None)
    assert_equal(match([],"noun"),None)

def test_skip():
    assert_equal(skip([("stop","the")],"stop"),None)
    result = skip([("stop","in"),("noun","bear")],"stop")
    assert_equal(result,None)

def test_parse_verb():
    assert_raises(ParserError,parse_verb,[("stop", "the"),("stop", "in")])
    assert_equal(parse_verb([("stop","the"),("verb","go")]),("verb", "go"))
    assert_equal(parse_verb([("verb", "eat"),("verb","kill")]),("verb","eat"))
    assert_raises(ParserError,parse_verb,[("noun","door"),("verb", "go")])
    assert_raises(ParserError,parse_verb,[("direction", "east"),("verb", "kill")])
def test_parse_object():
    assert_raises(ParserError, parse_object, [("stop","the"),("stop","in")])
    assert_raises(ParserError, parse_object, [("stop", "the"), ("verb", "go")])

    assert_equal(parse_object([("noun", "door"), ("verb", "go")]), ("noun", "door"))

    result = parse_object([("direction", "north"), ("verb", "eat")])
    assert_equal(result,("direction", "north"))



def test_parse_subject():
    result = parse_subject([("verb", "go"), ("stop", "the"), ("noun", "door")])
    assert_equal(result,("noun", "player"))


def test_parse_sentence():

    result = parse_sentence([("verb", "go"),("stop","the"), ("noun", "door")])
    assert_equal(result.subject,"player")
    assert_equal(result.verb,"go")
    assert_equal(result.object, "door")

    result = parse_sentence([("stop", "in"), ("noun", "door"), ("verb", "go"), ("direction", "north")])
    assert_equal(result.subject, "door")
    assert_equal(result.verb, "go")
    assert_equal(result.object, "north")

    assert_raises(ParserError, parse_sentence, [("stop", "in"), ("stop", "the")])
