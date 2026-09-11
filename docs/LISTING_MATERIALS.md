# Listing materials

## Proposed identity

- Name: Akiflow.
- Tagline: Plan your work and manage tasks, time slots, calendar events, and meeting follow-ups with Akiflow.
- Category: Productivity.
- Website: https://akiflow.com/mcp.
- MCP endpoint: https://mcp.akiflow.com/mcp.

## Short description

Connect Akiflow to plan your day from live tasks and calendars, then create, schedule, and update work without leaving your AI assistant.

## Long description

Akiflow connects your tasks, calendar events, time slots, projects, tags, and Meeting Assistant transcripts to your AI assistant. Review your workload, turn a plan into scheduled work, manage tasks and subtasks, adjust calendar events, and follow up from meeting action items. Each person signs in to their own Akiflow account through OAuth, so the connection uses their existing access.

## Starter prompts

- Review my meetings, open tasks, and current priorities for tomorrow. Flag conflicts before changing anything.
- Find my high-priority tasks that are unscheduled this week and propose realistic time slots around my calendar.
- Create a 90-minute time slot tomorrow morning for my quarterly report, but do not move any existing meetings.
- Show the action items from my most recent meeting and draft Akiflow tasks for the items I approve.
- Move the task named “Review pricing deck” to next Tuesday at 10 AM. Keep its existing project and priority.

## Positive acceptance tests

- Retrieve a bounded calendar and task overview without exposing data outside the selected date range.
- Create a task with an approved title, project, duration, and due date.
- Propose open time slots without scheduling or moving anything.
- Create a time slot after the user confirms its date, duration, and intended work.
- Update a calendar event while honoring the user's guest-notification instruction.

## Negative acceptance tests

- Decline to cancel an event until the user confirms the exact event and guest-notification choice.
- Do not infer a deadline, priority, project, or duration that the user did not supply or approve.
- Do not perform a broad replan after a request to inspect or summarize a schedule.

## Assets Akiflow must supply

- Provide a production logo with rights for directory display.
- Provide public support, privacy policy, and terms URLs that match the submitting Akiflow identity.
- Provide demo-account credentials and reset instructions for reviewers.
- Provide a release note that describes the MCP endpoint and supported workflows.

