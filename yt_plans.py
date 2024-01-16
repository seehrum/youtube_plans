import json
import os
import platform
import signal
import pandas as pd

class YouTubeContentPlanner:
    def __init__(self):
        self.plans = []
        self.load_plans()

    def add_plan(self):
        try:
            num_entries = int(input("How many entries do you want to add? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        for _ in range(num_entries):
            print("\nNew Entry:")
            entry_data = {
                "Date": input("Enter the date (DD/MM/YYYY): "),
                "Video Topic": input("Enter the video topic: "),
                "Target Keywords": input("Enter the target keywords (separated by commas): "),
                "Script Status": input("Enter the script status: "),
                "Editing Status": input("Enter the editing status: "),
                "Thumbnail Creation": input("Enter the thumbnail creation status: "),
                "Scheduled Posting Date": input("Enter the scheduled posting date (DD/MM/YYYY): "),
                "Promotion Strategy": input("Enter the promotion strategy: "),
                "Audience Analysis": input("Enter the audience analysis: "),
                "Call-to-Action": input("Enter the call-to-action: "),
                "Feedback and Adjustments": input("Enter feedback and adjustments: ")
            }
            self.plans.append(entry_data)
        self.save_plans()
        print("Entry added successfully.")

    def search_plans(self, search_term):
        search_term = search_term.lower()
        results = [plan for plan in self.plans if search_term in str(plan).lower()]
        return results

    def display_plans(self):
        print(f"\n\033[1mTotal number of plans: {len(self.plans)}\033[0m")  # Bold text
        for plan in self.plans:
            print(', '.join(f"{key}: {value}" for key, value in plan.items()))

    def save_plans(self):
        try:
            with open('youtube_plans.json', 'w', encoding='utf-8') as file:
                json.dump(self.plans, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving plans: {e}")

    def load_plans(self):
        try:
            with open('youtube_plans.json', 'r', encoding='utf-8') as file:
                self.plans = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading plans: {e}")
            self.plans = []

    def export_to_excel(self):
        if not self.plans:
            print("No plans to export.")
            return

        df = pd.DataFrame(self.plans)
        excel_filename = "youtube_plans.xlsx"
        df.to_excel(excel_filename, index=False)
        print(f"Plans exported to {excel_filename}")

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def signal_handler(sig, frame):
    print("\nExiting program.")
    raise SystemExit

def main():
    signal.signal(signal.SIGINT, signal_handler)
    planner = YouTubeContentPlanner()

    while True:
        clear_screen()
        print("\nYouTube Content Planning".center(50))
        print("1. Add New Planning Entry")
        print("2. Search in Plans")
        print("3. Display All Plans")
        print("4. Export to Excel")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            planner.add_plan()

        elif choice == '2':
            search_term = input("Enter a search term: ")
            results = planner.search_plans(search_term)
            print(f"\n\033[1mSearch Results - Total Found: {len(results)}\033[0m")
            for plan in results:
                print(', '.join(f"{key}: {value}" for key, value in plan.items()))
            input("\nPress Enter to continue...")

        elif choice == '3':
            planner.display_plans()
            input("\nPress Enter to continue...")

        elif choice == '4':
            planner.export_to_excel()
            input("\nPress Enter to continue...")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
