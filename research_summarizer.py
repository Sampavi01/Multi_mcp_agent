from mcp.server.fastmcp import FastMCP
import arxiv

mcp = FastMCP("ResearchSummarizer")

@mcp.tool()
def summarize_topic(topic: str, limit: int = 5) -> list:
    """
    Fetch top N papers from arXiv for a topic and return mini-summaries.
    Each summary contains the paper title and first 2 sentences of the abstract.
    """
    client = arxiv.Client()
    search_query = arxiv.Search(query=topic, max_results=limit)
    results = client.results(search_query)

    summaries = []
    for paper in results:
        abstract = paper.summary or ""
        short_summary = ". ".join(abstract.split(". ")[:2]) + "..."
        summaries.append(f"{paper.title} → {short_summary}")

    return summaries

if __name__ == "__main__":
    # Use stdio transport to allow MCP clients (like your Groq bot) to call this tool
    mcp.run(transport="stdio")
