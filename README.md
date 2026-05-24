# Q-Analyzer ✨

A lightweight and efficient Python script designed to scan, extract, and analyze numeric data from a text file (`data.txt`). It organizes numbers by their frequency, maps them to their respective structural positions (Surahs/Lines), and provides an intelligent, color-coded terminal dashboard based on value ranges.

---

## 🚀 Features

* **Intelligent Extraction:** Automatically extracts all independent numbers from the source file.
* **Surah Mapping & Detail Splitting:** Tracks precisely which line (Surah) a number appears in, including a frequency breakdown if a number appears multiple times in the same Surah.
* **Dynamic Terminal Color-Coding:** Uses standard ANSI escape codes to dynamically style outputs based on size thresholds:
    * 🟢 **Green:** Small values / short counts (1–10)
    * 🟡 **Yellow:** Medium values (11–100)
    * 🔴 **Red:** Large values (101+)
* **Final Summary Dashboard:** Provides an aggregated breakdown of total counts per range category at the end of the report.
* **No Clutter:** Professional, symmetric, and highly scannable terminal layout.

---

## 🛠️ Requirements

* Python 3.x
* A terminal that supports ANSI color codes (Standard Linux/Arch/Termux terminal, macOS Terminal, or VS Code integrated terminal).

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SPORIMEstudio/Q-Analyzer.git
   cd Q-Analyzer
   ```

2. **Run the script**
```bash
python analyzer.py
```
## 📊 Sample Output Preview

When executed, the script processes your data into organized segments followed by an actionable total summary block:
```
==================================================
            DATA ANALYSIS REPORT            
==================================================

NUMBER HEADING: 7
--------------------------------------------------
Data Sequence : 7
Total Count   : 1 times
Found In      : Surah 1
--------------------------------------------------

NUMBER HEADING: 8
--------------------------------------------------
Data Sequence : 8, 8, 8, 8
Total Count   : 4 times
Found In      : Surah 1, Surah 2, Surah 3
Detail Split  : Surah 1 (2x), Surah 2 (1x), Surah 3 (1x)
--------------------------------------------------

==================================================
               FINAL SUMMARY                
==================================================
🟢 Small Numbers (1-10)   : 4
🟡 Medium Numbers (11-100): 0
🔴 Large Numbers (101+)   : 2
--------------------------------------------------
📊 Total Numbers Found    : 6
==================================================
```

## 📄 License

This project is open-source and available under the MIT License.
