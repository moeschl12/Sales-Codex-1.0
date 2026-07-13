# Command Recipe: Task Router

Use when the user gives a new Sales Codex work request without a `TASK_TYPE`.

Steps:

1. Read `TASK_TYPES.md`.
2. Select the closest task type.
3. State the selected type briefly in chat.
4. Load only the files permitted by that task type.
5. If two task types fit equally well and the difference changes write scope, ask Felix before proceeding.

Output:

- One short sentence naming the task type.
- Then perform the task according to the selected route.

