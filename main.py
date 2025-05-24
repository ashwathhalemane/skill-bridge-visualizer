from typing import List, Optional
import networkx as nx

def build_skill_graph(dependencies: dict) -> nx.DiGraph:
    G = nx.DiGraph()
    for skill, prereqs in dependencies.items():
        G.add_node(skill)
        for prereq in prereqs:
            G.add_edge(prereq, skill)  # prereq must be learned before skill
    return G

def get_learning_path(G: nx.DiGraph, known_skills: list) -> list:
    # Remove known skills and their edges from the graph
    G_filtered = G.copy()
    G_filtered.remove_nodes_from(known_skills)

    try:
        return list(nx.topological_sort(G_filtered))
    except nx.NetworkXUnfeasible:
        raise ValueError("Cycle detected in the skill graph!")

if __name__ == "__main__":
    skill_graph_data = {
        "Linux": [],
        "Networking": [],
        "Packet Analysis": ["Networking"],
        "Firewall Config": ["Linux", "Networking"],
        "SIEM Tools": ["Packet Analysis", "Firewall Config"]
    }

    G = build_skill_graph(skill_graph_data)
    learning_path = get_learning_path(G, known_skills=["Linux", "Networking"])
    print("Your personalized roadmap:")
    for i, skill in enumerate(learning_path, 1):
        print(f"{i}. {skill}")

