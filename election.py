import json
from candidate import Candidate

class Election:
    def __init__(self, filename='election_data.json'):
        self.candidates = []
        self.voters = set()
        self.filename = filename
        self.load_data()

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def vote(self, voter_id, candidate_name):
        if voter_id in self.voters:
            print("You have already voted.")
            return False
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.add_vote()
                self.voters.add(voter_id)
                self.save_data()
                return True
        print("Invalid candidate name. Try again.")
        return False

    def display_results(self):
        for candidate in self.candidates:
            print(candidate)

    def save_data(self):
        data = {
            'candidates': [{ 'name': c.name, 'votes': c.votes } for c in self.candidates],
            'voters': list(self.voters)
        }
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for c in data['candidates']:
                    candidate = Candidate(c['name'])
                    candidate.votes = c['votes']
                    self.add_candidate(candidate)
                self.voters = set(data['voters'])
        except FileNotFoundError:
            pass
