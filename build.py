import sys
from pathlib import Path

# Import BRBuild from the parent directory
sys.path.append(str(Path(__file__).parent.parent))
from BRBuild.Builder import Builder

# Build the project, passing the project root to the builder
builder = Builder(Path(__file__).parent)
builder.build()