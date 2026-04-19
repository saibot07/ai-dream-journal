# AI Dream Journal

AI Dream Journal is a Python-based CLI tool that helps users document their dreams, analyze them using natural language processing, and generate meaningful insights or patterns based on their entries.

## Features
- **Quick Dream Logging**: Enter quick summaries of your dreams via the terminal.
- **AI-based Analysis**: Leverages NLP (via OpenAI API or local ML models) to detect key emotions, entities, and recurring themes.
- **Dream Statistics**: Provides patterns or trends based on past dream data.
- **Privacy First**: All logs are stored locally with an optional encryption feature.
- **Export Options**: Save your dreams in TXT, JSON, or Markdown formats.

## Installation
```bash
# Clone the repository
git clone https://github.com/saibot07/ai-dream-journal.git
cd ai-dream-journal

# Set up a virtual environment (optional)
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Start logging dreams
python main.py
```

## Example
```bash
$ python main.py
Welcome to AI Dream Journal!

What did you dream about?
> I was flying over the ocean, and then I saw strange glowing lights underwater.

Analyzing your dream...
[Emotions] Liberation, Curiosity
[Entities] Ocean, Lights
[Themes] Adventure, Mystery
Dream noted successfully!
```

## Configuration
You can modify the `config.json` file to:
- Use a local NLP model instead of an API.
- Choose your output file format.
- Enable/Disable encryption.

## Roadmap
- Add support for voice-based dream input.
- Implement a GUI interface in future versions.

## Licensing
This project is licensed under the MIT License.
