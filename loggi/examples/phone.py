class Phone:
	def format_phone(self, phone):
		valid_phone = False
		if len(phone) == 8 or len(phone) == 9:
			return phone[:4] + '-' + phone[4:]
		elif len(phone) == 10:
			return '(' + phone[:2] + ') ' + phone[2:6] + '-' + phone[6:]
		elif len(phone) == 11:
			return '(' + phone[:2] + ') ' + phone[2:7] + '-' + phone[7:]
		else:
			return ''