from agents import Agent, Runner, trace, InputGuardrailTripwireTriggered
from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from agents.items import TResponseInputItem
from connection import config
from pydantic import BaseModel
from typing import Union
import asyncio
import rich

# Output model for Teacher Agent
class TeacherResponse(BaseModel):
    reply: str
    isChangeRequest: bool

# Dummy output model for ClassTimings Agent
class ClassTimings(BaseModel):
    message: str

# Teacher Agent
teacher_agent = Agent(
    name="Teacher Agent",
    instructions="""
    You are a strict teacher. If a student tries to change class timings, your reply must still be polite,
    but mark the flag 'isChangeRequest = true'. Otherwise, mark it false.
    """,
    output_type=TeacherResponse
)

# Guardrail Function
@input_guardrail
async def change_class_guardrail(ctx, agent: Agent, input: Union[str, list]):
    result = await Runner.run(teacher_agent, input, run_config=config, context=ctx)
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isChangeRequest
    )

# Class Timings Agent (with guardrail)
class_timings_agent = Agent(
    name="ClassTimings Agent",
    instructions="""
    You are a class timings agent. Your task is to make sure students cannot change their class timings.
    """,
    input_guardrails=[change_class_guardrail],
   # output_type=ClassTimings
)

# Main Function
async def main():
    with trace("StudentClassTimings"):
        try:
            result = await Runner.run(class_timings_agent, "I want to change my class timings", run_config=config)
            rich.print(result)
            rich.print("[green]Guardrail did not trip[/green]")
        except InputGuardrailTripwireTriggered:
            rich.print("[red]Guardrail tripped: Class timings cannot be changed.[/red]")

if __name__ == "__main__":
    asyncio.run(main())
