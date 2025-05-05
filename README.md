# skill-bridge-visualizer
tool to visualize the skill/knowledge gap 

1. Use DAG - NetworkX python library for graph implementation.
2. Create 2 graphs - one for user entered knowledge/skill, one for target skill.
3. Check for connectivity in two graphs.
4. Use Topological sorting on user graph to see if the user checks all the pre-requisites.
5. Create a connection using a third graph (or just a node) to act as bridge to connect to the target graph. 
