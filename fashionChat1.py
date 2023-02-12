from fvalues import F
from ice.recipe import recipe
from ice.paper import Paper
from ice.recipe import recipe

#how to read text from file?
#sustainability definition
#company = adidas
#filename= adidas.txt
#prompt = 

sustainableDef = "A company is sustainable if they pay their workers a living wage, have supply chain transparency, and are committed to improving their sustainability initiatives. "
context1 = "Adidas does not pay most of their factory workers a living wage. They have supply chain transparency. They are committed to improving their sustainability initiatives."
question1 = "Is Adidas sustainable?"

context2 = "Express does pay their factory workers a living wage. They have supply chain transparency. They are committed to improving their sustainability initiatives."
question2 = "Is Express sustainable?"

context3 = "Haute Hijab does pay their workers a living wage. They have supply chain transparency. They are committed to improving their sustainability initiatives."
question3 = "Is Haute Hijab sustainable?"

#answer(sustainableDef+context2, question2)

DEFAULT_CONTEXT = sustainableDef + context3
DEFAULT_QUESTION = question3
#DEFAULT_CONTEXT = "A company is sustainable if they pay their workers a living wage, have supply chain transparency, and are committed to improving their sustainability initiatives. Adidas does not pay most of their factory workers a living wage. They have supply chain transparency. They are committed to improving their sustainability initiatives."
#DEFAULT_QUESTION = "Is Adidas sustainable?"


def make_qa_prompt(context: str, question: str) -> str:
    return F(
        f"""
Background text: "{context}"

Answer the following question about the background text above:

Question: "{question}"
Answer: "
"""
    ).strip()


async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt = make_qa_prompt(context, question)
    answer = await recipe.agent().complete(prompt=prompt, stop='"')
    return answer


recipe.main(answer)
