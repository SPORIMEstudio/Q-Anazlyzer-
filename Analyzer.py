import re
from collections import defaultdict

# Professional Terminal Colors (ANSI Escape Codes)
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Dynamic Value Colors
GREEN = "\033[32m"   # For Small numbers (1-10)
YELLOW = "\033[33m"  # For Medium numbers (11-100)
RED = "\033[31m"     # For Large numbers (101+)

def get_value_color(number):
    """Numbers ke size ke hisab se color select karne ke liye logic"""
    if number <= 10:
        return GREEN
    elif number <= 100:
        return YELLOW
    else:
        return RED

def analyze_numeric_data(file_path):
    number_map = defaultdict(list)
    
    # Categories ke counters initializing 
    green_count = 0
    yellow_count = 0
    red_count = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_idx, line in enumerate(file, start=1):
                numbers = re.findall(r'\b\d+\b', line)
                for num in numbers:
                    number_map[int(num)].append(line_idx)
                    
    except FileNotFoundError:
        print(f"\033[31mError: '{file_path}' file nahi mili. Please check karein ke file isi folder mein ho.{RESET}")
        return

    if not number_map:
        print("File mein koi valid numbers nahi mile.")
        return

    # Main Header
    print("\n" + "=" * 50)
    print(f"{BOLD}{CYAN}            DATA ANALYSIS REPORT            {RESET}")
    print("=" * 50)

    # Sorting numbers from low to high
    for num in sorted(number_map.keys()):
        line_occurrences = number_map[num]
        count = len(line_occurrences)
        
        # Category counters ko update karna (Total occurrences ke hisab se)
        if num <= 10:
            green_count += count
            COLOR = GREEN
        elif num <= 100:
            yellow_count += count
            COLOR = YELLOW
        else:
            red_count += count
            COLOR = RED
        
        # Clean Professional Layout
        print(f"\n{BOLD}{COLOR}NUMBER HEADING: {num}{RESET}")
        print("-" * 50)
        
        # Numbers Sequence display
        repeated_numbers = ", ".join([str(num)] * count)
        print(f"{BOLD}Data Sequence :{RESET} {COLOR}{repeated_numbers}{RESET}")
        
        # Total count display
        print(f"{BOLD}Total Count   :{RESET} {CYAN}{count} times{RESET}")
        
        # Surah breakdown logic
        unique_surahs = sorted(list(set(line_occurrences)))
        surah_list_str = ", ".join(f"Surah {s}" for s in unique_surahs)
        print(f"{BOLD}Found In      :{RESET} {WHITE}{surah_list_str}{RESET}")
        
        if count != len(unique_surahs):
            breakdown = [f"Surah {s} ({line_occurrences.count(s)}x)" for s in unique_surahs]
            print(f"{BOLD}Detail Split  :{RESET} {WHITE}{', '.join(breakdown)}{RESET}")
            
        print("-" * 50)

    # ==========================================
    # FINAL SUMMARY DASHBOARD (Last Breakdown)
    # ==========================================
    total_all_numbers = green_count + yellow_count + red_count
    
    print("\n" + "=" * 50)
    print(f"{BOLD}{CYAN}               FINAL SUMMARY                {RESET}")
    print("=" * 50)
    print(f"{BOLD}🟢 Small Numbers	    :{RESET} {GREEN}{green_count}{RESET}")
    print(f"{BOLD}🟡 Medium Numbers	    :{RESET} {YELLOW}{yellow_count}{RESET}")
    print(f"{BOLD}🔴 Large Numbers 	    :{RESET} {RED}{red_count}{RESET}")
    print("-" * 50)
    print(f"{BOLD}📊 Total Numbers Found    :{RESET} {BOLD}{CYAN}{total_all_numbers}{RESET}")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    analyze_numeric_data("data.txt")
