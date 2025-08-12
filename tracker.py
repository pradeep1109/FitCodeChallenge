import json
import os
import re
from datetime import datetime
from tabulate import tabulate

LOG_FILE = "road_to_hero.json"

def init_log_file():
    if not os.path.exists(LOG_FILE):
        print(f"📁 Creating new log file: {LOG_FILE}")
        with open(LOG_FILE, "w") as f:
            json.dump([], f, indent=2)

def load_log():
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def save_log(data):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def is_completed(entry):
    return entry["pushups"] and entry["squats"] and entry["crunches"]

def parse_lc_file(filename):
    match = re.match(r'lc-(\d+)-(.+)\.py$', filename)
    if not match:
        return None
    lc_number = int(match.group(1))
    desc = match.group(2).replace('_', ' ').title()
    return lc_number, desc

def get_creation_date(filepath):
    ts = os.path.getctime(filepath)
    return datetime.fromtimestamp(ts).date()

def prompt_fitness():
    return {
        "pushups": input("✅ Pushups done? (y/n): ").strip().lower() == 'y',
        "squats": input("✅ Squats done? (y/n): ").strip().lower() == 'y',
        "crunches": input("✅ Crunches done? (y/n): ").strip().lower() == 'y'
    }

def create_or_update_entry_from_file(filename, log):
    parsed = parse_lc_file(filename)
    if not parsed:
        return None, False
    lc_number, desc = parsed

    existing_entry = next((e for e in log if e["lc_number"] == lc_number), None)

    if existing_entry:
        if existing_entry["description"] != desc:
            print(f"✏️ Updating description for LC#{lc_number} from '{existing_entry['description']}' to '{desc}'")
            existing_entry["description"] = desc
            return None, True  # Description updated
        return None, False  # No new entry or update needed

    print(f"\n📄 Found new file: {filename}")
    print(f"➡️  LeetCode #{lc_number}: {desc}")

    file_date = get_creation_date(filename)
    print(f"📆 File creation date: {file_date}")
    use_date = input("Use this as the log date? (y/n): ").strip().lower()
    if use_date == 'y':
        log_date = str(file_date)
    else:
        log_date = input("Enter log date (YYYY-MM-DD): ").strip()

    fitness = prompt_fitness()

    new_entry = {
        "date": log_date,
        "lc_number": lc_number,
        "description": desc,
        **fitness
    }
    return new_entry, True

def display_progress(data):
    sorted_data = sorted(data, key=lambda e: (e["date"], e["lc_number"]))
    table = []
    for i, entry in enumerate(sorted_data, 1):
        table.append([
            i,
            entry["date"],
            entry["lc_number"],
            entry["description"],
            "✅" if entry["pushups"] else "❌",
            "✅" if entry["squats"] else "❌",
            "✅" if entry["crunches"] else "❌",
            "✅" if is_completed(entry) else "❌"
        ])
    headers = ["Day", "Date", "LC#", "Problem", "Pushups", "Squats", "Crunches", "Completed"]
    print("\n🏁 Progress So Far:")
    print(tabulate(table, headers=headers, tablefmt="github"))

def main():
    init_log_file()
    log = load_log()

    lc_files = [f for f in os.listdir('.') if re.match(r'lc-\d+-.+\.py$', f)]
    lc_files = sorted(lc_files)

    new_entries = []
    updated = False

    for file in lc_files:
        entry, changed = create_or_update_entry_from_file(file, log)
        if entry:
            new_entries.append(entry)
            updated = True
        elif changed:
            updated = True

    if new_entries:
        log.extend(new_entries)

    if updated:
        save_log(log)
        print(f"\n✅ Log updated.")

    else:
        print("\nℹ️ No changes detected.")

    display_progress(log)

if __name__ == "__main__":
    main()
