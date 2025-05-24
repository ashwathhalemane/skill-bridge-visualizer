# Skill Bridge Visualizer

## Overview

The Skill Bridge Visualizer is a Python tool that creates personalized learning roadmaps based on skill dependencies. It uses graph theory to determine the optimal order for learning skills while respecting prerequisite relationships.

## How It Works

### Core Components

#### 1. `build_skill_graph(dependencies: dict) -> nx.DiGraph`

Creates a directed graph representing skill dependencies:
- Each skill becomes a node in the graph
- Dependencies are represented as directed edges (prerequisite → skill)
- Uses NetworkX's DiGraph for efficient graph operations

**Example:**
```python
dependencies = {
    "Packet Analysis": ["Networking"],
    "Firewall Config": ["Linux", "Networking"]
}
```
Creates edges: Networking → Packet Analysis, Linux → Firewall Config, Networking → Firewall Config

#### 2. `get_learning_path(G: nx.DiGraph, known_skills: list) -> list`

Generates an optimal learning sequence:
- Removes already known skills from the graph
- Uses topological sorting to find a valid learning order
- Ensures prerequisites are always learned before dependent skills
- Raises an error if circular dependencies are detected

### Algorithm

1. **Graph Construction**: Build a directed graph where edges represent "must learn before" relationships
2. **Filtering**: Remove skills the learner already knows
3. **Topological Sort**: Find a linear ordering that respects all dependencies
4. **Path Generation**: Return the ordered list of skills to learn

### Example Use Case

The included example demonstrates a cybersecurity learning path:

**Skills and Dependencies:**
- Linux: No prerequisites
- Networking: No prerequisites  
- Packet Analysis: Requires Networking
- Firewall Config: Requires Linux and Networking
- SIEM Tools: Requires Packet Analysis and Firewall Config

**Known Skills:** Linux, Networking

**Generated Path:**
1. Packet Analysis
2. Firewall Config  
3. SIEM Tools

## Benefits

- **Dependency Awareness**: Ensures logical learning progression
- **Personalization**: Adapts to existing knowledge
- **Cycle Detection**: Prevents impossible learning sequences
- **Flexibility**: Easy to modify for different skill domains

## Usage

1. Define your skill dependencies as a dictionary
2. Specify what skills you already know
3. Run the program to get your personalized roadmap

The tool can be adapted for any domain with hierarchical skill relationships - programming languages, musical instruments, academic subjects, etc.