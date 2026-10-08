---
name: akiflow-workflows
description: Use when the user asks to plan work, inspect an Akiflow schedule, create or update Akiflow tasks, manage time slots, or modify calendar events through Akiflow.
---

# Akiflow workflows

Use the Akiflow MCP server for live task, schedule, time-slot, calendar, and Meeting Assistant data.

## Plan before changing anything

- Inspect the relevant date range, tasks, projects, calendars, and time slots before proposing a schedule change.
- State the proposed task or calendar changes before performing a multi-item schedule replan.
- Preserve fixed commitments, calendar guests, time zones, deadlines, and task durations.
- Ask for confirmation when a change would cancel a meeting, notify guests, delete an item, or materially rewrite a schedule.

## Create reliable tasks

- Use the user's own wording for the task title.
- Set a project, tag, priority, duration, deadline, and planned date only when the user supplied or approved each value.
- Use the returned item ID when following up on a specific task, event, or time slot.
- Report what changed and any remaining ambiguity after a write operation.

## Learn user preferences and editing practices

- When the user asks to remember a preference or corrects a recurring workflow, update the user-controlled local copy of this skill or its approved private preference store with a concise, reusable rule. Keep personal preferences out of the public plugin repository and distributed archives.
- Capture explicit defaults for task wording, projects, tags, priorities, durations, scheduling, time zones, and confirmation boundaries; distinguish standing preferences from one-off instructions and ask only when that distinction would materially change future edits.
- Record task-editing best practices only after they are demonstrated by successful operations or verified against the available tool contract. Preserve existing preferences, replace superseded rules, and briefly tell the user what was saved and where.
- Read saved preferences before editing tasks and use approved defaults to avoid repeated questions. Current user instructions take precedence; preferences never authorize deletion, guest notifications, or other consequential actions on their own.
- Read the current task, change only requested fields, preserve unrelated values, and verify the resulting state after edits. Reuse verified item IDs instead of creating duplicate tasks.
- If the installed skill is read-only or changes cannot persist, use an available user-approved private store; otherwise explain the limitation and provide the proposed rule without claiming it was saved. Do not modify unrelated memory or configuration.

## Handle calendar actions carefully

- Read an event before editing or cancelling it.
- Treat invitations and guest notifications as externally visible actions.
- Confirm whether guests should be notified when modifying an event with attendees.
- Distinguish a task deadline from a scheduled calendar block.

## Return useful results

- Summarize a schedule with dates, times, time zone, and conflicts.
- Separate completed actions from suggested actions.
- Include source item IDs when they will make the next request more precise.

