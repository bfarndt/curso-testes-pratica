from examples.phone import Phone
import pytest

def obj_phone():
	return Phone()

@pytest.mark.parametrize(
	'phone, formated_phone',
	[
		pytest.param('1234567', ''),
		pytest.param('12345678', '1234-5678'),
		pytest.param('123456789', '1234-56789'),
		pytest.param('1234567890', '(12) 3456-7890'),
		pytest.param('12345678901', '(12) 34567-8901'),
		pytest.param('123456789012', ''),
	]
)

def test_all_valid_cases(phone, formated_phone):
	phone_class = Phone()

	is_valid = phone_class.format_phone(phone)

	assert is_valid == formated_phone

def test01():
	phone = '1234567'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == ''

def test02():
	phone = '12345678'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == '1234-5678'

def test03():
	phone = '123456789'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == '1234-56789'

def test04():
	phone = '1234567890'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == '(12) 3456-7890'

def test05():
	phone = '12345678901'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == '(12) 34567-8901'

def test06():
	phone = '123456789012'

	formated_phone = obj_phone().format_phone(phone)

	assert formated_phone == ''