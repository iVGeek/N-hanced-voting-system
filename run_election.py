from election import Election
from candidate import Candidate

def run_election():
    election = Election()

    print("Enter the number of candidates:")
    while True:
        try:
            num_candidates = int(input())
            if num_candidates <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")

    for _ in range(num_candidates):
        while True:
            print("Enter candidate name:")
            name = input().strip()
            if name:
                election.add_candidate(Candidate(name))
                break
            else:
                print("Name cannot be empty. Try again.")

    while True:
        print("Enter your voter ID (or type 'exit' to finish):")
        voter_id = input().strip()
        if voter_id.lower() == 'exit':
            break
        if not voter_id:
            print("Voter ID cannot be empty. Try again.")
            continue
        print("Enter your vote:")
        vote = input().strip()
        if not election.vote(voter_id, vote):
            print(f"Vote for '{vote}' could not be recorded. Try again.")

    print("\nElection Results:")
    election.display_results()

if __name__ == "__main__":
    run_election()
