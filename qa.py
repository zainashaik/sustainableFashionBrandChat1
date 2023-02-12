from fvalues import F

from ice.recipe import recipe


DEFAULT_CONTEXT = "We're running a hackathon on 9/9/2022 to decompose complex reasoning tasks into subtasks that are easier to automate & evaluate with language models. Our team is currently breaking down reasoning about the quality of evidence in randomized controlled trials into smaller tasks e.g. placebo, intervention adherence rate, blinding procedure, etc."

DEFAULT_QUESTION = "What is happening on 9/9/2022?"


def make_qa_prompt(context: str, question: str) -> str:
    return F(
        f"""
Background text: "{context}"

Answer the following question about the background text above:

Question: "{question}"
Answer:"
"""
#Let’s think step by step.
    ).strip()


async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt1 = make_qa_prompt(context, question)
    answer1 = await recipe.agent().complete(prompt=prompt1, stop='"')
    
    question2 = DEFAULT_QUESTION + "Improve the previous answer."
    prompt2 = make_qa_prompt(context + " Here is the previos answer: " + answer1, question2)
    answer2 = await recipe.agent().complete(prompt=prompt2, stop='"')
    # save answer

    return answer2

async def qaLoop(iters: int = 5):
    context = DEFAULT_CONTEXT
    question1 = DEFAULT_QUESTION
    prompt1 = make_qa_prompt(context, question1)
    answer = await recipe.agent().complete(prompt=prompt1, stop='"')

    question2 = DEFAULT_QUESTION + " Improve the previous answer."
    for i in range(iters):
        prompt = make_qa_prompt(context + " Here is the previous answer: " + answer, question2)
        answer = await recipe.agent().complete(prompt=prompt, stop='"')
    
    return answer






#recipe.main(answer)
recipe.main(qaLoop)
