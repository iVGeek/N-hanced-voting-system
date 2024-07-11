## N-hanced Voting System

This project is a simple election voting system implemented in Python. The system allows users to add candidates, cast votes, and display election results. It includes features such as input validation, persistent storage of votes, and voter authentication to prevent multiple votes by the same user.

## Project Structure


`N-hanced-voting-system/
├── __main__.py
├── candidate.py
├── election.py
└── run_election.py`



`candidate.py`: Contains the Candidate class which represents each candidate.
`election.py`: Contains the Election class which manages the candidates, voting process, persistent storage, and input validation.
`run_election.py`: Contains the function run_election which interacts with the user to run the election.
`__main__.py`: The entry point for running the election system.

## Features

1. Input Validation: Ensures valid inputs for the number of candidates, candidate names, and voter IDs.

2. Persistent Storage: Saves votes and candidate data to a JSON file (election_data.json).

3. Authentication: Keeps track of voter IDs to prevent multiple votes by the same user.

## Installation

1. Ensure you have Python installed (version 3.6 or higher).
2. Clone this repository or download the project files.

## Usage

1. Navigate to the project directory:
   `cd N-hanced-voting-system`
   
2. Run the election system:
   `python __main__.py`

3. Follow the prompts to:
- Enter the number of candidates.
- Enter the names of the candidates.
- Cast votes by entering voter IDs and candidate names.
- Type exit when done voting to see the results.

## Example
1. Adding Candidates
   
` Enter the number of candidates:
3
Enter candidate name:
Alice
Enter candidate name:
Bob
Enter candidate name:
Charlie`

3. Casting Votes
`Enter your voter ID (or type 'exit' to finish):
voter1
Enter your vote:
Alice
Enter your voter ID (or type 'exit' to finish):
voter2
Enter your vote:
Bob
Enter your voter ID (or type 'exit' to finish):
voter1
You have already voted.
Enter your voter ID (or type 'exit' to finish):
exit`

4. Displaying Results
`Election Results:
Alice: 1 votes
Bob: 1 votes
Charlie: 0 votes`

## License
This project is licensed under the MIT `License`. See the LICENSE file for details.

## Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
