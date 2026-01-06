# Python_scripting
A python script to seperate game files into another dedicated directory

# Game Directory Builder & Compiler

A Python automation script that scans a source directory for game projects, copies them into a clean target structure, compiles Go-based games, and generates metadata in JSON format.

---

## What This Project Does

This tool is designed to automate repetitive game project management tasks.

It:

* Scans a source directory for folders containing the word **`game`**
* Copies each game directory into a structured target folder
* Renames game folders by stripping a suffix (e.g. `_game`)
* Compiles Go (`.go`) source files inside each game directory
* Generates a `metadata.json` file summarizing all discovered games

This is useful for:

* Game build automation
* Managing multiple Go-based game projects
* Learning filesystem automation and subprocess handling in Python

---

## Example Directory Flow

### Source directory

```
projects/
├── chess_game/
├── snake_game/
├── notes/
```

### Target directory (after running script)

```
build/
├── chess/
│   ├── main.go
│   └── chess.exe
├── snake/
│   ├── main.go
│   └── snake.exe
├── metadata.json
```

---

## Prerequisites

Make sure the following are installed and available in your system `PATH`:

* **Python 3.9+**
* **Go (Golang)**
* Supported OS: Windows, Linux, macOS

Verify installations:

```bash
python --version
go version
```

---

## How to Run

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Run the script

```bash
python get_game_data.py <source_directory> <destination_directory>
```

### Example

```bash
python get_game_data.py projects build
```

---

## Generated Metadata

After execution, a `metadata.json` file is created in the target directory:

```json
{
  "GameNames": ["chess", "snake"],
  "no_of_games": 2
}
```

---

## Key Features

* Recursive directory scanning (top-level only)
* Safe directory replacement (clean rebuilds)
* Go project compilation using `go build`
* OS-independent path handling
* Structured metadata generation

---

##  How It Works (High-Level)

1. Locate game directories using a name pattern
2. Copy them into a clean target structure
3. Compile Go source files in each game folder
4. Collect and store metadata as JSON

---

##  Notes

* Game directories must contain at least one `.go` file to be compiled
* Only top-level directories are scanned (intentional design)
* Existing target directories are deleted and recreated

---

##  License

MIT License

---

##  Future Improvements

* Parallel compilation
* Configurable patterns via CLI flags
* Support for non-Go games
* Better error reporting and logs

---

Built as a practical learning project for filesystem automation, subprocess control, and build tooling in Python.
