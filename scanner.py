"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?

NOTE: suitable for optional matches
"""

def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """

	if pos<0 or pos>=len(text): return None

	c = text[pos]

	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	if pos = 0:
			if c>='0' and c<='2': return '0-2'	# 0..9 grouped together

	if pos = 1 and c = '3':
		if c>='0' and c<='4': return '0-4'

	if (pos = 1 and c = '0-2') or (pos = 2 and (c = '0-4' or c '0-9')) or pos >= 3:
		if c>='0' and c<='9': return '0-9'

	return c	# anything else



def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""

	# initial state
	pos = 0
	state = 'q0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None


	while True:

		c = getchar(text,pos)	# get next char (category)

		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char

			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos

		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos

			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos


# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 'q0': { '0-2':'q1', '3':'q2' },
       			'q1': { '0-9':'q3' },
       			'q2': { '0-4':'q4', '5':'q5' },
       			'q3': { '0-9':'q6' },
				'q4': { '0-9':'q6' },
				'q5': { '0':'q6' },
				'q6': { '0-9':'q7' },
				'q7': { '0-9':'q8' },
				'q8': { 'K':'q9', 'G':'q10' },
				'q9': { 'T':'q13' },
				'q10': { '0-9':'q11' },
				'q11': { '0-9':'q12' },
				'q12': { 'K':'q9' },
     		  }

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 'q13':'WIND_TOKEN' }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
