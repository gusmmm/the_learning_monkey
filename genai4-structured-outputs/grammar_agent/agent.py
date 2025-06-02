from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class GrammarContent(BaseModel):
    """
    Represents the content for grammar.
    """
    expression: str = Field(..., description="The expression to be analyzed for grammar."),
    classification: str = Field(..., description="The classification of the expression, e.g., 'noun', 'verb', etc."),
    explanation: str = Field(..., description="Explanation of the grammar rule or concept related to the expression."),
    example: str = Field(..., description="An example sentence using the expression in context.")
    theme: str = Field(..., description="The theme or context in which the expression is used.")

root_agent = LlmAgent(
    name="grammar_agent",
    model="gemini-2.0-flash",
    description="Agent that provides grammar explanations and examples in a structured format.",
    instruction="""
        Create a norwegian expression related to the question or theme of the user
        Analyze the provided expression for its grammatical structure.
        Classify the expression, provide an explanation of the grammar rule, and give an example sentence.
        Use the theme to contextualize the expression.
        Important: Always provide the output in a structured format as defined by the GrammarContent schema.
        The response MUST be a valid JSON object like this:
        {
            "expression": "example expression",
            "classification": "noun/verb/adjective/etc.",
            "explanation": "This is a rule about the expression.",
            "example": "This is an example sentence using the expression.",
            "theme": "related theme"
        }
        The output should include the expression, its classification, an explanation of the grammar rule, an example sentence, and the theme.
        Ensure that the expression is relevant to the user's question or theme.
        The output should be clear, concise, and educational, helping the user understand the grammar concept.
    """,
    output_schema=GrammarContent,
    output_key="grammar_content",
)