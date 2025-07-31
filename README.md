This code defines a guardrail mechanism using two agents (Teacher Agent and ClassTimings Agent) to detect and block class timing change requests from students using OpenAI Agent SDK

working:
*******

A student gives an input like “I want to change my class timings ”.

This input goes to class_timings_agent, but before it responds, the input passes through a guardrail.

The guardrail invokes the teacher_agent, which checks if the input is a change request.

If yes, the guardrail trips, and an exception is raised to block the action.

If not, the request goes through normally.

<img width="1613" height="907" alt="trigger-True" src="https://github.com/user-attachments/assets/f1a3b7e0-cd56-4514-93f6-e9323ab116c9" />
<img width="1608" height="903" alt="cmd -output" src="https://github.com/user-attachments/assets/65aaa039-757f-4a1d-a871-b5b3f8f65910" />
<img width="1611" height="908" alt="guardrailslog2" src="https://github.com/user-attachments/assets/eeee0c02-357e-45b6-825e-8363f75e7d75" />
<img width="1608" height="906" alt="Code-outputDisplay1" src="https://github.com/user-attachments/assets/3be3032d-6859-40b4-88c0-b5d7e9f908b9" />
<img width="1613" height="907" alt="Code-outputDisplay" src="https://github.com/user-attachments/assets/1c137dbe-60bb-42f4-9986-11d527a9a6de" />
<img width="1611" height="907" alt="guardrail-log" src="https://github.com/user-attachments/assets/2ae76315-3a36-40eb-8e02-b1ea6a2a9be4" />
