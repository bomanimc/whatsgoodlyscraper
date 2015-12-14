import apiFunctions as api
from datetime import datetime
from dateutil import parser

def main():
	# Print User Info Text
	print("Logging into Whatsgoodly...\n")
	online = True
	try:
		print('Successful!')
	except:
		print("Error: Not connected to the Internet\n")
		online = False
	if online:
		print("Use the commands below.")
		
		currentPolls = []
		
		# While loop for terminal UI.
		while True:
			
			# Attempt to get a user choice for Python 2 or 3.
			try:
				choice = raw_input("\t*Read Polls\t\t(R)\n\n\t*Quit App\t\t(Q)\n\n->")
			except SyntaxError:
				choice = input("\t*Read Polls\t\t(R)\n\n\t*Quit App\t\t(Q)\n\n->")
			
			# Read Polls
			if choice.upper() == 'R':
				currentPolls = api.getPolls()
				pollPrint(currentPolls)
			# Quit App
			elif choice.upper() == 'Q':
				break;

# A function for prettily printing the polls
def pollPrint(allPolls):
	for poll in allPolls:
		print('-'*80)
		date = parser.parse(poll.created_date)
		print('Poll #{} Posted: {}\nQuestion: {}\nOptions:'.format(poll.id, date, poll.question))
		for i in range(0, len(poll.options)):
			print('\t{} | Votes: {}'.format(poll.options[i], poll.option_counts[i]))

		print('-'*80)
main()