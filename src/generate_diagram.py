"""
Utility script to generate a PNG and visualize the graph in this demo.
"""

from workflow.graph import graph

def generate_graph_image(output_file="graph.png"):
    """
    Generate a PNG image of the graph and save it to the specified file.

    Args:
        output_file (str): The file path to save the PNG image.
    """
    # Generate the PNG image
    graph_png = graph.get_graph().draw_mermaid_png()

    # Save the PNG to a file
    with open(output_file, "wb") as file:
        file.write(graph_png)

if __name__ == "__main__":
    generate_graph_image()