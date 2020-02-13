from examples.identifier import Identifier
import pytest

#@pytest.fixture(scope='module', params=['abcdef'])
#def obj_identifier(request):
#	return (Identifier(), request.param)
#
#def test_all_valid_cases(obj_identifier):
#	identifier = obj_identifier[0]
#
#	is_valid = identifier.validate_identifier(obj_identifier[1])
#
#	assert is_valid is True

def obj_identifier():
	return Identifier()

@pytest.mark.parametrize(
	'identif',
	[
		pytest.param('a', id='CT2'),
		pytest.param('ab', id='2_chars_validos'),
		pytest.param('abcde'),
		pytest.param('abcdef'),
		pytest.param('a1'),
	]
)

def test_all_valid_cases2(identif):
	identifier = Identifier()

	is_valid = identifier.validate_identifier(identif)

	assert is_valid is True

#def test_exception_raised():
#	identifier = Identifier()
#
#	with pytest.raises(ValueError) as error:
#		identifier.validate_identifier('')
#		pytest.set_trace()
#		assert error == 'Identificador inválido'