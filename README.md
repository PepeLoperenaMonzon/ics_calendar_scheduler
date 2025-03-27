# ICS Calendar Scheduler

This tool helps you download and keep your ICS calendar file up to date.

## Setup Instructions

1. Copy the example configuration file:

   ```
   copy config.ini.example config.ini
   ```

2. Edit the `config.ini` file with your settings:
   - Open `config.ini` in any text editor (like Notepad)
   - Change `ics_url` to your calendar's URL
   - Optionally change `local_file` and `hash_file` if you want different file names

## Usage

To update your calendar, simply run:

```
python src/calendar_retriever/calendar.py
```

The program will:

- Download your calendar from the specified URL
- Save it to the location specified in `local_file`
- Only update the file if there are changes

## Requirements

- Python 3.6 or newer
- The `requests` package (install with `pip install requests`)

## Troubleshooting

If you get an error saying "config.ini file not found!", make sure you:

1. Have copied the example file to `config.ini`
2. Are running the script from the project directory
3. Have edited the `config.ini` file with your calendar URL
